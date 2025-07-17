#!/usr/bin/env Rscript

# Diagnosis Script for Statistical Analysis Setup
# ==============================================

cat("=== DIAGNOSTIC SCRIPT FOR STATISTICAL ANALYSIS ===\n")
cat("This script will help identify setup issues.\n\n")

# 1. Check R version
cat("1. R Version Check:\n")
cat("R version:", R.version.string, "\n")
cat("Platform:", R.version$platform, "\n\n")

# 2. Check working directory
cat("2. Working Directory Check:\n")
cat("Current directory:", getwd(), "\n")
cat("Directory contents:\n")
print(list.files(pattern = "*\\.(R|csv|txt|md)$"))
cat("\n")

# 3. Check data file
cat("3. Data File Check:\n")
if(file.exists("datos_optimizados.csv")) {
  cat("✓ datos_optimizados.csv found\n")
  
  # Check file size
  file_info <- file.info("datos_optimizados.csv")
  cat("File size:", file_info$size, "bytes\n")
  
  # Try to read the file
  tryCatch({
    datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)
    cat("✓ File successfully loaded\n")
    cat("Rows:", nrow(datos), ", Columns:", ncol(datos), "\n")
    
    # Check for required columns
    required_cols <- c(
      "zscore_desarrollo_comunicacion",
      "zscore_desarrollo_motricidad_gruesa",
      "zscore_desarrollo_motricidad_fina",
      "zscore_desarrollo_resolucion_problemas",
      "zscore_desarrollo_socio_individual"
    )
    
    missing_cols <- required_cols[!required_cols %in% names(datos)]
    if(length(missing_cols) == 0) {
      cat("✓ All required development columns found\n")
    } else {
      cat("✗ Missing required columns:\n")
      for(col in missing_cols) {
        cat("  -", col, "\n")
      }
    }
    
    # Check sample variables
    sample_vars <- c("area_residencia", "grupo_etnico", "nivel_educativo_madre")
    available_vars <- sample_vars[sample_vars %in% names(datos)]
    cat("Sample variables available:", length(available_vars), "of", length(sample_vars), "\n")
    
    # Show first few rows
    cat("\nFirst 3 rows of key columns:\n")
    key_cols <- c("area_residencia", "grupo_etnico", "zscore_desarrollo_comunicacion")
    available_key_cols <- key_cols[key_cols %in% names(datos)]
    if(length(available_key_cols) > 0) {
      print(datos[1:min(3, nrow(datos)), available_key_cols])
    }
    
  }, error = function(e) {
    cat("✗ Error reading data file:\n")
    cat("Error message:", e$message, "\n")
  })
  
} else {
  cat("✗ datos_optimizados.csv NOT FOUND\n")
  cat("Please ensure the data file is in the current directory.\n")
}

cat("\n")

# 4. Check R scripts
cat("4. R Scripts Check:\n")
scripts <- c("analisis_demo.R", "analisis_reorganizado.R", "test_analisis.R")
for(script in scripts) {
  if(file.exists(script)) {
    cat("✓", script, "found\n")
    # Check if script is readable
    tryCatch({
      lines <- readLines(script, n = 5)
      cat("  First line:", substr(lines[1], 1, 50), "...\n")
    }, error = function(e) {
      cat("  ✗ Error reading script:", e$message, "\n")
    })
  } else {
    cat("✗", script, "NOT FOUND\n")
  }
}

cat("\n")

# 5. Test basic functionality
cat("5. Basic Functionality Test:\n")
if(file.exists("datos_optimizados.csv")) {
  tryCatch({
    datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)
    
    # Test table creation
    if("area_residencia" %in% names(datos)) {
      cat("✓ Testing table creation...\n")
      test_table <- table(datos$area_residencia, useNA = "ifany")
      cat("  area_residencia levels:", names(test_table), "\n")
      
      # Test z-score processing
      if("zscore_desarrollo_comunicacion" %in% names(datos)) {
        cat("✓ Testing z-score processing...\n")
        risk_var <- ifelse(datos$zscore_desarrollo_comunicacion < -1, "Riesgo", "Desarrollo adecuado")
        risk_table <- table(risk_var, useNA = "ifany")
        cat("  Risk distribution:", names(risk_table), "->", as.numeric(risk_table), "\n")
        
        # Test Chi-square
        if("area_residencia" %in% names(datos)) {
          cat("✓ Testing Chi-square analysis...\n")
          test_chi_table <- table(datos$area_residencia, risk_var)
          if(all(test_chi_table >= 5)) {
            chi_result <- chisq.test(test_chi_table)
            cat("  Chi-square test successful: p =", chi_result$p.value, "\n")
          } else {
            cat("  Using Fisher's exact test (small cells)\n")
            fisher_result <- fisher.test(test_chi_table)
            cat("  Fisher test successful: p =", fisher_result$p.value, "\n")
          }
        }
      }
    }
    
    cat("✓ All basic functionality tests passed\n")
    
  }, error = function(e) {
    cat("✗ Basic functionality test failed:\n")
    cat("Error message:", e$message, "\n")
  })
} else {
  cat("✗ Cannot run functionality test - data file missing\n")
}

cat("\n")

# 6. System information
cat("6. System Information:\n")
cat("OS:", Sys.info()["sysname"], "\n")
cat("R installation path:", R.home(), "\n")
cat("Current time:", Sys.time(), "\n")

cat("\n=== DIAGNOSIS COMPLETE ===\n")

# 7. Recommendations
cat("\n7. Recommendations:\n")
if(!file.exists("datos_optimizados.csv")) {
  cat("⚠ CRITICAL: Missing data file 'datos_optimizados.csv'\n")
  cat("  → Place the CSV file in the current directory\n")
}

missing_scripts <- scripts[!file.exists(scripts)]
if(length(missing_scripts) > 0) {
  cat("⚠ Missing scripts:\n")
  for(script in missing_scripts) {
    cat("  →", script, "\n")
  }
}

cat("\nIf all checks passed, you can run the analysis with:\n")
cat("  R --vanilla < analisis_demo.R > resultados_demo.txt\n")
cat("\nFor help, see SETUP_GUIDE.md\n")