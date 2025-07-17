# Análisis Exhaustivo de Chi-Cuadrado para Neurodesarrollo

Este proyecto implementa un análisis exhaustivo de chi-cuadrado para evaluar asociaciones entre variables categóricas y los dominios del neurodesarrollo en datos de tesis.

## Características Principales

### ✅ Requerimientos Implementados

1. **Manejo de datos faltantes:**
   - Ignora completamente los valores NA/missing en todos los análisis
   - No imputa ni rellena datos faltantes
   - Política estricta de exclusión de observaciones con valores faltantes

2. **Generación de tablas completas:**
   - Crea tablas de contingencia para TODAS las asociaciones entre cada variable categórica y los 5 dominios del neurodesarrollo
   - Muestra las tablas para cada combinación variable-dominio, incluso si no son significativas
   - Incluye conteos absolutos y porcentajes en las tablas

3. **Interpretación en español:**
   - Describe cada tabla en español
   - Explica si la asociación es estadísticamente significativa (p < 0.05)
   - Interpreta hacia qué categoría se inclina la asociación
   - Identifica qué categorías tienen mayor/menor riesgo

4. **Dominios del neurodesarrollo evaluados:**
   - `zscore_desarrollo_comunicacion` → Comunicación
   - `zscore_desarrollo_motricidad_gruesa` → Motricidad Gruesa
   - `zscore_desarrollo_motricidad_fina` → Motricidad Fina
   - `zscore_desarrollo_resolucion_problemas` → Resolución de Problemas
   - `zscore_desarrollo_socio_individual` → Desarrollo Socio-Individual

5. **Categorías de riesgo:**
   - **Desarrollo adecuado:** Z ≥ -1
   - **Riesgo de trastornos:** -2 ≤ Z < -1
   - **Alto riesgo:** Z < -2

## Estructura del Proyecto

```
data-tesis/
├── datos_optimizados.csv          # Dataset principal (1,725 observaciones)
├── analisis_chi_cuadrado.py       # Script principal del análisis
├── validacion_analisis.py         # Script de validación y resumen
├── reporte_chi_cuadrado.md        # Reporte completo generado (9,185 líneas)
└── README.md                      # Este archivo
```

## Instalación y Uso

### Requisitos

```bash
pip install pandas numpy scipy
```

### Ejecución Básica

```bash
# Ejecutar análisis completo
python analisis_chi_cuadrado.py

# Validar resultados
python validacion_analisis.py
```

### Uso Programático

```python
from analisis_chi_cuadrado import AnalisisChiCuadrado

# Crear instancia del análisis
analisis = AnalisisChiCuadrado('datos_optimizados.csv')

# Ejecutar análisis completo
reporte_completo = analisis.ejecutar_analisis_completo()

# Analizar variable específica
resultado_variable = analisis.analizar_variable_completa('grupo_etnico')

# Analizar asociación específica
resultado_asociacion = analisis.analizar_variable_dominio(
    'grupo_etnico', 
    'zscore_desarrollo_comunicacion'
)
```

## Resultados del Análisis

### Alcance del Análisis

- **Total de observaciones:** 1,725
- **Variables categóricas analizadas:** 50
- **Dominios del neurodesarrollo:** 5
- **Análisis chi-cuadrado realizados:** 250
- **Tablas de contingencia generadas:** 250
- **Interpretaciones en español:** 250

### Variables Categóricas Analizadas

1. `centro_atencion_salud`
2. `sexo_nino`
3. `nacimiento_prematuro`
4. `grupo_etnico`
5. `area_residencia`
6. `nivel_educativo_madre`
7. `nivel_educativo_padre`
8. Y 43 variables adicionales...

### Distribución de Categorías de Riesgo

| Dominio | Desarrollo Adecuado | Riesgo de Trastornos | Alto Riesgo |
|---------|---------------------|----------------------|-------------|
| Comunicación | 1,628 (94.4%) | 83 (4.8%) | 14 (0.8%) |
| Motricidad Gruesa | 1,437 (83.3%) | 234 (13.6%) | 54 (3.1%) |
| Motricidad Fina | 1,577 (91.4%) | 124 (7.2%) | 24 (1.4%) |
| Resolución de Problemas | 1,597 (92.6%) | 116 (6.7%) | 12 (0.7%) |
| Desarrollo Socio-Individual | 1,600 (92.8%) | 108 (6.3%) | 17 (1.0%) |

## Ejemplo de Formato de Salida

```markdown
### Variable: grupo_etnico

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                          
Indígena                                            6                  691                    44   741
No indígena                                         8                  937                    39   984
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                    
Indígena                                          0.8                 93.3                   5.9
No indígena                                       0.8                 95.2                   4.0

**Estadísticos:**
- Chi-cuadrado: 3.599
- Valor p: 0.165
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.599, p = 0.165).
No se puede concluir que exista una asociación significativa entre estas variables.
```

## Características Técnicas

### Manejo de Datos

- **Exclusión de valores faltantes:** Todas las observaciones con valores faltantes se excluyen completamente del análisis
- **No imputación:** No se realiza ningún tipo de imputación o relleno de datos
- **Categorización automática:** Los z-scores se categorizan automáticamente según los criterios establecidos

### Estadísticos Calculados

- **Chi-cuadrado de Pearson:** Estadístico de prueba para independencia
- **Valor p:** Probabilidad de obtener el resultado bajo hipótesis nula
- **Grados de libertad:** Calculados según las dimensiones de la tabla

### Interpretaciones

- **Significancia estadística:** Evaluada con α = 0.05
- **Análisis de categorías:** Identificación de categorías con mayor/menor riesgo
- **Interpretaciones descriptivas:** Explicaciones claras en español

## Validación

El script `validacion_analisis.py` proporciona:

- Verificación de la integridad del análisis
- Estadísticas resumen del dataset
- Validación del manejo de datos faltantes
- Confirmación de la estructura del reporte

## Limitaciones

- Los análisis se basan en datos categorizados según los criterios establecidos
- No se realizan análisis post-hoc para comparaciones múltiples
- Las interpretaciones se basan únicamente en estadísticos chi-cuadrado

## Contacto

Para preguntas o mejoras, contactar al equipo de desarrollo del proyecto de tesis.