# Análisis de Asociación entre Edad y Riesgo en Neurodesarrollo
# Script simplificado en R usando solo base R

cat("=== ANÁLISIS DE ASOCIACIÓN ENTRE EDAD Y RIESGO EN NEURODESARROLLO (R) ===\n\n")

# Función principal de análisis
analisis_neurodesarrollo_simple <- function(filepath) {
  
  # 1. CARGAR DATOS
  cat("1. Cargando datos...\n")
  data <- read.csv(filepath, stringsAsFactors = FALSE)
  cat(sprintf("Dataset cargado: %d registros\n", nrow(data)))
  
  # Definir dominios
  dominios <- c(
    "zscore_desarrollo_comunicacion",
    "zscore_desarrollo_motricidad_gruesa", 
    "zscore_desarrollo_motricidad_fina",
    "zscore_desarrollo_resolucion_problemas",
    "zscore_desarrollo_socio_individual"
  )
  
  nombres_dominios <- c(
    "Comunicación",
    "Motricidad Gruesa",
    "Motricidad Fina",
    "Resolución de Problemas",
    "Desarrollo Socio-Individual"
  )
  names(nombres_dominios) <- dominios
  
  # Verificar columnas requeridas
  columnas_requeridas <- c("edad_meses_nino", dominios)
  missing_cols <- setdiff(columnas_requeridas, names(data))
  if (length(missing_cols) > 0) {
    stop(sprintf("Columnas faltantes: %s", paste(missing_cols, collapse = ", ")))
  }
  
  # Convertir edad a numérica (remover " meses" del texto)
  data$edad_meses_nino <- as.numeric(gsub(" meses", "", data$edad_meses_nino))
  
  # 2. CREAR VARIABLES DE RIESGO
  cat("2. Creando variables de riesgo...\n")
  
  # Variables de riesgo por dominio (Z <= -1 = riesgo)
  for (dominio in dominios) {
    riesgo_col <- paste0("riesgo_", gsub("zscore_desarrollo_", "", dominio))
    data[[riesgo_col]] <- ifelse(data[[dominio]] <= -1, 1, 0)
  }
  
  # Variable de riesgo global (riesgo en al menos 1 dominio)
  columnas_riesgo <- paste0("riesgo_", gsub("zscore_desarrollo_", "", dominios))
  data$riesgo_global <- ifelse(rowSums(data[columnas_riesgo], na.rm = TRUE) >= 1, 1, 0)
  
  # Mostrar prevalencia de riesgo
  cat("Variables de riesgo creadas:\n")
  for (col in c(columnas_riesgo, "riesgo_global")) {
    n_riesgo <- sum(data[[col]], na.rm = TRUE)
    pct_riesgo <- (n_riesgo / nrow(data)) * 100
    cat(sprintf("  %s: %d (%.1f%%)\n", col, n_riesgo, pct_riesgo))
  }
  
  # 3. CREAR GRUPOS DE EDAD
  cat("3. Creando grupos de edad...\n")
  
  # Estadísticas de edad
  cat(sprintf("Rango de edades: %.0f - %.0f meses\n", 
              min(data$edad_meses_nino, na.rm = TRUE), 
              max(data$edad_meses_nino, na.rm = TRUE)))
  
  # Crear grupos de edad
  breaks <- c(0, 6, 12, 18, 24, 36, 48, 60, Inf)
  labels <- c("0-6m", "6-12m", "12-18m", "18-24m", "24-36m", "36-48m", "48-60m", "60m+")
  
  data$grupo_edad <- cut(data$edad_meses_nino, 
                        breaks = breaks, 
                        labels = labels, 
                        right = FALSE)
  
  # Mostrar distribución por grupo
  cat("Distribución por grupo de edad:\n")
  print(table(data$grupo_edad))
  
  # 4. ESTADÍSTICAS DESCRIPTIVAS
  cat("4. Calculando estadísticas descriptivas...\n")
  
  # Función para calcular estadísticas por grupo
  calcular_stats <- function(x) {
    x <- x[!is.na(x)]
    if (length(x) == 0) return(rep(NA, 8))
    c(
      n = length(x),
      mean = mean(x),
      sd = sd(x),
      min = min(x),
      max = max(x),
      q25 = quantile(x, 0.25),
      q50 = quantile(x, 0.50),
      q75 = quantile(x, 0.75)
    )
  }
  
  # Calcular estadísticas por grupo y dominio
  stats_list <- list()
  for (grupo in levels(data$grupo_edad)) {
    for (dominio in dominios) {
      datos_grupo <- data[data$grupo_edad == grupo & !is.na(data[[dominio]]), dominio]
      stats_vals <- calcular_stats(datos_grupo)
      stats_list[[length(stats_list) + 1]] <- c(
        grupo_edad = grupo,
        dominio = dominio,
        stats_vals
      )
    }
  }
  
  # Convertir a data.frame
  stats_df <- do.call(rbind, lapply(stats_list, function(x) as.data.frame(t(x))))
  
  # Guardar estadísticas
  write.csv(stats_df, "estadisticas_descriptivas_R_simple.csv", row.names = FALSE)
  cat("Estadísticas descriptivas guardadas en 'estadisticas_descriptivas_R_simple.csv'\n")
  
  # 5. PRUEBAS DE NORMALIDAD
  cat("5. Realizando pruebas de normalidad...\n")
  
  normalidad_results <- list()
  for (dominio in dominios) {
    for (grupo in levels(data$grupo_edad)) {
      datos_grupo <- data[data$grupo_edad == grupo & !is.na(data[[dominio]]), dominio]
      
      if (length(datos_grupo) < 3) next
      
      # Shapiro-Wilk
      if (length(datos_grupo) <= 5000) {
        shapiro_test <- shapiro.test(datos_grupo)
        shapiro_stat <- shapiro_test$statistic
        shapiro_p <- shapiro_test$p.value
      } else {
        shapiro_stat <- NA
        shapiro_p <- NA
      }
      
      # Kolmogorov-Smirnov
      ks_test <- ks.test(datos_grupo, "pnorm", mean(datos_grupo), sd(datos_grupo))
      
      # Agregar resultados
      normalidad_results[[length(normalidad_results) + 1]] <- data.frame(
        dominio = dominio,
        grupo_edad = grupo,
        n = length(datos_grupo),
        shapiro_stat = shapiro_stat,
        shapiro_p = shapiro_p,
        ks_stat = ks_test$statistic,
        ks_p = ks_test$p.value,
        normal_shapiro = ifelse(is.na(shapiro_p), NA, shapiro_p > 0.05),
        normal_ks = ks_test$p.value > 0.05
      )
    }
  }
  
  # Convertir a data.frame
  normalidad_df <- do.call(rbind, normalidad_results)
  
  # Guardar resultados
  write.csv(normalidad_df, "pruebas_normalidad_R_simple.csv", row.names = FALSE)
  cat("Pruebas de normalidad guardadas en 'pruebas_normalidad_R_simple.csv'\n")
  
  # 6. ANÁLISIS ANOVA
  cat("6. Realizando análisis ANOVA...\n")
  
  anova_results <- list()
  for (dominio in dominios) {
    # Filtrar datos válidos
    datos_validos <- data[!is.na(data[[dominio]]) & !is.na(data$grupo_edad), 
                         c("grupo_edad", dominio)]
    
    if (nrow(datos_validos) < 10) next
    
    # ANOVA
    formula_anova <- as.formula(paste(dominio, "~ grupo_edad"))
    anova_model <- aov(formula_anova, data = datos_validos)
    anova_summary <- summary(anova_model)
    
    # Eta cuadrado
    ss_between <- anova_summary[[1]]$`Sum Sq`[1]
    ss_total <- sum(anova_summary[[1]]$`Sum Sq`)
    eta_squared <- ss_between / ss_total
    
    # Agregar resultados
    anova_results[[length(anova_results) + 1]] <- data.frame(
      dominio = nombres_dominios[dominio],
      f_statistic = anova_summary[[1]]$`F value`[1],
      p_value = anova_summary[[1]]$`Pr(>F)`[1],
      eta_squared = eta_squared,
      significativo = anova_summary[[1]]$`Pr(>F)`[1] < 0.05,
      n_total = nrow(datos_validos)
    )
  }
  
  # Convertir a data.frame
  anova_df <- do.call(rbind, anova_results)
  
  # Guardar resultados
  write.csv(anova_df, "resultados_anova_R_simple.csv", row.names = FALSE)
  cat("Resultados ANOVA guardados en 'resultados_anova_R_simple.csv'\n")
  
  # 7. ANÁLISIS CHI-CUADRADO
  cat("7. Realizando análisis Chi-cuadrado...\n")
  
  chi2_results <- list()
  
  # Análisis por dominio
  for (dominio in dominios) {
    riesgo_col <- paste0("riesgo_", gsub("zscore_desarrollo_", "", dominio))
    
    # Crear tabla de contingencia
    tabla_contingencia <- table(data$grupo_edad, data[[riesgo_col]])
    
    # Chi-cuadrado
    chi2_test <- chisq.test(tabla_contingencia)
    
    # V de Cramer
    n <- sum(tabla_contingencia)
    cramer_v <- sqrt(chi2_test$statistic / (n * (min(dim(tabla_contingencia)) - 1)))
    
    # Agregar resultados
    chi2_results[[length(chi2_results) + 1]] <- data.frame(
      dominio = nombres_dominios[dominio],
      chi2_statistic = chi2_test$statistic,
      p_value = chi2_test$p.value,
      degrees_freedom = chi2_test$parameter,
      cramer_v = cramer_v,
      significativo = chi2_test$p.value < 0.05
    )
  }
  
  # Análisis para riesgo global
  tabla_contingencia_global <- table(data$grupo_edad, data$riesgo_global)
  chi2_test_global <- chisq.test(tabla_contingencia_global)
  n_global <- sum(tabla_contingencia_global)
  cramer_v_global <- sqrt(chi2_test_global$statistic / 
                         (n_global * (min(dim(tabla_contingencia_global)) - 1)))
  
  chi2_results[[length(chi2_results) + 1]] <- data.frame(
    dominio = "Riesgo Global",
    chi2_statistic = chi2_test_global$statistic,
    p_value = chi2_test_global$p.value,
    degrees_freedom = chi2_test_global$parameter,
    cramer_v = cramer_v_global,
    significativo = chi2_test_global$p.value < 0.05
  )
  
  # Convertir a data.frame
  chi2_df <- do.call(rbind, chi2_results)
  
  # Guardar resultados
  write.csv(chi2_df, "resultados_chi2_R_simple.csv", row.names = FALSE)
  cat("Resultados Chi-cuadrado guardados en 'resultados_chi2_R_simple.csv'\n")
  
  # 8. ANÁLISIS POST-HOC (Tukey HSD)
  cat("8. Realizando análisis post-hoc...\n")
  
  for (dominio in dominios) {
    # Filtrar datos válidos
    datos_validos <- data[!is.na(data[[dominio]]) & !is.na(data$grupo_edad), 
                         c("grupo_edad", dominio)]
    
    if (nrow(datos_validos) < 10) next
    
    # Verificar si ANOVA fue significativo
    anova_significativo <- any(anova_df$dominio == nombres_dominios[dominio] & 
                              anova_df$significativo == TRUE)
    
    if (!anova_significativo) next
    
    # Tukey HSD
    anova_model <- aov(as.formula(paste(dominio, "~ grupo_edad")), data = datos_validos)
    tukey_result <- TukeyHSD(anova_model)
    
    # Convertir a dataframe
    tukey_df <- as.data.frame(tukey_result$grupo_edad)
    tukey_df$comparison <- rownames(tukey_df)
    tukey_df$significativo <- tukey_df$`p adj` < 0.05
    
    # Guardar solo comparaciones significativas
    tukey_significativo <- tukey_df[tukey_df$significativo, ]
    if (nrow(tukey_significativo) > 0) {
      filename <- paste0("tukey_", gsub("zscore_desarrollo_", "", dominio), "_R_simple.csv")
      write.csv(tukey_significativo, filename, row.names = FALSE)
      cat(sprintf("Comparaciones post-hoc significativas para %s guardadas en %s\n", 
                  nombres_dominios[dominio], filename))
    }
  }
  
  # 9. RESUMEN EJECUTIVO
  cat("9. Generando resumen ejecutivo...\n")
  
  # Crear resumen de resultados significativos
  dominios_anova_sig <- anova_df[anova_df$significativo, "dominio"]
  dominios_chi2_sig <- chi2_df[chi2_df$significativo, "dominio"]
  prevalencia_riesgo_global <- sprintf("%.1f%%", mean(data$riesgo_global, na.rm = TRUE) * 100)
  
  # Guardar resumen
  sink("resumen_ejecutivo_R_simple.txt")
  cat("=== RESUMEN EJECUTIVO DEL ANÁLISIS (R) ===\n\n")
  cat("Análisis de Asociación entre Edad y Riesgo en Neurodesarrollo\n")
  cat("Dataset:", filepath, "\n")
  cat("Fecha de análisis:", format(Sys.Date(), "%Y-%m-%d"), "\n\n")
  
  cat("Dominios con diferencias significativas por edad (ANOVA):\n")
  if (length(dominios_anova_sig) > 0) {
    for (dominio in dominios_anova_sig) {
      cat("  -", dominio, "\n")
    }
  } else {
    cat("  - Ninguno\n")
  }
  cat("\n")
  
  cat("Dominios con asociación significativa edad-riesgo (Chi-cuadrado):\n")
  if (length(dominios_chi2_sig) > 0) {
    for (dominio in dominios_chi2_sig) {
      cat("  -", dominio, "\n")
    }
  } else {
    cat("  - Ninguno\n")
  }
  cat("\n")
  
  cat("Prevalencia de riesgo global:", prevalencia_riesgo_global, "\n\n")
  
  cat("Archivos generados:\n")
  cat("  - estadisticas_descriptivas_R_simple.csv\n")
  cat("  - pruebas_normalidad_R_simple.csv\n")
  cat("  - resultados_anova_R_simple.csv\n")
  cat("  - resultados_chi2_R_simple.csv\n")
  cat("  - tukey_*_R_simple.csv (para comparaciones significativas)\n")
  sink()
  
  cat("\n=== ANÁLISIS COMPLETADO ===\n")
  cat("Resumen ejecutivo guardado en 'resumen_ejecutivo_R_simple.txt'\n")
  
  # Retornar resultados
  return(list(
    data = data,
    anova = anova_df,
    chi2 = chi2_df,
    normalidad = normalidad_df
  ))
}

# Ejecutar análisis
main <- function() {
  # Ruta al archivo de datos
  filepath <- "datos_optimizados.csv"
  
  # Verificar que el archivo existe
  if (!file.exists(filepath)) {
    stop("Archivo de datos no encontrado: ", filepath)
  }
  
  # Ejecutar análisis
  resultados <- analisis_neurodesarrollo_simple(filepath)
  
  cat("Análisis completado exitosamente.\n")
  return(resultados)
}

# Ejecutar si se llama directamente
if (sys.nframe() == 0) {
  resultados <- main()
}