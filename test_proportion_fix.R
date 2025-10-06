# Test script para verificar las correcciones en proporciones y OR
# =====================================================================

# Cargar datos
datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)

# Crear variable dicotómica de riesgo para comunicación
datos$riesgo_comunicacion <- ifelse(datos$zscore_desarrollo_comunicacion < -1, "Riesgo", "Desarrollo adecuado")

# Función para calcular Odds Ratio CORREGIDA
calcular_odds_ratio <- function(variable, dominio_riesgo, datos) {
  # Crear tabla 2x2 para OR
  tabla <- table(datos[[variable]], datos[[dominio_riesgo]])
  
  if(nrow(tabla) == 2 && ncol(tabla) == 2) {
    # Calcular OR correctamente
    or <- (tabla[1,"Riesgo"] * tabla[2,"Desarrollo adecuado"]) / (tabla[1,"Desarrollo adecuado"] * tabla[2,"Riesgo"])
    
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

# Test con grupo_etnico
cat("=== PRUEBA CON GRUPO_ETNICO ===\n\n")

# Tabla de contingencia
tabla <- table(datos$grupo_etnico, datos$riesgo_comunicacion)
print("Tabla de contingencia:")
print(addmargins(tabla))

# Proporciones CORREGIDAS
props <- prop.table(tabla, 1) * 100
cat("\nProporciones CORREGIDAS:\n")
for(i in 1:nrow(props)) {
  cat("-", rownames(props)[i], ":", 
      sprintf("%.1f%% desarrollo adecuado vs %.1f%% riesgo", 
             props[i,"Desarrollo adecuado"], props[i,"Riesgo"]), "\n")
}

# OR CORREGIDO
resultado_or <- calcular_odds_ratio("grupo_etnico", "riesgo_comunicacion", datos)
cat("\nOdds Ratio CORREGIDO:\n")
if(!is.na(resultado_or$or)) {
  cat("OR =", sprintf("%.2f", resultado_or$or), 
      "(IC 95%:", sprintf("%.2f", resultado_or$ic_inf), 
      "-", sprintf("%.2f", resultado_or$ic_sup), ")\n")
  
  # Interpretación
  if(resultado_or$or > 1) {
    cat("Interpretación: El primer grupo tiene", sprintf("%.2f", resultado_or$or), "veces más probabilidad de riesgo\n")
  } else {
    cat("Interpretación: El primer grupo tiene", sprintf("%.2f", 1/resultado_or$or), "veces menos probabilidad de riesgo\n")
  }
} else {
  cat("No se pudo calcular OR\n")
}

cat("\n=== VERIFICACIÓN MANUAL ===\n")
cat("Cálculo manual del OR:\n")
cat("Indígena con riesgo:", tabla["Indígena", "Riesgo"], "\n")
cat("Indígena con desarrollo adecuado:", tabla["Indígena", "Desarrollo adecuado"], "\n")
cat("No indígena con riesgo:", tabla["No indígena", "Riesgo"], "\n")
cat("No indígena con desarrollo adecuado:", tabla["No indígena", "Desarrollo adecuado"], "\n")

# Cálculo manual
a <- tabla["Indígena", "Riesgo"]
b <- tabla["Indígena", "Desarrollo adecuado"]
c <- tabla["No indígena", "Riesgo"]
d <- tabla["No indígena", "Desarrollo adecuado"]

or_manual <- (a * d) / (b * c)
cat("OR manual = (", a, " * ", d, ") / (", b, " * ", c, ") = ", or_manual, "\n")

cat("\n=== FINALIZADO ===\n")