# Análisis Chi-Cuadrado Mejorado para Desarrollo Infantil
# Corrección de problemas en la interpretación de resultados estadísticamente significativos

# Usar solo funciones base de R para compatibilidad

# Función para categorizar z-scores en niveles de riesgo
categorizar_riesgo <- function(zscore) {
  # Usar clasificación estándar para z-scores de desarrollo
  ifelse(is.na(zscore), NA,
         ifelse(zscore >= -1, "Sin riesgo",
                ifelse(zscore >= -2, "Riesgo de trastorno", "Alto riesgo")))
}

# Función para calcular intervalo de confianza para proporciones
calcular_ic_proporcion <- function(x, n, conf.level = 0.95) {
  if (n == 0 || is.na(x) || is.na(n)) {
    return(list(lower = NA, upper = NA))
  }
  
  alpha <- 1 - conf.level
  z_alpha <- qnorm(1 - alpha/2)
  p <- x/n
  
  # Método de Wilson para intervalos de confianza
  center <- (p + z_alpha^2/(2*n)) / (1 + z_alpha^2/n)
  margin <- z_alpha * sqrt(p*(1-p)/n + z_alpha^2/(4*n^2)) / (1 + z_alpha^2/n)
  
  list(lower = max(0, center - margin), upper = min(1, center + margin))
}

# Función mejorada para análisis chi-cuadrado
analizar_chi_cuadrado_mejorado <- function(datos, var_independiente, var_dependiente, 
                                         min_diff_porcentaje = 2, conf.level = 0.95) {
  
  # Remover valores NA y valores vacíos
  datos_clean <- datos[!is.na(datos[[var_independiente]]) & !is.na(datos[[var_dependiente]]) & 
                      datos[[var_independiente]] != "" & datos[[var_dependiente]] != "", ]
  
  if (nrow(datos_clean) < 10) {
    return(paste("**Análisis no realizado:** Menos de 10 observaciones válidas para",
                 var_independiente, "y", var_dependiente))
  }
  
  # Crear tabla de contingencia
  tabla <- table(datos_clean[[var_independiente]], datos_clean[[var_dependiente]])
  
  # Verificar si hay suficientes datos para el análisis
  if (any(dim(tabla) < 2)) {
    return(paste("**Análisis no realizado:** Insuficiente variabilidad en las variables",
                 var_independiente, "y", var_dependiente))
  }
  
  # Calcular proporciones por fila
  prop_tabla <- prop.table(tabla, margin = 1) * 100
  
  # Determinar si usar chi-cuadrado o Fisher's exact test
  usar_fisher <- any(tabla < 5) || min(tabla) < 5
  
  # Realizar test estadístico
  if (usar_fisher && ncol(tabla) == 2 && nrow(tabla) == 2) {
    test_result <- fisher.test(tabla)
    test_name <- "Test exacto de Fisher"
    p_value <- test_result$p.value
    statistic <- NA
  } else {
    test_result <- chisq.test(tabla)
    test_name <- "Chi-cuadrado"
    p_value <- test_result$p.value
    statistic <- test_result$statistic
  }
  
  # Analizar significancia práctica
  significancia_practica <- FALSE
  categoria_conductor <- ""
  interpretacion_detallada <- ""
  
  if (p_value < 0.05) {
    # Identificar qué categoría está impulsando la significancia
    max_diff <- 0
    categoria_max <- ""
    categoria_min <- ""
    
    for (col in colnames(prop_tabla)) {
      if (nrow(prop_tabla) > 1) {
        diff_max <- max(prop_tabla[, col]) - min(prop_tabla[, col])
        if (diff_max > max_diff) {
          max_diff <- diff_max
          categoria_conductor <- col
          idx_max <- which.max(prop_tabla[, col])
          idx_min <- which.min(prop_tabla[, col])
          categoria_max <- rownames(prop_tabla)[idx_max]
          categoria_min <- rownames(prop_tabla)[idx_min]
        }
      }
    }
    
    # Verificar si la diferencia es prácticamente significativa
    if (max_diff >= min_diff_porcentaje && categoria_max != "" && categoria_min != "" && categoria_conductor != "") {
      significancia_practica <- TRUE
      interpretacion_detallada <- sprintf(
        "La significancia estadística se debe principalmente a que %s muestra mayor proporción de %s (%.1f%% vs %.1f%%, diferencia de %.1f%%)",
        categoria_max, categoria_conductor, 
        prop_tabla[categoria_max, categoria_conductor],
        prop_tabla[categoria_min, categoria_conductor],
        max_diff
      )
    } else {
      if (max_diff >= min_diff_porcentaje) {
        interpretacion_detallada <- sprintf(
          "Aunque estadísticamente significativa, la diferencia máxima es de %.1f%% (mayor al umbral de %.1f%%), pero no se pudo identificar claramente la categoría conductora",
          max_diff, min_diff_porcentaje
        )
      } else {
        interpretacion_detallada <- sprintf(
          "Aunque estadísticamente significativa, la diferencia máxima es de %.1f%% (menor al umbral de %.1f%%), lo que sugiere relevancia clínica limitada",
          max_diff, min_diff_porcentaje
        )
      }
    }
  }
  
  # Calcular intervalos de confianza para las proporciones
  ic_info <- ""
  if (p_value < 0.05) {
    ic_detalles <- c()
    for (i in 1:nrow(tabla)) {
      for (j in 1:ncol(tabla)) {
        if (tabla[i, j] > 0) {
          ic <- calcular_ic_proporcion(tabla[i, j], sum(tabla[i, ]), conf.level)
          ic_detalles <- c(ic_detalles, sprintf(
            "%s - %s: %.1f%% (IC %.0f%%: %.1f%% - %.1f%%)",
            rownames(tabla)[i], colnames(tabla)[j],
            prop_tabla[i, j], conf.level*100,
            ic$lower*100, ic$upper*100
          ))
        }
      }
    }
    ic_info <- paste(ic_detalles, collapse = "\n")
  }
  
  # Generar interpretación final
  significancia_estadistica <- ifelse(p_value < 0.05, "ES ESTADÍSTICAMENTE SIGNIFICATIVA", "NO ES ESTADÍSTICAMENTE SIGNIFICATIVA")
  
  if (usar_fisher) {
    test_info <- sprintf("%s (p = %.3f)", test_name, p_value)
  } else {
    test_info <- sprintf("%s (χ² = %.3f, p = %.3f)", test_name, statistic, p_value)
  }
  
  # Formatear resultado
  resultado <- paste0(
    "**Análisis de asociación: ", var_independiente, " vs ", var_dependiente, "**\n\n",
    "**Tabla de contingencia:**\n",
    paste(capture.output(print(tabla)), collapse = "\n"), "\n\n",
    "**Proporciones por fila:**\n",
    paste(capture.output(print(round(prop_tabla, 1))), collapse = "\n"), "\n\n",
    "**Interpretación:**\n",
    "La asociación entre ", var_independiente, " y ", var_dependiente, " ", 
    significancia_estadistica, " (", test_info, ").\n\n"
  )
  
  if (p_value < 0.05) {
    resultado <- paste0(resultado,
      "**Análisis detallado:**\n",
      interpretacion_detallada, "\n\n"
    )
    
    if (ic_info != "") {
      resultado <- paste0(resultado,
        "**Intervalos de confianza ", conf.level*100, "%:**\n",
        ic_info, "\n\n"
      )
    }
  }
  
  # Agregar limitaciones si es necesario
  limitaciones <- c()
  if (usar_fisher) {
    limitaciones <- c(limitaciones, "Se utilizó el test exacto de Fisher debido a conteos pequeños")
  }
  if (any(tabla < 10)) {
    limitaciones <- c(limitaciones, "Algunos conteos son menores a 10, interpretar con precaución")
  }
  if (!significancia_practica && p_value < 0.05) {
    limitaciones <- c(limitaciones, "Diferencias estadísticamente significativas pero prácticamente pequeñas")
  }
  
  if (length(limitaciones) > 0) {
    resultado <- paste0(resultado,
      "**Limitaciones:**\n",
      paste(paste0("- ", limitaciones), collapse = "\n"), "\n\n"
    )
  }
  
  return(resultado)
}

# Función principal para realizar todos los análisis
realizar_analisis_completo <- function(archivo_datos = "datos_optimizados.csv") {
  
  # Cargar datos
  cat("Cargando datos...\n")
  datos <- read.csv(archivo_datos, stringsAsFactors = FALSE)
  
  # Categorizar z-scores en niveles de riesgo
  cat("Categorizando z-scores en niveles de riesgo...\n")
  datos$riesgo_comunicacion <- categorizar_riesgo(datos$zscore_desarrollo_comunicacion)
  datos$riesgo_motricidad_gruesa <- categorizar_riesgo(datos$zscore_desarrollo_motricidad_gruesa)
  datos$riesgo_motricidad_fina <- categorizar_riesgo(datos$zscore_desarrollo_motricidad_fina)
  datos$riesgo_resolucion_problemas <- categorizar_riesgo(datos$zscore_desarrollo_resolucion_problemas)
  datos$riesgo_socio_individual <- categorizar_riesgo(datos$zscore_desarrollo_socio_individual)
  
  # Definir variables independientes de interés
  variables_independientes <- c("grupo_etnico", "area_residencia", "nivel_educativo_madre", 
                               "nivel_educativo_padre", "situacion_laboral_madre", 
                               "situacion_laboral_padre", "seguro_social", "sexo_nino")
  
  # Definir dominios de desarrollo
  dominios_desarrollo <- c("riesgo_comunicacion", "riesgo_motricidad_gruesa", 
                          "riesgo_motricidad_fina", "riesgo_resolucion_problemas", 
                          "riesgo_socio_individual")
  
  # Crear archivo de resultados
  archivo_resultados <- "analisis_chi_cuadrado_mejorado_resultados.txt"
  
  # Escribir encabezado
  cat("# ANÁLISIS CHI-CUADRADO MEJORADO\n", file = archivo_resultados)
  cat("# Análisis de asociaciones entre variables sociodemográficas y riesgo de desarrollo infantil\n", 
      file = archivo_resultados, append = TRUE)
  cat(paste("# Fecha:", Sys.Date(), "\n\n"), file = archivo_resultados, append = TRUE)
  
  # Realizar análisis para cada combinación
  cat("Realizando análisis chi-cuadrado mejorado...\n")
  
  for (var_indep in variables_independientes) {
    cat(paste("Analizando variable:", var_indep, "\n"))
    
    # Escribir sección de variable
    cat(paste("\n## VARIABLE:", toupper(var_indep), "\n\n"), 
        file = archivo_resultados, append = TRUE)
    
    for (dominio in dominios_desarrollo) {
      cat(paste("  - Dominio:", dominio, "\n"))
      
      # Realizar análisis
      resultado <- analizar_chi_cuadrado_mejorado(datos, var_indep, dominio)
      
      # Escribir resultado
      cat(paste("### Dominio:", toupper(gsub("riesgo_", "", dominio)), "\n\n"), 
          file = archivo_resultados, append = TRUE)
      cat(resultado, file = archivo_resultados, append = TRUE)
      cat("---\n\n", file = archivo_resultados, append = TRUE)
    }
  }
  
  cat(paste("Análisis completado. Resultados guardados en:", archivo_resultados, "\n"))
  
  # Generar resumen estadístico
  cat("\n## RESUMEN ESTADÍSTICO\n", file = archivo_resultados, append = TRUE)
  cat(paste("Total de observaciones:", nrow(datos), "\n"), file = archivo_resultados, append = TRUE)
  cat("Distribución de niveles de riesgo por dominio:\n", file = archivo_resultados, append = TRUE)
  
  for (dominio in dominios_desarrollo) {
    if (sum(!is.na(datos[[dominio]])) > 0) {
      tabla_resumen <- table(datos[[dominio]], useNA = "ifany")
      cat(paste("\n", toupper(gsub("riesgo_", "", dominio)), ":\n"), 
          file = archivo_resultados, append = TRUE)
      cat(paste(capture.output(print(tabla_resumen)), collapse = "\n"), 
          file = archivo_resultados, append = TRUE)
      cat("\n", file = archivo_resultados, append = TRUE)
    }
  }
  
  return(archivo_resultados)
}

# Ejecutar análisis si el script se ejecuta directamente
if (interactive() == FALSE) {
  cat("Iniciando análisis chi-cuadrado mejorado...\n")
  resultado_archivo <- realizar_analisis_completo()
  cat("Análisis completado exitosamente.\n")
}