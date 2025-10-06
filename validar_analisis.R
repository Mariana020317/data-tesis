# Script de validación para el análisis chi-cuadrado mejorado

source("analisis_chi_cuadrado_mejorado.R")

# Cargar datos
datos <- read.csv("datos_optimizados.csv", stringsAsFactors = FALSE)

# Categorizar z-scores
datos$riesgo_comunicacion <- categorizar_riesgo(datos$zscore_desarrollo_comunicacion)
datos$riesgo_motricidad_gruesa <- categorizar_riesgo(datos$zscore_desarrollo_motricidad_gruesa)

cat("=== VALIDACIÓN DEL ANÁLISIS CHI-CUADRADO MEJORADO ===\n\n")

# Test 1: Verificar que la función maneja correctamente casos sin significancia
cat("1. Probando caso sin significancia estadística...\n")
resultado1 <- analizar_chi_cuadrado_mejorado(datos, "sexo_nino", "riesgo_comunicacion")
cat(resultado1)
cat("\n" , rep("=", 50), "\n\n")

# Test 2: Verificar que identifica correctamente significancia práctica
cat("2. Probando caso con significancia estadística y práctica...\n")
resultado2 <- analizar_chi_cuadrado_mejorado(datos, "grupo_etnico", "riesgo_motricidad_gruesa")
cat(resultado2)
cat("\n", rep("=", 50), "\n\n")

# Test 3: Verificar manejo de muestras pequeñas
cat("3. Probando caso con muestras pequeñas (Fisher test)...\n")
resultado3 <- analizar_chi_cuadrado_mejorado(datos, "area_residencia", "riesgo_comunicacion")
cat(resultado3)
cat("\n", rep("=", 50), "\n\n")

# Test 4: Verificar intervalos de confianza
cat("4. Validando cálculo de intervalos de confianza...\n")
ic_test <- calcular_ic_proporcion(50, 100, 0.95)
cat(sprintf("IC para 50/100: %.3f - %.3f (esperado: ~0.401 - 0.599)\n", ic_test$lower, ic_test$upper))

ic_test2 <- calcular_ic_proporcion(5, 100, 0.95)
cat(sprintf("IC para 5/100: %.3f - %.3f (esperado: ~0.021 - 0.096)\n", ic_test2$lower, ic_test2$upper))

# Test 5: Verificar categorización de riesgo
cat("\n5. Validando categorización de z-scores...\n")
test_zscores <- c(-2.5, -1.5, -0.5, 0.5, NA)
categorias <- categorizar_riesgo(test_zscores)
expected <- c("Alto riesgo", "Riesgo de trastorno", "Sin riesgo", "Sin riesgo", NA)
cat("Z-scores: ", paste(test_zscores, collapse=", "), "\n")
cat("Categorías: ", paste(categorias, collapse=", "), "\n")
cat("Esperado: ", paste(expected, collapse=", "), "\n")
cat("Correcto: ", all(categorias == expected, na.rm=TRUE), "\n\n")

# Test 6: Verificar resumen estadístico
cat("6. Resumen de distribución de riesgo por dominio:\n")
for (dominio in c("riesgo_comunicacion", "riesgo_motricidad_gruesa")) {
  tabla <- table(datos[[dominio]], useNA="ifany")
  cat(sprintf("%s: %s\n", dominio, paste(names(tabla), "=", tabla, collapse=", ")))
}

cat("\n=== VALIDACIÓN COMPLETADA ===\n")