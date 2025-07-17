# Análisis ANOVA de Dominios de Desarrollo

Este repositorio contiene el análisis estadístico de cinco dominios del desarrollo neurológico en relación con variables sociodemográficas, ambientales y clínicas.

## Estructura del Proyecto

- `datos_optimizados.csv`: Dataset principal con 1,725 observaciones
- `anova_analysis_base.R`: Script principal de análisis ANOVA
- `resultados_anova.tex`: Tablas LaTeX con resultados del análisis
- `anova_summary.txt`: Resumen ejecutivo de los resultados
- `anova_results.RData`: Datos completos del análisis en formato R

## Dominios de Desarrollo Analizados

El análisis evalúa cinco dominios del desarrollo neurológico:

1. **Comunicación** (`zscore_desarrollo_comunicacion`)
2. **Motricidad gruesa** (`zscore_desarrollo_motricidad_gruesa`)
3. **Motricidad fina** (`zscore_desarrollo_motricidad_fina`)
4. **Resolución de problemas** (`zscore_desarrollo_resolucion_problemas`)
5. **Socio-individual** (`zscore_desarrollo_socio_individual`)

## Variables Independientes

El análisis incluye variables sociodemográficas, ambientales y clínicas:

- **Demográficas**: edad del niño, edad de padres, grupo étnico, área de residencia
- **Educativas**: nivel educativo de madre y padre
- **Ambientales**: fuente de agua, tipo de sanitario, manejo de basura, energía
- **Socioeconómicas**: propiedad de vivienda, situación laboral, seguro social
- **Familiares**: composición del hogar, estado civil, horas de pantalla
- **Prenatales**: controles prenatales, ultrasonidos, tipo de parto
- **Nutricionales**: lactancia, vitaminas, estado nutricional
- **Clínicas**: hospitalizaciones, vacunación, condiciones de salud

## Metodología

### Análisis Estadístico

1. **Preparación de datos**: 
   - Limpieza y transformación de variables
   - Conversión de variables continuas a categóricas
   - Manejo de valores perdidos

2. **Verificación de supuestos**:
   - Normalidad (prueba de Shapiro-Wilk)
   - Homogeneidad de varianzas (análisis de ratios de varianza)

3. **Análisis ANOVA**:
   - ANOVA estándar cuando se cumplen los supuestos
   - ANOVA de Welch cuando hay heterogeneidad de varianzas
   - Pruebas post-hoc para diferencias específicas entre grupos

4. **Clasificación de desarrollo**:
   - **Desarrollo adecuado**: Z > -1
   - **Riesgo de trastornos**: -2 ≤ Z ≤ -1
   - **Riesgo alto**: Z < -2

## Resultados Principales

Del análisis de 152 pruebas ANOVA realizadas:

- **50 resultados significativos** (32.9% del total)
- **Edad del niño**: Significativo para todos los dominios
- **Área de residencia**: Significativo para 4 de 5 dominios
- **Nivel educativo materno**: Significativo para todos los dominios
- **Variables nutricionales y clínicas**: Múltiples asociaciones significativas

## Uso del Código

### Requisitos

- R versión 4.0 o superior
- Paquetes base de R (no requiere instalaciones adicionales)

### Ejecución

```bash
# Ejecutar el análisis completo
Rscript anova_analysis_base.R
```

### Archivos de Salida

1. **`resultados_anova.tex`**: Tablas LaTeX listas para publicación
2. **`anova_summary.txt`**: Resumen ejecutivo con estadísticas clave
3. **`anova_results.RData`**: Datos completos para análisis adicionales

## Interpretación de Resultados

### Tablas LaTeX

Las tablas incluyen:
- F-estadístico o W-estadístico (Welch)
- Valor p
- Significancia estadística
- Estadísticas descriptivas por grupo

### Significancia Clínica

Los resultados sugieren que:
- La edad del niño es el factor más determinante del desarrollo
- Las variables socioeconómicas (educación, residencia) tienen impacto significativo
- Los factores prenatales y nutricionales muestran asociaciones importantes

## Limitaciones

- Variables continuas fueron categorizadas para el análisis
- Algunos análisis fallaron por datos insuficientes
- No se ajustó por comparaciones múltiples entre dominios

## Autor

Análisis generado para el proyecto data-tesis

## Fecha

Julio 2024