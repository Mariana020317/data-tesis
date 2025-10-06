# Análisis Chi-Cuadrado Mejorado para Desarrollo Infantil

## Descripción

Este script implementa un análisis chi-cuadrado mejorado que corrige problemas comunes en la interpretación de resultados estadísticamente significativos, especialmente cuando los conteos absolutos son pequeños y las diferencias porcentuales son mínimas.

## Características principales

### 1. Validación de significancia práctica
- Implementa un umbral mínimo de 2% para diferencias porcentuales
- Solo interpreta diferencias como "mayor riesgo" cuando son tanto estadística como prácticamente significativas
- Evita interpretaciones engañosas basadas en diferencias mínimas

### 2. Intervalos de confianza
- Calcula intervalos de confianza del 95% para todas las proporciones
- Utiliza el método de Wilson para mayor precisión
- Proporciona información sobre la precisión de las estimaciones

### 3. Test estadístico apropiado
- Utiliza automáticamente el test exacto de Fisher cuando los conteos son pequeños (< 5)
- Aplica chi-cuadrado cuando es apropiado
- Informa sobre las limitaciones del análisis

### 4. Interpretación mejorada
- Identifica específicamente qué categoría de riesgo impulsa la significancia estadística
- Proporciona diferencias porcentuales exactas
- Incluye limitaciones y precauciones cuando es necesario

## Uso

### Ejecutar el análisis completo:
```bash
Rscript analisis_chi_cuadrado_mejorado.R
```

### Usar funciones específicas:
```r
# Cargar el script
source("analisis_chi_cuadrado_mejorado.R")

# Ejecutar análisis completo
resultado <- realizar_analisis_completo("datos_optimizados.csv")

# Analizar una combinación específica
resultado <- analizar_chi_cuadrado_mejorado(datos, "grupo_etnico", "riesgo_comunicacion")
```

## Configuración

### Parámetros modificables:
- `min_diff_porcentaje`: Umbral mínimo para diferencias prácticamente significativas (default: 2%)
- `conf.level`: Nivel de confianza para intervalos (default: 0.95)

### Variables analizadas:
- **Variables independientes**: grupo_etnico, area_residencia, nivel_educativo_madre, nivel_educativo_padre, situacion_laboral_madre, situacion_laboral_padre, seguro_social, sexo_nino
- **Variables dependientes**: riesgo_comunicacion, riesgo_motricidad_gruesa, riesgo_motricidad_fina, riesgo_resolucion_problemas, riesgo_socio_individual

## Categorización de riesgo

Los z-scores de desarrollo se categorizan como:
- **Sin riesgo**: z-score ≥ -1
- **Riesgo de trastorno**: -2 ≤ z-score < -1
- **Alto riesgo**: z-score < -2

## Interpretación de resultados

### Formato de salida:
```
**Interpretación:**
La asociación entre [variable] y [dominio] ES/NO ES ESTADÍSTICAMENTE SIGNIFICATIVA (χ² = X.XX, p = X.XXX).

**Análisis detallado:**
La significancia estadística se debe principalmente a que [categoría] muestra mayor proporción de [nivel de riesgo] (X.X% vs Y.Y%, diferencia de Z.Z%)

**Intervalos de confianza 95%:**
[Categoría] - [Nivel]: X.X% (IC 95%: Y.Y% - Z.Z%)

**Limitaciones:**
- [Limitaciones específicas del análisis]
```

### Criterios de interpretación:
1. **Significancia estadística**: p < 0.05
2. **Significancia práctica**: Diferencia ≥ 2% entre proporciones
3. **Ambas condiciones**: Requeridas para interpretación como "mayor riesgo"

## Archivos de salida

- `analisis_chi_cuadrado_mejorado_resultados.txt`: Resultados completos del análisis
- Incluye tablas de contingencia, proporciones, interpretaciones y limitaciones
- Formato estructurado para fácil lectura y análisis

## Validaciones implementadas

1. **Manejo de datos faltantes**: Excluye valores NA y cadenas vacías
2. **Verificación de tamaño muestral**: Requiere mínimo 10 observaciones
3. **Selección de test apropiado**: Fisher vs. chi-cuadrado según conteos
4. **Advertencias sobre limitaciones**: Conteos pequeños, relevancia clínica

## Beneficios sobre análisis tradicional

- Reduce interpretaciones erróneas de diferencias mínimas
- Proporciona contexto clínico a la significancia estadística
- Incluye medidas de precisión (intervalos de confianza)
- Identifica claramente las categorías que impulsan los resultados
- Formato consistente y profesional para reportes

## Requisitos

- R (versión 4.0 o superior)
- Funciones base de R (sin dependencias externas)
- Archivo CSV con datos en formato apropiado