# Análisis Completo de Chi-Cuadrado: Variables Categóricas vs Neurodesarrollo

## Descripción del Proyecto

Este análisis implementa un estudio exhaustivo de asociaciones entre 48 variables categóricas y 5 dominios del neurodesarrollo utilizando pruebas de chi-cuadrado y test exacto de Fisher cuando es apropiado.

## Archivos Generados

### 📊 Análisis Principal
- **`analisis_chi_cuadrado_completo.txt`** (785 KB): Análisis detallado de las 240 combinaciones posibles con interpretaciones clínicas en español
- **`resumen_hallazgos_significativos.txt`**: Resumen ejecutivo con hallazgos clave y recomendaciones

### 📈 Visualizaciones
- **`hallazgos_neurodesarrollo.png/pdf`**: Gráficos principales mostrando distribuciones de riesgo
- **`correlaciones_dominios.png/pdf`**: Matriz de correlaciones entre dominios del neurodesarrollo

### 📋 Tablas Resumen
- **`estadisticas_resumen_dominios.csv/txt`**: Estadísticas descriptivas por dominio del neurodesarrollo

### 💻 Código Fuente
- **`analisis_chi_cuadrado_completo.py`**: Script principal del análisis
- **`generar_resumen_hallazgos.py`**: Generador de resumen ejecutivo
- **`crear_visualizaciones.py`**: Script para generar visualizaciones

## Metodología

### Variables Analizadas

#### Variables Categóricas (48 variables):
- **Demográficas**: edad_meses_nino, edad_anos_madre, edad_anos_padre, grupo_etnico, area_residencia
- **Educativas**: nivel_educativo_madre, nivel_educativo_padre
- **Socioeconómicas**: fuente_agua_consumo, tipo_sanitario, manejo_basura, tipo_energia_luz, tipo_energia_cocina, propiedad_vivienda
- **Familiares**: sexo_jefe_hogar, situacion_laboral_madre, situacion_laboral_padre, tipo_empleo_madre, tipo_empleo_padre
- **Salud**: seguro_social, total_personas_hogar, total_hermanos, posicion_nino_hermanos, estado_civil_cuidador
- **Desarrollo**: horas_pantalla, horas_juego_cuidador
- **Prenatales**: numero_controles_prenatales, ultrasonido_embarazo, prenatales_primeros_3_meses, prenatales_resto_embarazo
- **Parto**: servicio_asistencia_parto, tipo_parto, razon_cesarea_emergencia
- **Lactancia**: lactancia_primeros_6_meses, lactancia_6-12_meses, lactancia_12-24_meses
- **Suplementación**: vitamina_a_6-12_meses, vitamina_a_12-18_meses, vitamina_a_18-24_meses, vitaminas_minerales_6-12_meses, vitaminas_minerales_12-18_meses, vitaminas_minerales_18-24_meses
- **Estado nutricional**: retardo_crecimiento, desnutricion_aguda
- **Hospitalización**: hospitalizado_neonatal, razon_hospitalizado_neonatal, hospitalizado_infancia, razon_hospitalizado_infancia
- **Prevención**: vacunacion_completa

#### Dominios del Neurodesarrollo (5 dominios):
1. **Comunicación**: zscore_desarrollo_comunicacion
2. **Motricidad Gruesa**: zscore_desarrollo_motricidad_gruesa
3. **Motricidad Fina**: zscore_desarrollo_motricidad_fina
4. **Resolución de Problemas**: zscore_desarrollo_resolucion_problemas
5. **Socio Individual**: zscore_desarrollo_socio_individual

### Categorización de Z-Scores

Los z-scores se categorizaron según los criterios clínicos establecidos:

- **🔴 Alto riesgo**: Z < -2 (requiere intervención inmediata)
- **🟡 Riesgo moderado**: -2 ≤ Z < -1 (requiere seguimiento)
- **🟢 Desarrollo adecuado**: Z ≥ -1 (desarrollo normal)

### Análisis Estadístico

Para cada combinación variable-dominio se realizó:

1. **Prueba estadística apropiada**:
   - Chi-cuadrado: para tablas con frecuencias esperadas ≥ 5
   - Test exacto de Fisher: para tablas con frecuencias pequeñas

2. **Cálculo de odds ratios** (para resultados significativos):
   - OR con intervalos de confianza del 95%
   - Interpretación clínica del riesgo

3. **Tablas de contingencia** con:
   - Conteos absolutos
   - Proporciones por fila
   - Estadísticos de prueba

## Resultados Principales

### Estadísticas Generales
- **Total de análisis realizados**: 240 combinaciones
- **Asociaciones estadísticamente significativas**: 235 (97.9%)
- **Muestra total**: 1,725 observaciones

### Distribución de Riesgo por Dominio

| Dominio | N | Alto Riesgo (%) | Riesgo Moderado (%) | Desarrollo Adecuado (%) | Media Z-Score |
|---------|---|-----------------|---------------------|-------------------------|---------------|
| Comunicación | 1,725 | 0.8 | 4.8 | 94.4 | 0.111 |
| Motricidad Gruesa | 1,725 | 3.1 | 13.6 | 83.3 | -0.269 |
| Motricidad Fina | 1,725 | 1.4 | 7.2 | 91.4 | -0.077 |
| Resolución Problemas | 1,725 | 0.7 | 6.7 | 92.6 | -0.068 |
| Socio Individual | 1,725 | 1.0 | 6.3 | 92.8 | 0.034 |

### Dominio más Vulnerable
**Motricidad Gruesa** presenta el mayor riesgo combinado (16.7%) y la media z-score más baja (-0.269), indicando necesidad de intervención prioritaria.

## Interpretación Clínica

### Factores de Mayor Riesgo Identificados

Las variables con asociaciones significativas en todos los dominios incluyen:
- **Edad del niño**: Patrones específicos de riesgo por edad
- **Características parentales**: Edad y educación de padres
- **Factores socioeconómicos**: Área de residencia, acceso a servicios
- **Condiciones de salud**: Historia de hospitalizaciones, estado nutricional

### Recomendaciones para Salud Pública

1. **Intervención Prioritaria**:
   - Enfocar recursos en motricidad gruesa
   - Programas específicos para grupos de alto riesgo identificados

2. **Monitoreo Continuo**:
   - Seguimiento especial para población con factores de riesgo
   - Evaluación periódica del desarrollo neurológico

3. **Prevención Temprana**:
   - Programas de estimulación temprana dirigidos
   - Capacitación a cuidadores y profesionales

## Limitaciones del Estudio

- **Diseño transversal**: No establece causalidad
- **Múltiples comparaciones**: Posible inflación del error tipo I
- **Necesidad de validación**: Estudios longitudinales requeridos

## Cómo Usar Este Análisis

1. **Para revisión rápida**: Consultar `resumen_hallazgos_significativos.txt`
2. **Para análisis detallado**: Revisar `analisis_chi_cuadrado_completo.txt`
3. **Para visualización**: Abrir archivos PNG/PDF generados
4. **Para análisis estadístico**: Usar datos en `estadisticas_resumen_dominios.csv`

## Requisitos Técnicos

### Dependencias Python
```bash
pip install pandas numpy scipy matplotlib seaborn statsmodels
```

### Ejecución
```bash
python3 analisis_chi_cuadrado_completo.py
python3 generar_resumen_hallazgos.py
python3 crear_visualizaciones.py
```

## Estructura del Proyecto

```
data-tesis/
├── datos_optimizados.csv                    # Datos originales
├── analisis_chi_cuadrado_completo.py        # Script principal
├── analisis_chi_cuadrado_completo.txt       # Análisis detallado
├── resumen_hallazgos_significativos.txt     # Resumen ejecutivo
├── estadisticas_resumen_dominios.csv        # Estadísticas por dominio
├── hallazgos_neurodesarrollo.png           # Visualizaciones principales
├── correlaciones_dominios.png              # Correlaciones
└── README_ANALISIS_CHI_CUADRADO.md         # Este archivo
```

## Contacto y Soporte

Para preguntas sobre la metodología, interpretación de resultados o replicación del análisis, consultar los scripts comentados o la documentación técnica incluida en cada archivo.

---

**Fecha de análisis**: 17/07/2025  
**Versión**: 1.0  
**Formato de salida**: Análisis completo con interpretaciones clínicas en español