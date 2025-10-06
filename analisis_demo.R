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

# Definir variables prioritarias para demostración
variables_analisis <- list(
  "Variables sociodemográficas" = c(
    "edad_meses_nino", "grupo_etnico", "area_residencia", "sexo_jefe_hogar"
  ),
  "Variables educativas" = c(
    "nivel_educativo_madre", "nivel_educativo_padre"
  ),
  "Variables socioeconómicas" = c(
    "situacion_laboral_madre", "seguro_social", "propiedad_vivienda"
  ),
  "Variables de vivienda" = c(
    "fuente_agua_consumo", "tipo_sanitario", "manejo_basura"
  ),
  "Variables de salud" = c(
    "retardo_crecimiento", "desnutricion_aguda", "vacunacion_completa"
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
    # Calcular proporciones de riesgo para cada grupo
    prop_riesgo_grupo1 <- tabla[1, "Riesgo"] / (tabla[1, "Riesgo"] + tabla[1, "Desarrollo adecuado"])
    prop_riesgo_grupo2 <- tabla[2, "Riesgo"] / (tabla[2, "Riesgo"] + tabla[2, "Desarrollo adecuado"])
    
    # Siempre calcular OR con el grupo de mayor riesgo en el numerador
    if(prop_riesgo_grupo1 >= prop_riesgo_grupo2) {
      # Grupo 1 tiene mayor riesgo
      or <- (tabla[1,"Riesgo"] * tabla[2,"Desarrollo adecuado"]) / (tabla[1,"Desarrollo adecuado"] * tabla[2,"Riesgo"])
      grupo_mayor_riesgo <- rownames(tabla)[1]
      grupo_menor_riesgo <- rownames(tabla)[2]
    } else {
      # Grupo 2 tiene mayor riesgo
      or <- (tabla[2,"Riesgo"] * tabla[1,"Desarrollo adecuado"]) / (tabla[2,"Desarrollo adecuado"] * tabla[1,"Riesgo"])
      grupo_mayor_riesgo <- rownames(tabla)[2]
      grupo_menor_riesgo <- rownames(tabla)[1]
    }
    
    # Calcular intervalo de confianza
    log_or <- log(or)
    se_log_or <- sqrt(sum(1/tabla))
    ic_inf <- exp(log_or - 1.96 * se_log_or)
    ic_sup <- exp(log_or + 1.96 * se_log_or)
    
    return(list(
      or = or,
      ic_inf = ic_inf,
      ic_sup = ic_sup,
      grupo_mayor_riesgo = grupo_mayor_riesgo,
      grupo_menor_riesgo = grupo_menor_riesgo
    ))
  } else {
    return(list(or = NA, ic_inf = NA, ic_sup = NA, grupo_mayor_riesgo = NA, grupo_menor_riesgo = NA))
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
  cat("\n", rep("=", 80), "\n")
  cat("### VARIABLE:", toupper(variable), "\n")
  cat(rep("=", 80), "\n\n")
  
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
    cat(rep("-", 50), "\n")
    
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
      tabla_con_totales <- addmargins(resultado_chi$tabla)
      print(tabla_con_totales)
      cat("\n")
      
      # Calcular y mostrar proporciones
      props <- prop.table(resultado_chi$tabla, 1) * 100
      cat("**Proporciones:**\n")
      for(i in 1:nrow(props)) {
        cat("-", rownames(props)[i], ":", 
            sprintf("%.1f%% desarrollo adecuado vs %.1f%% riesgo", 
                   props[i,"Desarrollo adecuado"], props[i,"Riesgo"]), "\n")
      }
      
      # Calcular diferencia de riesgo
      if(nrow(props) == 2) {
        diferencia <- props[1,"Riesgo"] - props[2,"Riesgo"]
        cat("- Diferencia de riesgo:", sprintf("%.1f%%", abs(diferencia)), 
            ifelse(diferencia > 0, "mayor en", "menor en"), rownames(props)[1], "\n")
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
        cat("- El riesgo de retraso en", nombres_dominios[dominio], 
            "es", sprintf("%.2f", resultado_or$or), "veces mayor en", 
            resultado_or$grupo_mayor_riesgo, "comparado con", resultado_or$grupo_menor_riesgo, "\n")
        cat("- Magnitud del efecto:", 
            ifelse(resultado_or$or < 1.5, "pequeña", 
                   ifelse(resultado_or$or < 2.5, "moderada", "grande")), "\n")
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
    resultado_or_temp <- ifelse(resultado_chi$p_valor < 0.05, 
                                list(calcular_odds_ratio(variable, dominio_riesgo, datos_var)), 
                                list(list(or = NA, ic_inf = NA, ic_sup = NA)))[[1]]
    
    resultados_variable[[dominio]] <- list(
      chi_cuadrado = resultado_chi$estadistico,
      p_valor = resultado_chi$p_valor,
      significativo = resultado_chi$p_valor < 0.05,
      or = resultado_or_temp$or,
      ic_inf = resultado_or_temp$ic_inf,
      ic_sup = resultado_or_temp$ic_sup
    )
  }
  
  # Resumen de variable
  cat(rep("=", 80), "\n")
  cat("### RESUMEN:", toupper(variable), "\n")
  cat(rep("=", 80), "\n\n")
  
  # Crear tabla resumen
  cat("| Dominio | Chi-cuadrado | p-valor | OR | IC 95% | Significativo |\n")
  cat("|---------|--------------|---------|----|---------|--------------|\n")
  
  for(dominio in names(dominios)) {
    resultado <- resultados_variable[[dominio]]
    chi_str <- ifelse(is.na(resultado$chi_cuadrado), "-", sprintf("%.2f", resultado$chi_cuadrado))
    or_str <- ifelse(is.na(resultado$or), "-", sprintf("%.2f", resultado$or))
    ic_str <- ifelse(is.na(resultado$ic_inf), "-", 
                    paste0(sprintf("%.2f", resultado$ic_inf), "-", sprintf("%.2f", resultado$ic_sup)))
    sig_str <- ifelse(resultado$significativo, "Sí", "No")
    
    cat("| ", nombres_dominios[dominio], " | ", chi_str, " | ", 
        formatear_p_valor(resultado$p_valor), " | ", or_str, " | ", 
        ic_str, " | ", sig_str, " |\n")
  }
  
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
    
    # Prioridad de intervención
    prioridad <- ifelse(dominios_significativos >= 3, "ALTA", 
                       ifelse(dominios_significativos >= 2, "MEDIA", "BAJA"))
    cat("\nPrioridad de intervención:", prioridad)
  } else {
    cat(".")
    cat("\nPrioridad de intervención: BAJA")
  }
  cat("\n\n")
  
  return(resultados_variable)
}

# Función principal para ejecutar análisis de variables prioritarias
ejecutar_analisis_demo <- function() {
  cat(rep("=", 100), "\n")
  cat("# ANÁLISIS REORGANIZADO POR VARIABLE - DEMOSTRACIÓN\n")
  cat("# Chi-cuadrado → Descripción → Odds Ratio\n")
  cat(rep("=", 100), "\n\n")
  
  todos_resultados <- list()
  
  # Seleccionar variables prioritarias para demostración
  variables_demo <- c("area_residencia", "grupo_etnico", "nivel_educativo_madre", 
                     "seguro_social", "retardo_crecimiento")
  
  for(variable in variables_demo) {
    resultado <- analizar_variable(variable, datos)
    if(!is.null(resultado)) {
      todos_resultados[[variable]] <- resultado
    }
  }
  
  # Crear resumen general
  cat(rep("=", 100), "\n")
  cat("## RESUMEN GENERAL DE VARIABLES ANALIZADAS\n")
  cat(rep("=", 100), "\n\n")
  
  cat("| Variable | Dominios afectados | OR máximo | Dominio de mayor impacto | Prioridad |\n")
  cat("|----------|-------------------|-----------|--------------------------|----------|\n")
  
  for(variable in names(todos_resultados)) {
    resultado_var <- todos_resultados[[variable]]
    dominios_afectados <- sum(sapply(resultado_var, function(x) x$significativo))
    
    if(dominios_afectados > 0) {
      ors <- sapply(resultado_var, function(x) ifelse(is.na(x$or), 0, x$or))
      max_or <- max(ors, na.rm = TRUE)
      max_dominio <- names(which.max(ors))
      
      prioridad <- ifelse(dominios_afectados >= 3, "Alta", 
                         ifelse(dominios_afectados >= 2, "Media", "Baja"))
      
      cat("| ", variable, " | ", paste0(dominios_afectados, "/5"), " | ", 
          sprintf("%.2f", max_or), " | ", nombres_dominios[max_dominio], " | ", 
          prioridad, " |\n")
    } else {
      cat("| ", variable, " | 0/5 | - | - | Baja |\n")
    }
  }
  
  cat("\n**Conclusiones principales:**\n")
  total_variables <- length(todos_resultados)
  variables_prioritarias <- sum(sapply(todos_resultados, function(x) 
    sum(sapply(x, function(y) y$significativo)) >= 2))
  
  cat("- Se analizaron", total_variables, "variables de demostración\n")
  cat("- Variables con prioridad media o alta:", variables_prioritarias, "\n")
  cat("- Se requiere análisis completo de todas las variables del estudio\n")
  cat("- Este análisis demuestra la metodología reorganizada por variable\n")
  
  return(todos_resultados)
}

# Ejecutar análisis de demostración
cat("Iniciando análisis de demostración...\n")
resultados_demo <- ejecutar_analisis_demo()

cat("\n", rep("=", 100), "\n")
cat("ANÁLISIS COMPLETADO\n")
cat("Para análisis completo, ejecutar con todas las variables del estudio.\n")
cat(rep("=", 100), "\n")