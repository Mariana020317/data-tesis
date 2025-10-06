# Análisis completo de chi-cuadrado con todas las variables categóricas 
# cruzadas con los 5 dominios del neurodesarrollo
# Autor: Análisis automatizado
# Fecha: 2024

# Cargar librerías necesarias
library(tidyverse)
library(epitools)
library(exact2x2)
library(knitr)
library(kableExtra)

# Función para limpiar y preparar los datos
preparar_datos <- function(archivo_datos) {
  cat("Cargando y preparando datos...\n")
  
  # Cargar datos
  df <- read.csv(archivo_datos, stringsAsFactors = FALSE)
  
  # Variables categóricas especificadas en los requisitos
  variables_categoricas <- c(
    "edad_meses_nino", "edad_anos_madre", "edad_anos_padre", "grupo_etnico",
    "area_residencia", "nivel_educativo_madre", "nivel_educativo_padre",
    "fuente_agua_consumo", "tipo_sanitario", "manejo_basura", "tipo_energia_luz",
    "tipo_energia_cocina", "propiedad_vivienda", "sexo_jefe_hogar",
    "situacion_laboral_madre", "situacion_laboral_padre", "tipo_empleo_madre",
    "tipo_empleo_padre", "seguro_social", "total_personas_hogar", "total_hermanos",
    "posicion_nino_hermanos", "estado_civil_cuidador", "horas_pantalla",
    "horas_juego_cuidador", "numero_controles_prenatales", "ultrasonido_embarazo",
    "prenatales_primeros_3_meses", "prenatales_resto_embarazo", "servicio_asistencia_parto",
    "tipo_parto", "razon_cesarea_emergencia", "lactancia_primeros_6_meses",
    "lactancia_6-12_meses", "lactancia_12-24_meses", "vitamina_a_6-12_meses",
    "vitamina_a_12-18_meses", "vitamina_a_18-24_meses", "vitaminas_minerales_6-12_meses",
    "vitaminas_minerales_12-18_meses", "vitaminas_minerales_18-24_meses",
    "retardo_crecimiento", "desnutricion_aguda", "hospitalizado_neonatal",
    "razon_hospitalizado_neonatal", "hospitalizado_infancia", "razon_hospitalizado_infancia",
    "vacunacion_completa"
  )
  
  # Dominios del neurodesarrollo
  dominios_neurodesarrollo <- c(
    "zscore_desarrollo_comunicacion",
    "zscore_desarrollo_motricidad_gruesa", 
    "zscore_desarrollo_motricidad_fina",
    "zscore_desarrollo_resolucion_problemas",
    "zscore_desarrollo_socio_individual"
  )
  
  # Verificar que todas las variables existen
  variables_faltantes <- setdiff(variables_categoricas, names(df))
  if (length(variables_faltantes) > 0) {
    warning(paste("Variables faltantes:", paste(variables_faltantes, collapse = ", ")))
    variables_categoricas <- intersect(variables_categoricas, names(df))
  }
  
  # Convertir variables categóricas a factor
  df[variables_categoricas] <- lapply(df[variables_categoricas], as.factor)
  
  # Categorizar z-scores según los criterios especificados
  for (dominio in dominios_neurodesarrollo) {
    if (dominio %in% names(df)) {
      zscore_col <- df[[dominio]]
      categoria_col <- paste0(dominio, "_categoria")
      
      df[[categoria_col]] <- cut(zscore_col, 
                                breaks = c(-Inf, -2, -1, Inf),
                                labels = c("Alto riesgo (Z < -2)", 
                                          "Riesgo moderado (-2 ≤ Z < -1)", 
                                          "Desarrollo adecuado (Z ≥ -1)"),
                                include.lowest = TRUE)
    }
  }
  
  cat("Datos preparados exitosamente\n")
  cat("Observaciones:", nrow(df), "\n")
  cat("Variables categóricas disponibles:", length(variables_categoricas), "\n")
  cat("Dominios del neurodesarrollo:", length(dominios_neurodesarrollo), "\n")
  
  return(list(
    datos = df,
    variables_categoricas = variables_categoricas,
    dominios_neurodesarrollo = dominios_neurodesarrollo
  ))
}

# Función para realizar test chi-cuadrado o exacto de Fisher
realizar_test_estadistico <- function(tabla_contingencia) {
  # Verificar si alguna celda tiene menos de 5 observaciones
  min_esperado <- min(chisq.test(tabla_contingencia)$expected)
  
  if (min_esperado < 5 || any(tabla_contingencia < 5)) {
    # Usar test exacto de Fisher
    test_result <- fisher.test(tabla_contingencia, simulate.p.value = TRUE)
    return(list(
      test_type = "Fisher's Exact Test",
      statistic = NA,
      p_value = test_result$p.value,
      df = NA,
      method = "exact"
    ))
  } else {
    # Usar test chi-cuadrado
    test_result <- chisq.test(tabla_contingencia)
    return(list(
      test_type = "Chi-squared Test",
      statistic = test_result$statistic,
      p_value = test_result$p.value,
      df = test_result$parameter,
      method = "chi-square"
    ))
  }
}

# Función para calcular odds ratios
calcular_odds_ratio <- function(tabla_contingencia, es_significativo, alpha = 0.05) {
  if (!es_significativo) {
    return(NULL)
  }
  
  # Para tablas 2x2
  if (nrow(tabla_contingencia) == 2 && ncol(tabla_contingencia) == 2) {
    or_result <- epitools::oddsratio(tabla_contingencia, method = "wald")
    return(list(
      odds_ratio = or_result$measure[2,1],
      ci_lower = or_result$measure[2,2],
      ci_upper = or_result$measure[2,3],
      tipo_tabla = "2x2"
    ))
  }
  
  # Para tablas más grandes, calcular OR para cada categoría vs. referencia
  if (nrow(tabla_contingencia) > 2) {
    # Combinar categorías de riesgo vs. desarrollo adecuado
    tabla_combinada <- rbind(
      "Riesgo combinado" = tabla_contingencia[1,] + tabla_contingencia[2,],
      "Desarrollo adecuado" = tabla_contingencia[3,]
    )
    
    if (ncol(tabla_combinada) == 2) {
      or_result <- epitools::oddsratio(tabla_combinada, method = "wald")
      return(list(
        odds_ratio = or_result$measure[2,1],
        ci_lower = or_result$measure[2,2],
        ci_upper = or_result$measure[2,3],
        tipo_tabla = "combinada"
      ))
    }
  }
  
  return(NULL)
}

# Función para generar interpretación en español
generar_interpretacion <- function(variable_cat, dominio, tabla_contingencia, 
                                 test_result, odds_ratio, porcentajes) {
  
  # Extraer nombre del dominio sin zscore_desarrollo_
  nombre_dominio <- gsub("zscore_desarrollo_", "", dominio)
  nombre_dominio <- gsub("_", " ", nombre_dominio)
  
  # Determinar significancia
  es_significativo <- test_result$p_value < 0.05
  
  # Calcular riesgo combinado por categoría
  riesgo_combinado <- porcentajes[, "Alto riesgo (Z < -2)"] + porcentajes[, "Riesgo moderado (-2 ≤ Z < -1)"]
  
  # Encontrar categoría con mayor riesgo
  categoria_mayor_riesgo <- names(riesgo_combinado)[which.max(riesgo_combinado)]
  valor_mayor_riesgo <- max(riesgo_combinado)
  
  # Encontrar categoría con menor riesgo
  categoria_menor_riesgo <- names(riesgo_combinado)[which.min(riesgo_combinado)]
  valor_menor_riesgo <- min(riesgo_combinado)
  
  # Generar interpretación
  interpretacion <- paste0(
    "### Variable: ", variable_cat, " vs Dominio: ", nombre_dominio, "\n\n",
    "**Interpretación:**\n",
    "La asociación entre ", variable_cat, " y ", nombre_dominio, 
    ifelse(es_significativo, " ES ESTADÍSTICAMENTE SIGNIFICATIVA", " NO ES ESTADÍSTICAMENTE SIGNIFICATIVA"),
    " (", test_result$test_type, ifelse(is.na(test_result$statistic), "", 
                                      paste0(" χ² = ", round(test_result$statistic, 3))),
    ", p = ", format(test_result$p_value, scientific = TRUE, digits = 3), ").\n\n",
    
    "**Análisis detallado:**\n",
    "- ", categoria_mayor_riesgo, " presenta mayor riesgo de trastornos del neurodesarrollo (", 
    round(valor_mayor_riesgo, 1), "%)\n",
    "- Riesgo combinado: ", categoria_mayor_riesgo, " ", round(valor_mayor_riesgo, 1), 
    "% vs ", categoria_menor_riesgo, " ", round(valor_menor_riesgo, 1), 
    "% (diferencia de ", round(valor_mayor_riesgo - valor_menor_riesgo, 1), "%)\n"
  )
  
  # Agregar análisis de odds ratio si es significativo
  if (es_significativo && !is.null(odds_ratio)) {
    interpretacion <- paste0(interpretacion,
      "- Esta diferencia se debe principalmente a mayor prevalencia de alto riesgo\n\n",
      "**Odds Ratio:**\n",
      "Categorías de riesgo tienen OR = ", round(odds_ratio$odds_ratio, 2),
      " (IC 95%: ", round(odds_ratio$ci_lower, 2), " - ", round(odds_ratio$ci_upper, 2),
      ") veces mayor probabilidad de presentar trastornos del neurodesarrollo\n\n"
    )
  } else {
    interpretacion <- paste0(interpretacion, "\n")
  }
  
  # Conclusión clínica
  if (es_significativo) {
    interpretacion <- paste0(interpretacion,
      "**Conclusión clínica:**\n",
      categoria_mayor_riesgo, " requiere intervención prioritaria en el desarrollo de ", 
      nombre_dominio, "\n\n"
    )
  } else {
    interpretacion <- paste0(interpretacion,
      "**Conclusión clínica:**\n",
      "No se encontraron diferencias significativas entre grupos para ", nombre_dominio, 
      ". Se requiere monitoreo uniforme.\n\n"
    )
  }
  
  return(interpretacion)
}

# Función principal para realizar análisis completo
realizar_analisis_completo <- function(archivo_datos = "datos_optimizados.csv") {
  
  # Preparar datos
  datos_preparados <- preparar_datos(archivo_datos)
  df <- datos_preparados$datos
  variables_categoricas <- datos_preparados$variables_categoricas
  dominios_neurodesarrollo <- datos_preparados$dominios_neurodesarrollo
  
  # Crear archivo de salida
  archivo_salida <- "analisis_chi_cuadrado_completo.txt"
  cat("", file = archivo_salida) # Limpiar archivo
  
  # Escribir encabezado
  cat("# ANÁLISIS COMPLETO DE CHI-CUADRADO\n", file = archivo_salida, append = TRUE)
  cat("# Variables categóricas cruzadas con dominios del neurodesarrollo\n", file = archivo_salida, append = TRUE)
  cat("# Datos: datos_optimizados.csv\n", file = archivo_salida, append = TRUE)
  cat("# Fecha:", format(Sys.Date(), "%d/%m/%Y"), "\n\n", file = archivo_salida, append = TRUE)
  
  # Contadores para resumen
  total_analisis <- length(variables_categoricas) * length(dominios_neurodesarrollo)
  analisis_completados <- 0
  resultados_significativos <- 0
  
  cat("Iniciando análisis completo...\n")
  cat("Total de análisis a realizar:", total_analisis, "\n\n")
  
  # Iterar sobre todas las combinaciones
  for (variable_cat in variables_categoricas) {
    
    cat("## VARIABLE:", toupper(variable_cat), "\n", file = archivo_salida, append = TRUE)
    cat("=" , rep("=", 80), "\n\n", file = archivo_salida, append = TRUE)
    
    for (dominio in dominios_neurodesarrollo) {
      
      analisis_completados <- analisis_completados + 1
      dominio_categoria <- paste0(dominio, "_categoria")
      
      cat("Analizando:", variable_cat, "vs", dominio, "(", analisis_completados, "/", total_analisis, ")\n")
      
      # Verificar que ambas variables existen y no están vacías
      if (!(variable_cat %in% names(df)) || !(dominio_categoria %in% names(df))) {
        cat("### Variable: ", variable_cat, " vs Dominio: ", dominio, "\n", file = archivo_salida, append = TRUE)
        cat("ERROR: Variables no encontradas en los datos\n\n", file = archivo_salida, append = TRUE)
        next
      }
      
      # Crear subset sin valores NA
      subset_datos <- df[!is.na(df[[variable_cat]]) & !is.na(df[[dominio_categoria]]), ]
      
      if (nrow(subset_datos) < 10) {
        cat("### Variable: ", variable_cat, " vs Dominio: ", dominio, "\n", file = archivo_salida, append = TRUE)
        cat("ERROR: Datos insuficientes para análisis (n < 10)\n\n", file = archivo_salida, append = TRUE)
        next
      }
      
      # Crear tabla de contingencia
      tabla_contingencia <- table(subset_datos[[variable_cat]], subset_datos[[dominio_categoria]])
      
      # Verificar que la tabla tiene al menos 2x2
      if (nrow(tabla_contingencia) < 2 || ncol(tabla_contingencia) < 2) {
        cat("### Variable: ", variable_cat, " vs Dominio: ", dominio, "\n", file = archivo_salida, append = TRUE)
        cat("ERROR: Tabla de contingencia insuficiente\n\n", file = archivo_salida, append = TRUE)
        next
      }
      
      # Realizar test estadístico
      test_result <- realizar_test_estadistico(tabla_contingencia)
      
      # Calcular porcentajes por fila
      porcentajes <- prop.table(tabla_contingencia, margin = 1) * 100
      
      # Calcular odds ratio si es significativo
      odds_ratio <- calcular_odds_ratio(tabla_contingencia, test_result$p_value < 0.05)
      
      # Generar interpretación
      interpretacion <- generar_interpretacion(variable_cat, dominio, tabla_contingencia, 
                                             test_result, odds_ratio, porcentajes)
      
      # Escribir resultados al archivo
      cat(interpretacion, file = archivo_salida, append = TRUE)
      
      # Escribir tabla de contingencia
      cat("**Tabla de contingencia:**\n", file = archivo_salida, append = TRUE)
      cat("```\n", file = archivo_salida, append = TRUE)
      capture.output(print(tabla_contingencia), file = archivo_salida, append = TRUE)
      cat("```\n\n", file = archivo_salida, append = TRUE)
      
      # Escribir proporciones por fila
      cat("**Proporciones por fila:**\n", file = archivo_salida, append = TRUE)
      cat("```\n", file = archivo_salida, append = TRUE)
      capture.output(print(round(porcentajes, 1)), file = archivo_salida, append = TRUE)
      cat("```\n\n", file = archivo_salida, append = TRUE)
      
      # Escribir estadísticos
      cat("**Estadísticos:**\n", file = archivo_salida, append = TRUE)
      cat("- Test:", test_result$test_type, "\n", file = archivo_salida, append = TRUE)
      if (!is.na(test_result$statistic)) {
        cat("- χ² =", round(test_result$statistic, 3), "\n", file = archivo_salida, append = TRUE)
      }
      cat("- p-value =", format(test_result$p_value, scientific = TRUE, digits = 3), "\n", file = archivo_salida, append = TRUE)
      if (!is.na(test_result$df)) {
        cat("- Grados de libertad =", test_result$df, "\n", file = archivo_salida, append = TRUE)
      }
      cat("\n", file = archivo_salida, append = TRUE)
      
      # Contar si es significativo
      if (test_result$p_value < 0.05) {
        resultados_significativos <- resultados_significativos + 1
      }
      
      cat("---\n\n", file = archivo_salida, append = TRUE)
    }
    
    cat("\n", file = archivo_salida, append = TRUE)
  }
  
  # Escribir resumen final
  cat("# RESUMEN FINAL\n", file = archivo_salida, append = TRUE)
  cat("=" , rep("=", 80), "\n", file = archivo_salida, append = TRUE)
  cat("Total de análisis realizados:", analisis_completados, "\n", file = archivo_salida, append = TRUE)
  cat("Resultados estadísticamente significativos:", resultados_significativos, "\n", file = archivo_salida, append = TRUE)
  cat("Porcentaje de significancia:", round(resultados_significativos/analisis_completados*100, 1), "%\n", file = archivo_salida, append = TRUE)
  cat("Archivo de salida:", archivo_salida, "\n", file = archivo_salida, append = TRUE)
  
  cat("\n¡Análisis completo finalizado!\n")
  cat("Resultados guardados en:", archivo_salida, "\n")
  cat("Análisis completados:", analisis_completados, "/", total_analisis, "\n")
  cat("Resultados significativos:", resultados_significativos, "\n")
  
  return(archivo_salida)
}

# Función para generar resumen ejecutivo
generar_resumen_ejecutivo <- function() {
  cat("Generando resumen ejecutivo...\n")
  
  # Leer resultados del análisis
  if (!file.exists("analisis_chi_cuadrado_completo.txt")) {
    cat("ERROR: No se encontró el archivo de análisis completo\n")
    return(NULL)
  }
  
  # Crear resumen
  archivo_resumen <- "resumen_ejecutivo_chi_cuadrado.txt"
  cat("", file = archivo_resumen) # Limpiar archivo
  
  cat("# RESUMEN EJECUTIVO - ANÁLISIS CHI-CUADRADO\n", file = archivo_resumen, append = TRUE)
  cat("# Análisis de asociaciones entre variables categóricas y neurodesarrollo\n\n", file = archivo_resumen, append = TRUE)
  
  cat("## METODOLOGÍA\n", file = archivo_resumen, append = TRUE)
  cat("- Análisis chi-cuadrado para todas las combinaciones de variables categóricas\n", file = archivo_resumen, append = TRUE)
  cat("- Test exacto de Fisher para conteos pequeños\n", file = archivo_resumen, append = TRUE)
  cat("- Cálculo de odds ratios para resultados significativos\n", file = archivo_resumen, append = TRUE)
  cat("- Categorización de z-scores en tres niveles de riesgo\n\n", file = archivo_resumen, append = TRUE)
  
  cat("## INTERPRETACIÓN DE RESULTADOS\n", file = archivo_resumen, append = TRUE)
  cat("- Desarrollo adecuado: Z ≥ -1\n", file = archivo_resumen, append = TRUE)
  cat("- Riesgo moderado: -2 ≤ Z < -1\n", file = archivo_resumen, append = TRUE)
  cat("- Alto riesgo: Z < -2\n\n", file = archivo_resumen, append = TRUE)
  
  cat("Para análisis detallado, consultar: analisis_chi_cuadrado_completo.txt\n", file = archivo_resumen, append = TRUE)
  
  cat("Resumen ejecutivo generado en:", archivo_resumen, "\n")
  return(archivo_resumen)
}

# Ejecutar análisis si se corre directamente
if (interactive() || !exists("loaded_by_source")) {
  cat("=== ANÁLISIS CHI-CUADRADO COMPLETO ===\n")
  cat("Iniciando análisis automatizado...\n\n")
  
  # Verificar que existe el archivo de datos
  if (!file.exists("datos_optimizados.csv")) {
    cat("ERROR: No se encontró el archivo datos_optimizados.csv\n")
    cat("Asegúrese de que el archivo esté en el directorio de trabajo\n")
    quit(status = 1)
  }
  
  # Ejecutar análisis completo
  archivo_salida <- realizar_analisis_completo("datos_optimizados.csv")
  
  # Generar resumen ejecutivo
  generar_resumen_ejecutivo()
  
  cat("\n=== ANÁLISIS COMPLETADO ===\n")
  cat("Archivos generados:\n")
  cat("- Análisis completo: analisis_chi_cuadrado_completo.txt\n")
  cat("- Resumen ejecutivo: resumen_ejecutivo_chi_cuadrado.txt\n")
}