# Análisis ANOVA de Desarrollo Infantil

Este proyecto implementa un análisis estadístico integral mediante ANOVA de una vía para evaluar las asociaciones entre variables sociodemográficas, ambientales y clínicas con cinco dominios del desarrollo infantil.

## 📊 Descripción del Análisis

El análisis evalúa **240 combinaciones** de variables independientes con cinco dominios del desarrollo infantil usando puntajes Z:

- **Comunicación** (zscore_desarrollo_comunicacion)
- **Motricidad gruesa** (zscore_desarrollo_motricidad_gruesa)  
- **Motricidad fina** (zscore_desarrollo_motricidad_fina)
- **Resolución de problemas** (zscore_desarrollo_resolucion_problemas)
- **Socio-individual** (zscore_desarrollo_socio_individual)

## 🔬 Metodología Estadística

### Clasificación de Riesgo
- **Desarrollo normal**: Z > -1
- **Riesgo de trastornos del desarrollo**: Z ≤ -1

### Preparación de Variables
- **Variables de edad**: Convertidas a intervalos categóricos apropiados
  - Edad del niño: 0-6, 7-12, 13-18, 19-24, 25-36, 37-48, 49-60 meses
  - Edad de la madre: ≤20, 21-25, 26-30, 31-35, >35 años
  - Edad del padre: ≤25, 26-30, 31-35, 36-40, >40 años

### Proceso de Análisis
1. **Verificación de supuestos**: Normalidad (Shapiro-Wilk) y homocedasticidad (Levene)
2. **Selección de prueba**: ANOVA estándar o ANOVA de Welch según corresponda
3. **Análisis post-hoc**: Identificación de grupos afectados para resultados significativos
4. **Estadísticas descriptivas**: Media, desviación estándar, clasificación de riesgo por grupo

## 📁 Archivos del Proyecto

### `anova_analysis.py` - Script Principal (Python)
- **Dependencias**: pandas, numpy, scipy, pingouin
- **Entrada**: `datos_optimizados.csv` (1,725 observaciones, 57 variables)
- **Salida**: Tablas LaTeX, resumen ejecutivo, resultados en CSV

### `resultados_anova.tex` - Tablas LaTeX
- **Formato**: Documento LaTeX profesional con explicaciones detalladas
- **Contenido**: Tablas comprensivas para todas las combinaciones variable-dominio
- **Idioma**: Español, listo para publicación
- **Características**: Estadísticos F/W, p-valores, indicadores de significancia, estadísticas descriptivas

### `anova_summary.txt` - Resumen Ejecutivo
- **Contenido**: Resumen estadístico completo de todos los análisis
- **Formato**: Texto legible con detalles de cada prueba significativa

### `anova_results.csv` - Resultados Completos
- **Formato**: CSV con todos los resultados para análisis posterior
- **Contenido**: Estadísticos, p-valores, clasificaciones de riesgo, metadatos

## 🚀 Uso

### Ejecución del Análisis
```bash
# Instalar dependencias
pip install pandas numpy scipy pingouin

# Ejecutar análisis completo
python3 anova_analysis.py
```

### Archivos Generados
- `resultados_anova.tex`: Tablas LaTeX listas para publicación
- `anova_summary.txt`: Resumen ejecutivo del análisis
- `anova_results.csv`: Resultados completos en formato CSV

## 📈 Resultados Principales

### Estadísticas Generales
- **Total de pruebas ANOVA**: 235
- **Resultados significativos**: 74 (31.5%)
- **Muestra analizada**: 1,725 niños
- **Variables independientes**: 48 variables

### Variables con Mayor Impacto
Las variables con mayor número de asociaciones significativas incluyen:
- Edad del niño (todos los dominios)
- Nivel educativo de la madre
- Área de residencia
- Factores nutricionales y clínicos

### Interpretación de Resultados
Cada resultado significativo incluye:
- **Identificación del grupo afectado**: Grupo con mayor riesgo de desarrollo
- **Estadísticas descriptivas**: Medias, desviaciones estándar, porcentajes de riesgo
- **Interpretación clínica**: Explicación del impacto en el desarrollo infantil

## 🔍 Características Técnicas

### Gestión de Supuestos ANOVA
- **Normalidad**: Prueba de Shapiro-Wilk por grupo
- **Homocedasticidad**: Prueba de Levene
- **Selección automática**: ANOVA estándar vs. ANOVA de Welch

### Análisis Post-hoc
- **Comparaciones múltiples**: Pruebas t con corrección de Bonferroni
- **Identificación de grupos**: Automática para resultados significativos
- **Interpretación**: Explicaciones detalladas en español

### Robustez del Análisis
- **Manejo de valores faltantes**: Eliminación por lista para cada análisis
- **Tamaño mínimo de muestra**: 10 observaciones por análisis
- **Validación de grupos**: Mínimo 3 observaciones por grupo

## 📚 Aplicaciones

### Investigación Clínica
- Identificación de factores de riesgo para alteraciones del desarrollo
- Evaluación de intervenciones preventivas
- Diseño de estrategias de tamizaje

### Salud Pública
- Formulación de políticas basadas en evidencia
- Priorización de recursos para grupos vulnerables
- Monitoreo de indicadores de desarrollo infantil

### Práctica Clínica
- Identificación temprana de riesgos
- Orientación para derivaciones especializadas
- Seguimiento de casos en riesgo

## ✅ Validación

El análisis implementa:
- ✅ Verificación rigurosa de supuestos estadísticos
- ✅ Selección automática de pruebas apropiadas
- ✅ Análisis post-hoc para resultados significativos
- ✅ Clasificación de riesgo según criterios clínicos
- ✅ Documentación completa en español
- ✅ Tablas LaTeX listas para publicación

## 📞 Soporte Técnico

Para dudas sobre implementación o interpretación de resultados, consulte:
- Documentación técnica en `ANALYSIS_SUMMARY.md`
- Código fuente comentado en `anova_analysis.py`
- Resultados detallados en `anova_summary.txt`

---

**Nota**: Este análisis proporciona evidencia estadística sobre factores asociados con el desarrollo infantil. Los resultados deben interpretarse en el contexto clínico apropiado y considerando las limitaciones del diseño de estudio.