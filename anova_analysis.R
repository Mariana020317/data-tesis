# =============================================================================
# ANOVA Analysis Script for Developmental Z-Scores (Base R Version)
# Author: Generated for data-tesis project
# Purpose: Perform one-way ANOVA analysis for sociodemographic, environmental, 
#          and clinical variables with five developmental z-score domains
# =============================================================================

# =============================================================================
# Configuration and Setup
# =============================================================================

# Set working directory to script location
setwd("/home/runner/work/data-tesis/data-tesis")

# Z-score domains (dependent variables)
zscore_domains <- c(
  "zscore_desarrollo_comunicacion",
  "zscore_desarrollo_motricidad_gruesa", 
  "zscore_desarrollo_motricidad_fina",
  "zscore_desarrollo_resolucion_problemas",
  "zscore_desarrollo_socio_individual"
)

# Spanish names for domains (for LaTeX output)
domain_names_spanish <- c(
  "Comunicación",
  "Motricidad gruesa",
  "Motricidad fina", 
  "Resolución de problemas",
  "Socio-individual"
)

# Independent variables to test
independent_vars <- c(
  "edad_meses_nino", "edad_anos_madre", "edad_anos_padre",
  "grupo_etnico", "area_residencia", 
  "nivel_educativo_madre", "nivel_educativo_padre",
  "fuente_agua_consumo", "tipo_sanitario", "manejo_basura",
  "tipo_energia_luz", "tipo_energia_cocina", "propiedad_vivienda",
  "sexo_jefe_hogar", "situacion_laboral_madre", "situacion_laboral_padre",
  "tipo_empleo_madre", "tipo_empleo_padre", "seguro_social",
  "total_personas_hogar", "total_hermanos", "posicion_nino_hermanos",
  "estado_civil_cuidador", "horas_pantalla", "horas_juego_cuidador",
  "numero_controles_prenatales", "ultrasonido_embarazo",
  "prenatales_primeros_3_meses", "prenatales_resto_embarazo",
  "servicio_asistencia_parto", "tipo_parto", "razon_cesarea_emergencia",
  "lactancia_primeros_6_meses", "lactancia_6.12_meses", "lactancia_12.24_meses",
  "vitamina_a_6.12_meses", "vitamina_a_12.18_meses", "vitamina_a_18.24_meses",
  "vitaminas_minerales_6.12_meses", "vitaminas_minerales_12.18_meses", 
  "vitaminas_minerales_18.24_meses", "retardo_crecimiento", "desnutricion_aguda",
  "hospitalizado_neonatal", "razon_hospitalizado_neonatal",
  "hospitalizado_infancia", "razon_hospitalizado_infancia", "vacunacion_completa"
)

# =============================================================================
# Data Loading and Preparation Functions
# =============================================================================

load_and_clean_data <- function(file_path) {
  cat("Loading data from:", file_path, "\n")
  
  # Read data
  data <- read.csv(file_path, stringsAsFactors = FALSE, na.strings = c("", "NA"))
  
  cat("Original dataset dimensions:", dim(data), "\n")
  
  # Convert logical columns
  logical_cols <- c("ultrasonido_embarazo", "prenatales_primeros_3_meses", 
                   "prenatales_resto_embarazo", "retardo_crecimiento",
                   "desnutricion_aguda", "hospitalizado_neonatal",
                   "hospitalizado_infancia", "vacunacion_completa")
  
  for(col in logical_cols) {
    if(col %in% names(data)) {
      data[[col]] <- ifelse(data[[col]] == "Sí", "Sí", 
                           ifelse(data[[col]] == "No", "No", NA))
    }
  }
  
  # Convert vitamin columns from VERDADERO/FALSO to Sí/No
  vitamin_cols <- grep("vitamina_a_|vitaminas_minerales_", names(data), value = TRUE)
  for(col in vitamin_cols) {
    if(col %in% names(data)) {
      data[[col]] <- ifelse(data[[col]] == "VERDADERO", "Sí", 
                           ifelse(data[[col]] == "FALSO", "No", NA))
    }
  }
  
  # Handle continuous variables - convert to categorical for ANOVA
  # Clean and convert edad_meses_nino to numeric
  if("edad_meses_nino" %in% names(data)) {
    data$edad_meses_nino_numeric <- as.numeric(gsub(" meses", "", data$edad_meses_nino))
    data$edad_meses_nino_cat <- cut(data$edad_meses_nino_numeric, 
                                   breaks = quantile(data$edad_meses_nino_numeric, 
                                                   probs = 0:4/4, na.rm = TRUE),
                                   labels = c("0-25%", "25-50%", "50-75%", "75-100%"),
                                   include.lowest = TRUE)
  }
  
  if("edad_anos_madre" %in% names(data)) {
    data$edad_anos_madre_cat <- cut(data$edad_anos_madre, 
                                   breaks = c(0, 20, 25, 30, 35, Inf),
                                   labels = c("≤20", "21-25", "26-30", "31-35", ">35"),
                                   include.lowest = TRUE)
  }
  
  if("edad_anos_padre" %in% names(data)) {
    data$edad_anos_padre_cat <- cut(data$edad_anos_padre, 
                                   breaks = c(0, 25, 30, 35, 40, Inf),
                                   labels = c("≤25", "26-30", "31-35", "36-40", ">40"),
                                   include.lowest = TRUE)
  }
  
  cat("Data loaded and cleaned successfully\n")
  return(data)
}

# =============================================================================
# Statistical Analysis Functions
# =============================================================================

# Function to check normality (simplified)
check_normality <- function(data, group_var, outcome_var) {
  # Split data by groups
  groups <- split(data[[outcome_var]], data[[group_var]])
  
  normality_results <- sapply(groups, function(x) {
    if(length(x) > 2 && !all(is.na(x))) {
      if(length(x) <= 5000) {
        shapiro.test(x)$p.value
      } else {
        # For large samples, approximate normality
        return(0.1)  # Assume normality for large samples
      }
    } else {
      NA
    }
  })
  
  return(normality_results)
}

# Function to check homogeneity of variance (simplified)
check_homogeneity <- function(data, group_var, outcome_var) {
  # Remove NA values
  clean_data <- data[!is.na(data[[group_var]]) & !is.na(data[[outcome_var]]), ]
  
  if(nrow(clean_data) < 10) return(NA)
  
  # Simple variance ratio test
  groups <- split(clean_data[[outcome_var]], clean_data[[group_var]])
  group_vars <- sapply(groups, var, na.rm = TRUE)
  
  # If variance ratio is too high, assume heterogeneity
  max_var <- max(group_vars, na.rm = TRUE)
  min_var <- min(group_vars, na.rm = TRUE)
  
  if(max_var/min_var > 4) {
    return(0.01)  # Assume heterogeneity
  } else {
    return(0.1)   # Assume homogeneity
  }
}

# Function to classify z-scores
classify_zscore <- function(zscore) {
  ifelse(zscore > -1, "Desarrollo adecuado",
         ifelse(zscore >= -2, "Riesgo de trastornos en el neurodesarrollo",
                "Riesgo alto de trastornos en el neurodesarrollo"))
}

# Function to calculate descriptive statistics
calculate_descriptives <- function(data, group_var, outcome_var) {
  clean_data <- data[!is.na(data[[group_var]]) & !is.na(data[[outcome_var]]), ]
  
  # Split data by groups
  groups <- split(clean_data[[outcome_var]], clean_data[[group_var]])
  
  # Calculate descriptives for each group
  descriptives <- data.frame(
    Group = names(groups),
    n = sapply(groups, length),
    mean = sapply(groups, mean, na.rm = TRUE),
    sd = sapply(groups, sd, na.rm = TRUE),
    desarrollo_adecuado = sapply(groups, function(x) sum(x > -1, na.rm = TRUE)),
    riesgo_trastornos = sapply(groups, function(x) sum(x >= -2 & x <= -1, na.rm = TRUE)),
    riesgo_alto = sapply(groups, function(x) sum(x < -2, na.rm = TRUE)),
    stringsAsFactors = FALSE
  )
  
  # Calculate percentages
  descriptives$pct_desarrollo_adecuado <- round(descriptives$desarrollo_adecuado / descriptives$n * 100, 1)
  descriptives$pct_riesgo_trastornos <- round(descriptives$riesgo_trastornos / descriptives$n * 100, 1)
  descriptives$pct_riesgo_alto <- round(descriptives$riesgo_alto / descriptives$n * 100, 1)
  
  return(descriptives)
}

# Main ANOVA analysis function
perform_anova_analysis <- function(data, group_var, outcome_var) {
  # Clean data
  clean_data <- data[!is.na(data[[group_var]]) & !is.na(data[[outcome_var]]), ]
  
  # Check if we have enough data
  if(nrow(clean_data) < 10) {
    return(list(
      valid = FALSE,
      reason = "Insufficient data"
    ))
  }
  
  # Check number of groups
  n_groups <- length(unique(clean_data[[group_var]]))
  if(n_groups < 2) {
    return(list(
      valid = FALSE,
      reason = "Less than 2 groups"
    ))
  }
  
  # Check assumptions
  normality_p <- check_normality(clean_data, group_var, outcome_var)
  homogeneity_p <- check_homogeneity(clean_data, group_var, outcome_var)
  
  # Determine which test to use
  use_welch <- !is.na(homogeneity_p) && homogeneity_p < 0.05
  
  # Perform ANOVA
  if(use_welch) {
    # Welch's ANOVA
    anova_result <- tryCatch({
      oneway.test(clean_data[[outcome_var]] ~ clean_data[[group_var]], 
                 var.equal = FALSE)
    }, error = function(e) NULL)
    
    if(is.null(anova_result)) {
      return(list(valid = FALSE, reason = "ANOVA failed"))
    }
    
    test_statistic <- anova_result$statistic
    p_value <- anova_result$p.value
    test_type <- "Welch's ANOVA"
    
  } else {
    # Standard ANOVA
    anova_result <- tryCatch({
      aov(clean_data[[outcome_var]] ~ clean_data[[group_var]])
    }, error = function(e) NULL)
    
    if(is.null(anova_result)) {
      return(list(valid = FALSE, reason = "ANOVA failed"))
    }
    
    anova_summary <- summary(anova_result)
    test_statistic <- anova_summary[[1]]$`F value`[1]
    p_value <- anova_summary[[1]]$`Pr(>F)`[1]
    test_type <- "Standard ANOVA"
  }
  
  # Calculate descriptives
  descriptives <- calculate_descriptives(clean_data, group_var, outcome_var)
  
  # Post-hoc tests if significant (simplified)
  posthoc_results <- NULL
  if(!is.na(p_value) && p_value < 0.05 && n_groups > 2) {
    # Simplified post-hoc using pairwise t-tests
    posthoc_results <- tryCatch({
      pairwise.t.test(clean_data[[outcome_var]], clean_data[[group_var]], 
                     p.adjust.method = "bonferroni")
    }, error = function(e) NULL)
  }
  
  return(list(
    valid = TRUE,
    test_type = test_type,
    test_statistic = test_statistic,
    p_value = p_value,
    significant = !is.na(p_value) && p_value < 0.05,
    normality_p = normality_p,
    homogeneity_p = homogeneity_p,
    descriptives = descriptives,
    posthoc = posthoc_results,
    n_total = nrow(clean_data),
    n_groups = n_groups
  ))
}

# =============================================================================
# LaTeX Table Generation Functions
# =============================================================================

generate_latex_table <- function(var_name, var_results, output_file) {
  # Create table header
  latex_header <- paste0(
    "\\begin{table}[H]\n",
    "\\centering\n",
    "\\caption{Análisis ANOVA para ", var_name, "}\n",
    "\\label{tab:", gsub("_", "", var_name), "}\n",
    "\\begin{tabular}{|l|c|c|c|c|c|}\n",
    "\\hline\n",
    "& \\textbf{Comunicación} & \\textbf{Motricidad gruesa} & \\textbf{Motricidad fina} & \\textbf{Resolución problemas} & \\textbf{Socio-individual} \\\\\n",
    "\\hline\n"
  )
  
  # Extract results for each domain
  results_summary <- data.frame(
    Domain = domain_names_spanish,
    F_stat = sapply(var_results, function(x) if(x$valid) round(x$test_statistic, 3) else "N/A"),
    p_value = sapply(var_results, function(x) if(x$valid) {
      if(x$p_value < 0.001) "< 0.001" else round(x$p_value, 3)
    } else "N/A"),
    significant = sapply(var_results, function(x) if(x$valid) ifelse(x$significant, "Sí", "No") else "N/A"),
    test_type = sapply(var_results, function(x) if(x$valid) x$test_type else "N/A"),
    stringsAsFactors = FALSE
  )
  
  # Add F-statistic row
  f_row <- paste0("F-estadístico & ", 
                 paste(results_summary$F_stat, collapse = " & "), " \\\\\n")
  
  # Add p-value row
  p_row <- paste0("Valor p & ", 
                 paste(results_summary$p_value, collapse = " & "), " \\\\\n")
  
  # Add significance row
  sig_row <- paste0("Significativo & ", 
                   paste(results_summary$significant, collapse = " & "), " \\\\\n")
  
  # Create table footer
  latex_footer <- paste0(
    "\\hline\n",
    "\\end{tabular}\n",
    "\\begin{tablenotes}\n",
    "\\small\n",
    "\\item Nota: Se aplicó ANOVA estándar o Welch's ANOVA según homogeneidad de varianzas.\n",
    "\\item Significancia: p < 0.05. N/A: No aplicable por datos insuficientes.\n",
    "\\end{tablenotes}\n",
    "\\end{table}\n\n"
  )
  
  # Combine all parts
  full_table <- paste0(latex_header, f_row, p_row, sig_row, latex_footer)
  
  # Write to file
  cat(full_table, file = output_file, append = TRUE)
  
  return(full_table)
}

# Generate detailed descriptive statistics table
generate_descriptive_table <- function(var_name, var_results, output_file) {
  # Find the first valid result to get group structure
  valid_result <- NULL
  for(result in var_results) {
    if(result$valid) {
      valid_result <- result
      break
    }
  }
  
  if(is.null(valid_result)) {
    return("No valid results found")
  }
  
  # Create descriptive statistics table
  desc_header <- paste0(
    "\\begin{table}[H]\n",
    "\\centering\n",
    "\\caption{Estadísticas descriptivas para ", var_name, "}\n",
    "\\label{tab:desc", gsub("_", "", var_name), "}\n",
    "\\begin{tabular}{|l|c|c|c|c|c|}\n",
    "\\hline\n",
    "\\textbf{Grupo} & \\textbf{n} & \\textbf{Media} & \\textbf{DE} & \\textbf{Desarrollo adecuado (\\%)} & \\textbf{Riesgo alto (\\%)} \\\\\n",
    "\\hline\n"
  )
  
  # Generate rows for each group
  groups <- valid_result$descriptives$Group
  desc_rows <- ""
  
  for(group in groups) {
    group_data <- valid_result$descriptives[valid_result$descriptives$Group == group, ]
    desc_rows <- paste0(desc_rows,
                       group, " & ",
                       group_data$n, " & ",
                       round(group_data$mean, 2), " & ",
                       round(group_data$sd, 2), " & ",
                       group_data$pct_desarrollo_adecuado, " & ",
                       group_data$pct_riesgo_alto, " \\\\\n")
  }
  
  desc_footer <- paste0(
    "\\hline\n",
    "\\end{tabular}\n",
    "\\begin{tablenotes}\n",
    "\\small\n",
    "\\item Nota: DE = Desviación estándar. Desarrollo adecuado: Z > -1. Riesgo alto: Z < -2.\n",
    "\\end{tablenotes}\n",
    "\\end{table}\n\n"
  )
  
  full_desc_table <- paste0(desc_header, desc_rows, desc_footer)
  cat(full_desc_table, file = output_file, append = TRUE)
  
  return(full_desc_table)
}

# =============================================================================
# Main Analysis Execution
# =============================================================================

main_analysis <- function() {
  cat("Starting ANOVA analysis...\n")
  
  # Load data
  data <- load_and_clean_data("datos_optimizados.csv")
  
  # Initialize results storage
  all_results <- list()
  
  # Initialize LaTeX output file
  latex_file <- "resultados_anova.tex"
  cat("", file = latex_file)  # Clear file
  
  # Write LaTeX document header
  cat("\\documentclass{article}\n", file = latex_file, append = TRUE)
  cat("\\usepackage[utf8]{inputenc}\n", file = latex_file, append = TRUE)
  cat("\\usepackage[spanish]{babel}\n", file = latex_file, append = TRUE)
  cat("\\usepackage{float}\n", file = latex_file, append = TRUE)
  cat("\\usepackage{threeparttable}\n", file = latex_file, append = TRUE)
  cat("\\usepackage{booktabs}\n", file = latex_file, append = TRUE)
  cat("\\usepackage{geometry}\n", file = latex_file, append = TRUE)
  cat("\\geometry{margin=1in}\n", file = latex_file, append = TRUE)
  cat("\\title{Resultados Análisis ANOVA - Dominios de Desarrollo}\n", file = latex_file, append = TRUE)
  cat("\\author{Análisis Estadístico}\n", file = latex_file, append = TRUE)
  cat("\\date{\\today}\n", file = latex_file, append = TRUE)
  cat("\\begin{document}\n", file = latex_file, append = TRUE)
  cat("\\maketitle\n\n", file = latex_file, append = TRUE)
  
  # Add introduction
  cat("\\section{Introducción}\n", file = latex_file, append = TRUE)
  cat("Este documento presenta los resultados del análisis ANOVA para evaluar las diferencias en los cinco dominios del desarrollo (comunicación, motricidad gruesa, motricidad fina, resolución de problemas y socio-individual) según diversas variables sociodemográficas, ambientales y clínicas.\n\n", file = latex_file, append = TRUE)
  
  # Process each independent variable
  for(var in independent_vars) {
    cat("\nProcessing variable:", var, "\n")
    
    # Check if variable exists in data
    if(!(var %in% names(data))) {
      # Check for categorical version
      var_cat <- paste0(var, "_cat")
      if(var_cat %in% names(data)) {
        var <- var_cat
      } else {
        cat("Warning: Variable", var, "not found in data\n")
        next
      }
    }
    
    # Initialize results for this variable
    var_results <- list()
    
    # Analyze each z-score domain
    for(domain in zscore_domains) {
      cat("  Analyzing", domain, "...\n")
      
      result <- perform_anova_analysis(data, var, domain)
      var_results[[domain]] <- result
      
      if(result$valid) {
        cat("    ", result$test_type, ": F =", round(result$test_statistic, 3), 
            ", p =", round(result$p_value, 4), 
            ifelse(result$significant, "(significant)", "(not significant)"), "\n")
      } else {
        cat("    Analysis failed:", result$reason, "\n")
      }
    }
    
    # Store results
    all_results[[var]] <- var_results
    
    # Generate LaTeX table
    cat("\\section{", var, "}\n", file = latex_file, append = TRUE)
    generate_latex_table(var, var_results, latex_file)
    generate_descriptive_table(var, var_results, latex_file)
    cat("\\newpage\n", file = latex_file, append = TRUE)
  }
  
  # Close LaTeX document
  cat("\\end{document}\n", file = latex_file, append = TRUE)
  
  cat("\nAnalysis complete! Results saved to:", latex_file, "\n")
  
  # Save detailed results
  save(all_results, file = "anova_results.RData")
  
  # Generate summary report
  generate_summary_report(all_results)
  
  return(all_results)
}

# Generate summary report
generate_summary_report <- function(all_results) {
  cat("Generating summary report...\n")
  
  summary_file <- "anova_summary.txt"
  cat("ANOVA Analysis Summary Report\n", file = summary_file)
  cat("=============================\n\n", file = summary_file, append = TRUE)
  
  total_tests <- 0
  significant_tests <- 0
  
  for(var_name in names(all_results)) {
    var_results <- all_results[[var_name]]
    
    cat("Variable:", var_name, "\n", file = summary_file, append = TRUE)
    cat("-------------------------------------------\n", file = summary_file, append = TRUE)
    
    for(domain in names(var_results)) {
      result <- var_results[[domain]]
      
      if(result$valid) {
        total_tests <- total_tests + 1
        if(result$significant) {
          significant_tests <- significant_tests + 1
        }
        
        cat("  ", domain, ":\n", file = summary_file, append = TRUE)
        cat("    Test:", result$test_type, "\n", file = summary_file, append = TRUE)
        cat("    F-statistic:", round(result$test_statistic, 3), "\n", file = summary_file, append = TRUE)
        cat("    P-value:", round(result$p_value, 4), "\n", file = summary_file, append = TRUE)
        cat("    Significant:", ifelse(result$significant, "Yes", "No"), "\n", file = summary_file, append = TRUE)
        cat("    Sample size:", result$n_total, "\n", file = summary_file, append = TRUE)
        cat("    Groups:", result$n_groups, "\n", file = summary_file, append = TRUE)
        cat("\n", file = summary_file, append = TRUE)
      } else {
        cat("  ", domain, ": FAILED -", result$reason, "\n", file = summary_file, append = TRUE)
      }
    }
    
    cat("\n", file = summary_file, append = TRUE)
  }
  
  cat("OVERALL SUMMARY\n", file = summary_file, append = TRUE)
  cat("===============\n", file = summary_file, append = TRUE)
  cat("Total tests performed:", total_tests, "\n", file = summary_file, append = TRUE)
  cat("Significant results:", significant_tests, "\n", file = summary_file, append = TRUE)
  cat("Percentage significant:", round(significant_tests/total_tests*100, 1), "%\n", file = summary_file, append = TRUE)
  
  cat("Summary report saved to:", summary_file, "\n")
}

# =============================================================================
# Execute Analysis
# =============================================================================

if(!interactive()) {
  # Run analysis when script is executed
  results <- main_analysis()
  cat("ANOVA analysis completed successfully!\n")
}