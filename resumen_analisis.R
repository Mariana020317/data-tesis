# Análisis de Resumen por Variable: Chi-cuadrado y OR
# =================================================

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

# Definir todas las variables para análisis
todas_variables <- c(
  # Variables sociodemográficas
  "edad_meses_nino", "grupo_etnico", "area_residencia", "sexo_jefe_hogar",
  # Variables educativas
  "nivel_educativo_madre", "nivel_educativo_padre",
  # Variables socioeconómicas
  "situacion_laboral_madre", "situacion_laboral_padre", 
  "tipo_empleo_madre", "tipo_empleo_padre", "seguro_social", "propiedad_vivienda",
  # Variables de vivienda y servicios
  "fuente_agua_consumo", "tipo_sanitario", "manejo_basura", 
  "tipo_energia_luz", "tipo_energia_cocina",
  # Variables familiares
  "edad_anos_madre", "edad_anos_padre", "total_personas_hogar", 
  "total_hermanos", "posicion_nino_hermanos", "estado_civil_cuidador",
  # Variables de cuidado
  "horas_pantalla", "horas_juego_cuidador",
  # Variables prenatales
  "numero_controles_prenatales", "ultrasonido_embarazo", 
  "prenatales_primeros_3_meses", "prenatales_resto_embarazo", 
  "servicio_asistencia_parto", "tipo_parto", "razon_cesarea_emergencia",
  # Variables nutricionales
  "lactancia_primeros_6_meses", "lactancia_6-12_meses", "lactancia_12-24_meses",
  "vitamina_a_6-12_meses", "vitamina_a_12-18_meses", "vitamina_a_18-24_meses",
  "vitaminas_minerales_6-12_meses", "vitaminas_minerales_12-18_meses", 
  "vitaminas_minerales_18-24_meses",
  # Variables de salud
  "retardo_crecimiento", "desnutricion_aguda", "hospitalizado_neonatal", 
  "razon_hospitalizado_neonatal", "hospitalizado_infancia", 
  "razon_hospitalizado_infancia", "vacunacion_completa"
)

# Función para limpiar datos (eliminar NA y valores vacíos)
limpiar_datos <- function(datos, variable, dominio_riesgo) {
  # Crear subset sin NA ni valores vacíos
  datos_limpios <- datos[!is.na(datos[[variable]]) & 
                        !is.na(datos[[dominio_riesgo]]) & 
                        datos[[variable]] != "" & 
                        datos[[variable]] != " ", ]
  return(datos_limpios)
}

# Función para realizar análisis Chi-cuadrado
realizar_chi_cuadrado <- function(variable, dominio_riesgo, datos) {
  # Limpiar datos
  datos_limpios <- limpiar_datos(datos, variable, dominio_riesgo)
  
  if(nrow(datos_limpios) == 0) {
    return(list(
      estadistico = NA,
      grados_libertad = NA,
      p_valor = NA,
      tipo_test = "Sin datos",
      tabla = NA,
      error = TRUE
    ))
  }
  
  # Crear tabla de contingencia
  tabla <- table(datos_limpios[[variable]], datos_limpios[[dominio_riesgo]])
  
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
      tabla = tabla,
      error = FALSE
    ))
  } else {
    # Usar Chi-cuadrado
    test_result <- tryCatch({
      chisq.test(tabla)
    }, error = function(e) {
      return(list(
        estadistico = NA,
        grados_libertad = NA,
        p_valor = NA,
        tipo_test = "Error",
        tabla = tabla,
        error = TRUE
      ))
    })
    
    if(inherits(test_result, "htest")) {
      return(list(
        estadistico = test_result$statistic,
        grados_libertad = test_result$parameter,
        p_valor = test_result$p.value,
        tipo_test = "Chi-cuadrado",
        tabla = tabla,
        error = FALSE
      ))
    } else {
      return(test_result)
    }
  }
}

# Función para calcular Odds Ratio
calcular_odds_ratio <- function(variable, dominio_riesgo, datos) {
  # Limpiar datos
  datos_limpios <- limpiar_datos(datos, variable, dominio_riesgo)
  
  if(nrow(datos_limpios) == 0) {
    return(list(or = NA, ic_inf = NA, ic_sup = NA, grupo_mayor_riesgo = NA, grupo_menor_riesgo = NA))
  }
  
  # Crear tabla 2x2 para OR
  tabla <- table(datos_limpios[[variable]], datos_limpios[[dominio_riesgo]])
  
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
  if(is.na(p)) return("-")
  if(p < 0.001) return("< 0.001")
  if(p < 0.01) return(sprintf("%.3f", p))
  return(sprintf("%.3f", p))
}

# Función para formatear OR
formatear_or <- function(or, ic_inf, ic_sup) {
  if(is.na(or)) return("-")
  return(sprintf("%.2f", or))
}

# Función para formatear IC
formatear_ic <- function(ic_inf, ic_sup) {
  if(is.na(ic_inf) || is.na(ic_sup)) return("-")
  return(sprintf("%.2f-%.2f", ic_inf, ic_sup))
}

# Función para determinar significancia
es_significativo <- function(p) {
  if(is.na(p)) return("No")
  return(ifelse(p < 0.05, "Sí", "No"))
}

# Función para obtener grupo más afectado
obtener_grupo_mas_afectado <- function(variable, datos) {
  # Limpiar datos
  datos_limpios <- datos[!is.na(datos[[variable]]) & datos[[variable]] != "" & datos[[variable]] != " ", ]
  
  if(nrow(datos_limpios) == 0) {
    return("Sin datos suficientes")
  }
  
  # Calcular el promedio de riesgo por grupo para todos los dominios
  resultados_grupo <- list()
  grupos <- unique(datos_limpios[[variable]])
  
  # Verificar si hay demasiados grupos únicos (variable continua)
  if(length(grupos) > 20) {
    return("Variable continua - análisis por grupos no aplicable")
  }
  
  for(grupo in grupos) {
    datos_grupo <- datos_limpios[datos_limpios[[variable]] == grupo, ]
    
    total_riesgo <- 0
    total_dominios <- 0
    
    for(dominio in names(dominios)) {
      var_riesgo <- paste0("riesgo_", dominio)
      if(var_riesgo %in% names(datos_grupo)) {
        riesgo_count <- sum(datos_grupo[[var_riesgo]] == "Riesgo", na.rm = TRUE)
        total_count <- sum(!is.na(datos_grupo[[var_riesgo]]))
        if(total_count > 0) {
          total_riesgo <- total_riesgo + (riesgo_count / total_count)
          total_dominios <- total_dominios + 1
        }
      }
    }
    
    if(total_dominios > 0) {
      resultados_grupo[[as.character(grupo)]] <- total_riesgo / total_dominios
    }
  }
  
  if(length(resultados_grupo) == 0) {
    return("Sin datos suficientes")
  }
  
  # Convertir a vector numérico
  valores_riesgo <- unlist(resultados_grupo)
  
  # Encontrar el grupo con mayor riesgo promedio
  grupo_mas_afectado <- names(valores_riesgo)[which.max(valores_riesgo)]
  return(grupo_mas_afectado)
}

# Función principal para analizar una variable
analizar_variable <- function(variable, datos) {
  cat("### RESUMEN:", toupper(variable), "\n")
  cat("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = \n\n")
  
  # Verificar si la variable existe
  if(!variable %in% names(datos)) {
    cat("Variable no encontrada en los datos.\n\n")
    return()
  }
  
  # Crear tabla de resultados
  cat("| Dominio | Chi-cuadrado | p-valor | OR | IC 95% | Significativo |\n")
  cat("|---------|--------------|---------|----|---------|--------------|\n")
  
  dominios_significativos <- 0
  resultados_dominios <- list()
  
  for(dominio in names(dominios)) {
    var_riesgo <- paste0("riesgo_", dominio)
    
    if(var_riesgo %in% names(datos)) {
      # Realizar análisis chi-cuadrado
      resultado_chi <- realizar_chi_cuadrado(variable, var_riesgo, datos)
      
      if(!resultado_chi$error) {
        # Calcular OR si es significativo
        or_resultado <- list(or = NA, ic_inf = NA, ic_sup = NA)
        if(resultado_chi$p_valor < 0.05) {
          or_resultado <- calcular_odds_ratio(variable, var_riesgo, datos)
          dominios_significativos <- dominios_significativos + 1
        }
        
        # Formatear valores
        chi_val <- ifelse(is.na(resultado_chi$estadistico), "-", sprintf("%.2f", resultado_chi$estadistico))
        p_val <- formatear_p_valor(resultado_chi$p_valor)
        or_val <- formatear_or(or_resultado$or, or_resultado$ic_inf, or_resultado$ic_sup)
        ic_val <- formatear_ic(or_resultado$ic_inf, or_resultado$ic_sup)
        sig_val <- es_significativo(resultado_chi$p_valor)
        
        resultados_dominios[[dominio]] <- list(
          chi = chi_val,
          p = p_val,
          or = or_val,
          ic = ic_val,
          sig = sig_val
        )
      } else {
        resultados_dominios[[dominio]] <- list(
          chi = "-",
          p = "-",
          or = "-",
          ic = "-",
          sig = "No"
        )
      }
    }
  }
  
  # Imprimir tabla
  for(dominio in names(nombres_dominios)) {
    if(dominio %in% names(resultados_dominios)) {
      res <- resultados_dominios[[dominio]]
      cat(sprintf("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |\n", 
                  nombres_dominios[[dominio]], res$chi, res$p, res$or, res$ic, res$sig))
    }
  }
  
  cat("\n")
  
  # Interpretación del grupo más afectado
  grupo_mas_afectado <- obtener_grupo_mas_afectado(variable, datos)
  cat("**Interpretación:**\n")
  cat(sprintf("- Dominios con asociaciones significativas: %d/5\n", dominios_significativos))
  cat(sprintf("- Grupo más afectado: %s\n", grupo_mas_afectado))
  
  if(dominios_significativos > 0) {
    cat("- Esta variable muestra asociaciones significativas con el neurodesarrollo\n")
  } else {
    cat("- Esta variable no muestra asociaciones significativas con el neurodesarrollo\n")
  }
  
  cat("\n")
  cat("================================================================================\n\n")
}

# Ejecutar análisis para todas las variables
cat("ANÁLISIS DE RESUMEN POR VARIABLE\n")
cat("================================\n\n")

for(variable in todas_variables) {
  analizar_variable(variable, datos)
}

cat("ANÁLISIS COMPLETADO\n")
cat("===================\n")