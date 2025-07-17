# Análisis Reorganizado por Variable: Chi-cuadrado → Descripción → Odds Ratio
# ========================================================================

# Cargar datos
datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)

# Definir los dominios del neurodesarrollo
dominios <- c(
  "comunicacion" = "zscore_desarrollo_comunicacion",
  "motricidad_gruesa" = "zscore_desarrollo_motricidad_gruesa", 
  "motricidad_fina" = "zscore_desarrollo_motricidad_fina",
  "resolucion_problemas" = "zscore_desarrollo_resolucion_problemas",
  "socio_individual" = "zscore_desarrollo_socio_individual"
)

# Nombres legibles para los dominios
nombres_dominios <- c(
  "comunicacion" = "Comunicación",
  "motricidad_gruesa" = "Motricidad gruesa",
  "motricidad_fina" = "Motricidad fina", 
  "resolucion_problemas" = "Resolución de problemas",
  "socio_individual" = "Socio-individual"
)

# Crear variables dicotómicas de riesgo (z-score < -1)
for(dominio in dominios) {
  nueva_var <- paste0("riesgo_", names(dominios)[dominios == dominio])
  datos[[nueva_var]] <- ifelse(datos[[dominio]] < -1, "Riesgo", "Desarrollo adecuado")
}

# Definir variables en el orden especificado
variables_analisis <- list(
  "Variables sociodemográficas" = c(
    "edad_meses_nino", "grupo_etnico", "area_residencia", "sexo_jefe_hogar"
  ),
  "Variables educativas" = c(
    "nivel_educativo_madre", "nivel_educativo_padre"
  ),
  "Variables socioeconómicas" = c(
    "situacion_laboral_madre", "situacion_laboral_padre", 
    "tipo_empleo_madre", "tipo_empleo_padre", "seguro_social", "propiedad_vivienda"
  ),
  "Variables de vivienda y servicios" = c(
    "fuente_agua_consumo", "tipo_sanitario", "manejo_basura", 
    "tipo_energia_luz", "tipo_energia_cocina"
  ),
  "Variables familiares" = c(
    "edad_anos_madre", "edad_anos_padre", "total_personas_hogar", 
    "total_hermanos", "posicion_nino_hermanos", "estado_civil_cuidador"
  ),
  "Variables de cuidado" = c(
    "horas_pantalla", "horas_juego_cuidador"
  ),
  "Variables prenatales" = c(
    "numero_controles_prenatales", "ultrasonido_embarazo", 
    "prenatales_primeros_3_meses", "prenatales_resto_embarazo", 
    "servicio_asistencia_parto", "tipo_parto", "razon_cesarea_emergencia"
  ),
  "Variables nutricionales" = c(
    "lactancia_primeros_6_meses", "lactancia_6-12_meses", "lactancia_12-24_meses",
    "vitamina_a_6-12_meses", "vitamina_a_12-18_meses", "vitamina_a_18-24_meses",
    "vitaminas_minerales_6-12_meses", "vitaminas_minerales_12-18_meses", 
    "vitaminas_minerales_18-24_meses"
  ),
  "Variables de salud" = c(
    "retardo_crecimiento", "desnutricion_aguda", "hospitalizado_neonatal", 
    "razon_hospitalizado_neonatal", "hospitalizado_infancia", 
    "razon_hospitalizado_infancia", "vacunacion_completa"
  )
)

# Función para realizar análisis Chi-cuadrado
realizar_chi_cuadrado <- function(variable, dominio_riesgo, datos) {
  # Crear tabla de contingencia
  tabla <- table(datos[[variable]], datos[[dominio_riesgo]])
  
  # Verificar si hay suficientes observaciones
  if(any(tabla < 5) && min(dim(tabla)) > 1) {
    # Usar test exacto de Fisher para tablas pequeñas
    test_result <- tryCatch({
      fisher.test(tabla)
    }, error = function(e) {
      # Si Fisher falla, usar simulación
      fisher.test(tabla, simulate.p.value = TRUE)
    })
    return(list(
      estadistico = NA,
      grados_libertad = NA,
      p_valor = test_result$p.value,
      tipo_test = "Fisher",
      tabla = tabla
    ))
  } else {
    # Usar Chi-cuadrado
    test_result <- chisq.test(tabla)
    return(list(
      estadistico = test_result$statistic,
      grados_libertad = test_result$parameter,
      p_valor = test_result$p.value,
      tipo_test = "Chi-cuadrado",
      tabla = tabla
    ))
  }
}

# Función para calcular Odds Ratio
calcular_odds_ratio <- function(variable, dominio_riesgo, datos) {
  # Crear tabla 2x2 para OR
  tabla <- table(datos[[variable]], datos[[dominio_riesgo]])
  
  if(nrow(tabla) == 2 && ncol(tabla) == 2) {
    # Calcular OR manualmente
    or <- (tabla[1,1] * tabla[2,2]) / (tabla[1,2] * tabla[2,1])
    
    # Calcular intervalo de confianza
    log_or <- log(or)
    se_log_or <- sqrt(sum(1/tabla))
    ic_inf <- exp(log_or - 1.96 * se_log_or)
    ic_sup <- exp(log_or + 1.96 * se_log_or)
    
    return(list(
      or = or,
      ic_inf = ic_inf,
      ic_sup = ic_sup
    ))
  } else {
    return(list(or = NA, ic_inf = NA, ic_sup = NA))
  }
}

# Función para formatear p-valor
formatear_p_valor <- function(p) {
  if(p < 0.001) return("< 0.001")
  if(p < 0.01) return(sprintf("%.3f", p))
  return(sprintf("%.3f", p))
}

# Función para interpretar OR
interpretar_or <- function(or) {
  if(is.na(or)) return("No aplicable")
  if(or < 1.5) return("Asociación débil")
  if(or < 2.5) return("Asociación moderada")
  if(or < 5) return("Asociación fuerte")
  return("Asociación muy fuerte")
}

# Función principal de análisis por variable
analizar_variable <- function(variable, datos) {
  cat("\n### VARIABLE:", toupper(variable), "\n\n")
  
  # Verificar si la variable existe en los datos
  if(!variable %in% names(datos)) {
    cat("**NOTA:** Variable no encontrada en los datos.\n\n")
    return(NULL)
  }
  
  # Eliminar valores faltantes
  datos_var <- datos[!is.na(datos[[variable]]), ]
  
  if(nrow(datos_var) == 0) {
    cat("**NOTA:** No hay datos válidos para esta variable.\n\n")
    return(NULL)
  }
  
  resultados_variable <- list()
  
  # Analizar cada dominio
  for(dominio in names(dominios)) {
    cat("#### DOMINIO:", nombres_dominios[dominio], "\n")
    
    dominio_riesgo <- paste0("riesgo_", dominio)
    
    # Chi-cuadrado
    resultado_chi <- realizar_chi_cuadrado(variable, dominio_riesgo, datos_var)
    
    cat("**Chi-cuadrado:**\n")
    if(resultado_chi$tipo_test == "Chi-cuadrado") {
      cat("χ² =", sprintf("%.2f", resultado_chi$estadistico), 
          ", gl =", resultado_chi$grados_libertad, 
          ", p =", formatear_p_valor(resultado_chi$p_valor), "\n\n")
    } else {
      cat("Test exacto de Fisher: p =", formatear_p_valor(resultado_chi$p_valor), "\n\n")
    }
    
    # Descripción de resultados
    if(resultado_chi$p_valor < 0.05) {
      cat("**Descripción de resultados:**\n")
      cat("- La prueba indica una asociación estadísticamente significativa entre", 
          variable, "y", nombres_dominios[dominio], "\n")
      cat("- Las diferencias observadas en las proporciones no se deben al azar\n")
      if(resultado_chi$tipo_test == "Chi-cuadrado") {
        cat("- El estadístico chi-cuadrado de", sprintf("%.2f", resultado_chi$estadistico), 
            "con", resultado_chi$grados_libertad, "grados de libertad supera el valor crítico\n")
      }
      cat("- La significancia es", 
          ifelse(resultado_chi$p_valor < 0.001, "alta", "moderada"), 
          "(p", formatear_p_valor(resultado_chi$p_valor), 
          "), indicando evidencia sólida de asociación\n\n")
      
      # Mostrar tabla de contingencia
      cat("**Tabla de contingencia:**\n")
      print(addmargins(resultado_chi$tabla))
      cat("\n")
      
      # Calcular y mostrar proporciones
      props <- prop.table(resultado_chi$tabla, 1) * 100
      cat("**Proporciones:**\n")
      for(i in 1:nrow(props)) {
        cat("-", rownames(props)[i], ":", 
            sprintf("%.1f%% riesgo vs %.1f%% desarrollo adecuado", 
                   props[i,1], props[i,2]), "\n")
      }
      cat("\n")
      
      # Odds Ratio
      cat("**Odds Ratio:**\n")
      resultado_or <- calcular_odds_ratio(variable, dominio_riesgo, datos_var)
      
      if(!is.na(resultado_or$or)) {
        cat("OR =", sprintf("%.2f", resultado_or$or), 
            "(IC 95%:", sprintf("%.2f", resultado_or$ic_inf), 
            "-", sprintf("%.2f", resultado_or$ic_sup), ")\n")
        cat("**Interpretación:**", interpretar_or(resultado_or$or), "\n")
        
        # Interpretación clínica detallada
        if(resultado_or$or > 1) {
          cat("- El riesgo de retraso en", nombres_dominios[dominio], 
              "es", sprintf("%.2f", resultado_or$or), "veces mayor\n")
        } else {
          cat("- El riesgo de retraso en", nombres_dominios[dominio], 
              "es", sprintf("%.2f", 1/resultado_or$or), "veces menor\n")
        }
      } else {
        cat("No se pudo calcular OR (tabla no 2x2)\n")
      }
      
    } else {
      cat("**Resultado:**\n")
      cat("No se encontró asociación estadísticamente significativa entre", 
          variable, "y", nombres_dominios[dominio], ".\n\n")
      
      cat("**Odds Ratio:**\n")
      cat("No aplicable (chi-cuadrado no significativo).\n")
    }
    
    cat("\n")
    
    # Guardar resultados
    resultados_variable[[dominio]] <- list(
      chi_cuadrado = resultado_chi$estadistico,
      p_valor = resultado_chi$p_valor,
      significativo = resultado_chi$p_valor < 0.05,
      or = ifelse(resultado_chi$p_valor < 0.05, 
                 calcular_odds_ratio(variable, dominio_riesgo, datos_var)$or, 
                 NA),
      ic_inf = ifelse(resultado_chi$p_valor < 0.05, 
                     calcular_odds_ratio(variable, dominio_riesgo, datos_var)$ic_inf, 
                     NA),
      ic_sup = ifelse(resultado_chi$p_valor < 0.05, 
                     calcular_odds_ratio(variable, dominio_riesgo, datos_var)$ic_sup, 
                     NA)
    )
  }
  
  # Resumen de variable
  cat("### RESUMEN:", toupper(variable), "\n\n")
  
  # Crear tabla resumen
  tabla_resumen <- data.frame(
    Dominio = nombres_dominios,
    Chi_cuadrado = sapply(resultados_variable, function(x) 
      ifelse(is.na(x$chi_cuadrado), "-", sprintf("%.2f", x$chi_cuadrado))),
    p_valor = sapply(resultados_variable, function(x) formatear_p_valor(x$p_valor)),
    OR = sapply(resultados_variable, function(x) 
      ifelse(is.na(x$or), "-", sprintf("%.2f", x$or))),
    IC_95 = sapply(resultados_variable, function(x) 
      ifelse(is.na(x$ic_inf), "-", paste0(sprintf("%.2f", x$ic_inf), "-", sprintf("%.2f", x$ic_sup)))),
    Significativo = sapply(resultados_variable, function(x) ifelse(x$significativo, "Sí", "No"))
  )
  
  print(tabla_resumen)
  
  # Conclusión clínica
  dominios_significativos <- sum(sapply(resultados_variable, function(x) x$significativo))
  cat("\n**Conclusión clínica:**\n")
  cat(variable, "afecta significativamente", dominios_significativos, "de 5 dominios del neurodesarrollo")
  
  if(dominios_significativos > 0) {
    # Encontrar el OR más alto
    ors <- sapply(resultados_variable, function(x) ifelse(is.na(x$or), 0, x$or))
    max_or_idx <- which.max(ors)
    max_or <- ors[max_or_idx]
    
    if(max_or > 0) {
      cat(", con mayor impacto en", nombres_dominios[names(max_or_idx)], 
          "(OR =", sprintf("%.2f", max_or), ").")
    }
  }
  cat("\n\n")
  
  return(resultados_variable)
}

# Función principal para ejecutar todo el análisis
ejecutar_analisis_completo <- function() {
  cat("# ANÁLISIS REORGANIZADO POR VARIABLE\n")
  cat("# Chi-cuadrado → Descripción → Odds Ratio\n")
  cat("# =====================================\n\n")
  
  todos_resultados <- list()
  
  # Procesar cada grupo de variables
  for(grupo in names(variables_analisis)) {
    cat("## ", grupo, "\n\n")
    
    for(variable in variables_analisis[[grupo]]) {
      resultado <- analizar_variable(variable, datos)
      if(!is.null(resultado)) {
        todos_resultados[[variable]] <- resultado
      }
    }
  }
  
  # Crear resumen general
  cat("## RESUMEN GENERAL DE TODAS LAS VARIABLES\n\n")
  
  resumen_general <- data.frame()
  
  for(variable in names(todos_resultados)) {
    resultado_var <- todos_resultados[[variable]]
    dominios_afectados <- sum(sapply(resultado_var, function(x) x$significativo))
    
    if(dominios_afectados > 0) {
      ors <- sapply(resultado_var, function(x) ifelse(is.na(x$or), 0, x$or))
      max_or <- max(ors, na.rm = TRUE)
      max_dominio <- names(which.max(ors))
      
      prioridad <- ifelse(dominios_afectados >= 3, "Alta", 
                         ifelse(dominios_afectados >= 2, "Media", "Baja"))
      
      resumen_general <- rbind(resumen_general, data.frame(
        Variable = variable,
        Dominios_afectados = paste0(dominios_afectados, "/5"),
        OR_maximo = sprintf("%.2f", max_or),
        Dominio_mayor_impacto = nombres_dominios[max_dominio],
        Prioridad = prioridad,
        stringsAsFactors = FALSE
      ))
    }
  }
  
  # Ordenar por prioridad y OR máximo
  resumen_general <- resumen_general[order(resumen_general$Prioridad, 
                                         -as.numeric(resumen_general$OR_maximo)), ]
  
  print(resumen_general)
  
  cat("\n\n**Conclusiones principales:**\n")
  cat("- Se analizaron", length(todos_resultados), "variables en total\n")
  cat("- Variables con alta prioridad:", 
      sum(resumen_general$Prioridad == "Alta"), "\n")
  cat("- Variables con prioridad media:", 
      sum(resumen_general$Prioridad == "Media"), "\n")
  cat("- Se requiere intervención prioritaria en las variables de alta prioridad\n")
  
  return(todos_resultados)
}

# Ejecutar análisis completo
resultados_completos <- ejecutar_analisis_completo()