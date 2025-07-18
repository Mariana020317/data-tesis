# Análisis de Asociación entre Edad y Riesgo en Neurodesarrollo
# Script en R para análisis estadístico completo

# Cargar librerías necesarias
required_packages <- c("dplyr", "ggplot2", "readr", "tidyr", "car", "agricolae", "nortest", "gridExtra", "scales", "RColorBrewer", "reshape2")

# Instalar paquetes faltantes en directorio de usuario
for (package in required_packages) {
  if (!require(package, character.only = TRUE, quietly = TRUE)) {
    install.packages(package, repos = "https://cran.r-project.org", lib = "~/R/library")
    library(package, character.only = TRUE)
  }
}

# Función principal de análisis
analisis_neurodesarrollo <- function(filepath) {
  
  # Configuración inicial
  cat("=== ANÁLISIS DE ASOCIACIÓN ENTRE EDAD Y RIESGO EN NEURODESARROLLO ===\n\n")
  
  # Definir dominios y nombres
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
  
  # 1. CARGAR DATOS
  cat("1. Cargando datos...\n")
  data <- read_csv(filepath, locale = locale(encoding = "UTF-8"))
  cat(sprintf("Dataset cargado: %d registros\n", nrow(data)))
  
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
  edad_stats <- summary(data$edad_meses_nino)
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
  
  # Estadísticas por grupo de edad
  stats_por_grupo <- data %>%
    group_by(grupo_edad) %>%
    summarise(
      across(all_of(dominios), 
             list(n = ~sum(!is.na(.)),
                  mean = ~mean(., na.rm = TRUE),
                  sd = ~sd(., na.rm = TRUE),
                  min = ~min(., na.rm = TRUE),
                  max = ~max(., na.rm = TRUE),
                  q25 = ~quantile(., 0.25, na.rm = TRUE),
                  q50 = ~quantile(., 0.50, na.rm = TRUE),
                  q75 = ~quantile(., 0.75, na.rm = TRUE)),
             .names = "{.col}_{.fn}"),
      .groups = "drop"
    )
  
  # Guardar estadísticas
  write_csv(stats_por_grupo, "estadisticas_descriptivas_R.csv")
  cat("Estadísticas descriptivas guardadas en 'estadisticas_descriptivas_R.csv'\n")
  
  # 5. PRUEBAS DE NORMALIDAD
  cat("5. Realizando pruebas de normalidad...\n")
  
  resultados_normalidad <- data.frame()
  
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
      
      # Anderson-Darling
      ad_test <- ad.test(datos_grupo)
      
      # Agregar resultados
      resultados_normalidad <- rbind(resultados_normalidad, data.frame(
        dominio = dominio,
        grupo_edad = grupo,
        n = length(datos_grupo),
        shapiro_stat = shapiro_stat,
        shapiro_p = shapiro_p,
        ks_stat = ks_test$statistic,
        ks_p = ks_test$p.value,
        ad_stat = ad_test$statistic,
        ad_p = ad_test$p.value,
        normal_shapiro = ifelse(is.na(shapiro_p), NA, shapiro_p > 0.05),
        normal_ks = ks_test$p.value > 0.05,
        normal_ad = ad_test$p.value > 0.05
      ))
    }
  }
  
  # Guardar resultados
  write_csv(resultados_normalidad, "pruebas_normalidad_R.csv")
  cat("Pruebas de normalidad guardadas en 'pruebas_normalidad_R.csv'\n")
  
  # 6. PRUEBAS DE HOMOGENEIDAD
  cat("6. Realizando pruebas de homogeneidad de varianzas...\n")
  
  resultados_homogeneidad <- data.frame()
  
  for (dominio in dominios) {
    # Filtrar datos válidos
    datos_validos <- data[!is.na(data[[dominio]]) & !is.na(data$grupo_edad), 
                         c("grupo_edad", dominio)]
    
    if (nrow(datos_validos) < 10) next
    
    # Test de Levene
    levene_test <- leveneTest(datos_validos[[dominio]], datos_validos$grupo_edad)
    
    # Test de Bartlett
    bartlett_test <- bartlett.test(datos_validos[[dominio]], datos_validos$grupo_edad)
    
    # Test de Fligner-Killeen (robusto)
    fligner_test <- fligner.test(datos_validos[[dominio]], datos_validos$grupo_edad)
    
    # Agregar resultados
    resultados_homogeneidad <- rbind(resultados_homogeneidad, data.frame(
      dominio = dominio,
      levene_stat = levene_test$`F value`[1],
      levene_p = levene_test$`Pr(>F)`[1],
      bartlett_stat = bartlett_test$statistic,
      bartlett_p = bartlett_test$p.value,
      fligner_stat = fligner_test$statistic,
      fligner_p = fligner_test$p.value,
      homogeneo_levene = levene_test$`Pr(>F)`[1] > 0.05,
      homogeneo_bartlett = bartlett_test$p.value > 0.05,
      homogeneo_fligner = fligner_test$p.value > 0.05
    ))
  }
  
  # Guardar resultados
  write_csv(resultados_homogeneidad, "pruebas_homogeneidad_R.csv")
  cat("Pruebas de homogeneidad guardadas en 'pruebas_homogeneidad_R.csv'\n")
  
  # 7. ANÁLISIS ANOVA
  cat("7. Realizando análisis ANOVA...\n")
  
  resultados_anova <- data.frame()
  
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
    resultados_anova <- rbind(resultados_anova, data.frame(
      dominio = dominio,
      f_statistic = anova_summary[[1]]$`F value`[1],
      p_value = anova_summary[[1]]$`Pr(>F)`[1],
      eta_squared = eta_squared,
      significativo = anova_summary[[1]]$`Pr(>F)`[1] < 0.05,
      n_total = nrow(datos_validos)
    ))
  }
  
  # Guardar resultados
  write_csv(resultados_anova, "resultados_anova_R.csv")
  cat("Resultados ANOVA guardados en 'resultados_anova_R.csv'\n")
  
  # 8. ANÁLISIS CHI-CUADRADO
  cat("8. Realizando análisis Chi-cuadrado...\n")
  
  resultados_chi2 <- data.frame()
  
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
    resultados_chi2 <- rbind(resultados_chi2, data.frame(
      dominio = nombres_dominios[dominio],
      chi2_statistic = chi2_test$statistic,
      p_value = chi2_test$p.value,
      degrees_freedom = chi2_test$parameter,
      cramer_v = cramer_v,
      significativo = chi2_test$p.value < 0.05
    ))
  }
  
  # Análisis para riesgo global
  tabla_contingencia_global <- table(data$grupo_edad, data$riesgo_global)
  chi2_test_global <- chisq.test(tabla_contingencia_global)
  n_global <- sum(tabla_contingencia_global)
  cramer_v_global <- sqrt(chi2_test_global$statistic / 
                         (n_global * (min(dim(tabla_contingencia_global)) - 1)))
  
  resultados_chi2 <- rbind(resultados_chi2, data.frame(
    dominio = "Riesgo Global",
    chi2_statistic = chi2_test_global$statistic,
    p_value = chi2_test_global$p.value,
    degrees_freedom = chi2_test_global$parameter,
    cramer_v = cramer_v_global,
    significativo = chi2_test_global$p.value < 0.05
  ))
  
  # Guardar resultados
  write_csv(resultados_chi2, "resultados_chi2_R.csv")
  cat("Resultados Chi-cuadrado guardados en 'resultados_chi2_R.csv'\n")
  
  # 9. ANÁLISIS POST-HOC
  cat("9. Realizando análisis post-hoc...\n")
  
  # Crear directorio para resultados post-hoc
  if (!dir.exists("post_hoc_R")) dir.create("post_hoc_R")
  
  for (dominio in dominios) {
    # Filtrar datos válidos
    datos_validos <- data[!is.na(data[[dominio]]) & !is.na(data$grupo_edad), 
                         c("grupo_edad", dominio)]
    
    if (nrow(datos_validos) < 10) next
    
    # Verificar si ANOVA fue significativo
    anova_result <- resultados_anova[resultados_anova$dominio == dominio, ]
    if (nrow(anova_result) == 0 || !anova_result$significativo) next
    
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
      filename <- paste0("post_hoc_R/tukey_", gsub("zscore_desarrollo_", "", dominio), "_R.csv")
      write_csv(tukey_significativo, filename)
    }
  }
  
  # 10. CREAR VISUALIZACIONES
  cat("10. Creando visualizaciones...\n")
  
  # Crear directorio para gráficos
  if (!dir.exists("graficos_R")) dir.create("graficos_R")
  
  # Boxplots por dominio
  plots_list <- list()
  
  for (i in 1:length(dominios)) {
    dominio <- dominios[i]
    nombre_dominio <- nombres_dominios[dominio]
    
    p <- ggplot(data, aes(x = grupo_edad, y = .data[[dominio]])) +
      geom_boxplot(aes(fill = grupo_edad), alpha = 0.7) +
      geom_hline(yintercept = -1, color = "red", linetype = "dashed", alpha = 0.7) +
      labs(title = nombre_dominio, 
           x = "Grupo de Edad", 
           y = "Z-score") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1),
            legend.position = "none") +
      scale_fill_brewer(type = "qual", palette = "Set3")
    
    plots_list[[i]] <- p
  }
  
  # Guardar boxplots
  combined_plot <- grid.arrange(grobs = plots_list, ncol = 3)
  ggsave("graficos_R/boxplots_dominios_R.png", combined_plot, 
         width = 18, height = 12, dpi = 300)
  
  # Gráfico de barras para prevalencia de riesgo
  prevalencia_data <- data %>%
    select(grupo_edad, all_of(columnas_riesgo)) %>%
    pivot_longer(cols = all_of(columnas_riesgo), 
                 names_to = "dominio_riesgo", 
                 values_to = "riesgo") %>%
    group_by(grupo_edad, dominio_riesgo) %>%
    summarise(prevalencia = mean(riesgo, na.rm = TRUE) * 100, .groups = "drop") %>%
    mutate(dominio = case_when(
      dominio_riesgo == "riesgo_comunicacion" ~ "Comunicación",
      dominio_riesgo == "riesgo_motricidad_gruesa" ~ "Motricidad Gruesa",
      dominio_riesgo == "riesgo_motricidad_fina" ~ "Motricidad Fina",
      dominio_riesgo == "riesgo_resolucion_problemas" ~ "Resolución de Problemas",
      dominio_riesgo == "riesgo_socio_individual" ~ "Desarrollo Socio-Individual"
    ))
  
  p_prevalencia <- ggplot(prevalencia_data, aes(x = grupo_edad, y = prevalencia, fill = dominio)) +
    geom_bar(stat = "identity", position = "dodge", alpha = 0.8) +
    labs(title = "Prevalencia de Riesgo por Grupo de Edad y Dominio",
         x = "Grupo de Edad",
         y = "Prevalencia de Riesgo (%)",
         fill = "Dominio") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1),
          legend.position = "bottom") +
    scale_fill_brewer(type = "qual", palette = "Set2") +
    guides(fill = guide_legend(title.position = "top"))
  
  ggsave("graficos_R/prevalencia_riesgo_R.png", p_prevalencia, 
         width = 14, height = 8, dpi = 300)
  
  # Heatmap de correlaciones
  correlaciones <- cor(data[dominios], use = "complete.obs")
  rownames(correlaciones) <- nombres_dominios[rownames(correlaciones)]
  colnames(correlaciones) <- nombres_dominios[colnames(correlaciones)]
  
  # Convertir a formato largo para ggplot
  correlaciones_long <- melt(correlaciones)
  
  p_heatmap <- ggplot(correlaciones_long, aes(x = Var1, y = Var2, fill = value)) +
    geom_tile() +
    geom_text(aes(label = round(value, 2)), color = "white", size = 3) +
    scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                        midpoint = 0, limit = c(-1, 1), space = "Lab", 
                        name = "Correlación") +
    labs(title = "Correlaciones entre Dominios del Desarrollo",
         x = "", y = "") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1),
          axis.text.y = element_text(angle = 0))
  
  ggsave("graficos_R/correlaciones_dominios_R.png", p_heatmap, 
         width = 12, height = 10, dpi = 300)
  
  cat("Visualizaciones guardadas en directorio 'graficos_R/'\n")
  
  # 11. RESUMEN EJECUTIVO
  cat("11. Generando resumen ejecutivo...\n")
  
  # Crear resumen de resultados significativos
  resumen <- list(
    "Dominios con diferencias significativas por edad (ANOVA)" = 
      resultados_anova[resultados_anova$significativo, "dominio"],
    "Dominios con asociación significativa edad-riesgo (Chi-cuadrado)" = 
      resultados_chi2[resultados_chi2$significativo, "dominio"],
    "Prevalencia de riesgo global" = 
      sprintf("%.1f%%", mean(data$riesgo_global, na.rm = TRUE) * 100)
  )
  
  # Guardar resumen
  sink("resumen_ejecutivo_R.txt")
  cat("=== RESUMEN EJECUTIVO DEL ANÁLISIS ===\n\n")
  cat("Análisis de Asociación entre Edad y Riesgo en Neurodesarrollo\n")
  cat("Dataset:", filepath, "\n")
  cat("Fecha de análisis:", format(Sys.Date(), "%Y-%m-%d"), "\n\n")
  
  for (item in names(resumen)) {
    cat(item, ":\n")
    if (is.character(resumen[[item]])) {
      for (subitem in resumen[[item]]) {
        cat("  -", subitem, "\n")
      }
    } else {
      cat("  ", resumen[[item]], "\n")
    }
    cat("\n")
  }
  
  cat("Archivos generados:\n")
  cat("  - estadisticas_descriptivas_R.csv\n")
  cat("  - pruebas_normalidad_R.csv\n")
  cat("  - pruebas_homogeneidad_R.csv\n")
  cat("  - resultados_anova_R.csv\n")
  cat("  - resultados_chi2_R.csv\n")
  cat("  - post_hoc_R/ (directorio con pruebas post-hoc)\n")
  cat("  - graficos_R/ (directorio con visualizaciones)\n")
  sink()
  
  cat("\n=== ANÁLISIS COMPLETADO ===\n")
  cat("Resumen ejecutivo guardado en 'resumen_ejecutivo_R.txt'\n")
  
  # Retornar resultados
  return(list(
    data = data,
    estadisticas_descriptivas = stats_por_grupo,
    normalidad = resultados_normalidad,
    homogeneidad = resultados_homogeneidad,
    anova = resultados_anova,
    chi2 = resultados_chi2
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
  resultados <- analisis_neurodesarrollo(filepath)
  
  cat("Análisis completado exitosamente.\n")
  return(resultados)
}

# Ejecutar si se llama directamente
if (sys.nframe() == 0) {
  resultados <- main()
}