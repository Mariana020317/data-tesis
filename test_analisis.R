# Test script para validar la funcionalidad básica
# ===============================================

# Cargar datos
datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)

# Mostrar estructura de los datos
cat("Estructura de los datos:\n")
str(datos)

# Verificar las variables de desarrollo
cat("\nVariables de desarrollo disponibles:\n")
desarrollo_vars <- names(datos)[grepl("zscore_desarrollo", names(datos))]
print(desarrollo_vars)

# Crear variables dicotómicas de riesgo (z-score < -1)
dominios <- c(
  "comunicacion" = "zscore_desarrollo_comunicacion",
  "motricidad_gruesa" = "zscore_desarrollo_motricidad_gruesa", 
  "motricidad_fina" = "zscore_desarrollo_motricidad_fina",
  "resolucion_problemas" = "zscore_desarrollo_resolucion_problemas",
  "socio_individual" = "zscore_desarrollo_socio_individual"
)

for(dominio in dominios) {
  nueva_var <- paste0("riesgo_", names(dominios)[dominios == dominio])
  datos[[nueva_var]] <- ifelse(datos[[dominio]] < -1, "Riesgo", "Desarrollo adecuado")
}

cat("\nVariables de riesgo creadas:\n")
riesgo_vars <- names(datos)[grepl("riesgo_", names(datos))]
print(riesgo_vars)

# Probar análisis con una variable
variable_test <- "area_residencia"
dominio_test <- "riesgo_comunicacion"

if(variable_test %in% names(datos) && dominio_test %in% names(datos)) {
  cat("\nProbando análisis con", variable_test, "y", dominio_test, ":\n")
  
  # Tabla de contingencia
  tabla <- table(datos[[variable_test]], datos[[dominio_test]])
  print("Tabla de contingencia:")
  print(tabla)
  
  # Chi-cuadrado
  if(all(tabla >= 5)) {
    chi_result <- chisq.test(tabla)
    cat("\nChi-cuadrado:\n")
    cat("X² =", chi_result$statistic, ", df =", chi_result$parameter, ", p =", chi_result$p.value, "\n")
  } else {
    cat("\nUsando test exacto de Fisher (celdas < 5):\n")
    fisher_result <- fisher.test(tabla)
    cat("p =", fisher_result$p.value, "\n")
  }
  
  # Odds Ratio (si es tabla 2x2)
  if(nrow(tabla) == 2 && ncol(tabla) == 2) {
    or <- (tabla[1,1] * tabla[2,2]) / (tabla[1,2] * tabla[2,1])
    log_or <- log(or)
    se_log_or <- sqrt(sum(1/tabla))
    ic_inf <- exp(log_or - 1.96 * se_log_or)
    ic_sup <- exp(log_or + 1.96 * se_log_or)
    
    cat("\nOdds Ratio:\n")
    cat("OR =", or, "(IC 95%:", ic_inf, "-", ic_sup, ")\n")
  }
}

# Verificar algunas variables específicas
variables_test <- c("grupo_etnico", "nivel_educativo_madre", "seguro_social")

cat("\nVerificando variables específicas:\n")
for(var in variables_test) {
  if(var %in% names(datos)) {
    cat(var, "- Presente\n")
    cat("  Valores únicos:", length(unique(datos[[var]])), "\n")
    print(table(datos[[var]], useNA = "ifany"))
  } else {
    cat(var, "- NO ENCONTRADA\n")
  }
  cat("\n")
}