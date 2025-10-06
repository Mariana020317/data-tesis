# Análisis de Chi-cuadrado con Interpretaciones Detalladas de Odds Ratios

## Descripción del Proyecto

Este proyecto implementa un análisis estadístico completo para evaluar asociaciones entre variables categóricas y el desarrollo neuromotor en población infantil, con énfasis en la interpretación clínica de Odds Ratios para resultados estadísticamente significativos.

## Archivos Principales

### Scripts de Análisis
- `analisis_chi_cuadrado_odds_ratios.py`: Análisis principal con interpretaciones detalladas de OR
- `analisis_complementario.py`: Análisis específico para variables categóricas múltiples

### Datos
- `datos_optimizados.csv`: Dataset principal con 1,725 observaciones y 57 variables

### Resultados Generados
- `forest_plot_odds_ratios.png`: Gráfico de forest plot con top 10 asociaciones
- `graficos_nivel_educativo_materno.png`: Gráficos específicos por nivel educativo materno
- `resumen_resultados_significativos.csv`: Tabla resumen de resultados significativos
- `informe_analisis_odds_ratios.txt`: Informe completo del análisis

## Metodología

### 1. Categorización de Variables de Desarrollo
- **Riesgo combinado**: Z-score < -1.0 (combina alto riesgo + riesgo de trastorno)
- **Desarrollo adecuado**: Z-score ≥ -1.0

### 2. Dominios de Desarrollo Analizados
- Comunicación
- Motricidad Gruesa
- Motricidad Fina
- Resolución de Problemas
- Socio Individual

### 3. Variables Categóricas Analizadas
- Área de residencia (Rural/Urbano)
- Sexo del niño
- Grupo étnico
- Nivel educativo madre/padre
- Nacimiento prematuro
- Retardo del crecimiento
- Desnutrición aguda
- Vacunación completa
- Seguro social
- Y otras variables sociodemográficas

### 4. Análisis Estadístico
- **Test de chi-cuadrado**: Para evaluar asociaciones
- **Odds Ratios con IC 95%**: Solo para resultados significativos (p < 0.05)
- **Test exacto de Fisher**: Para cálculo de p-valores precisos
- **Corrección de continuidad**: Para celdas con valores pequeños

## Hallazgos Principales

### Asociaciones Más Fuertes (OR > 1.5)
1. **Retardo del crecimiento → Desarrollo Socio Individual**: OR = 2.03 (IC: 1.26-3.25)
2. **Desnutrición aguda → Desarrollo Socio Individual**: OR = 1.97 (IC: 1.07-3.64)
3. **Nacimiento prematuro → Resolución de Problemas**: OR = 1.60 (IC: 1.09-2.36)
4. **Retardo del crecimiento → Motricidad Gruesa**: OR = 1.52 (IC: 1.05-2.19)

### Factores Protectores
- **Área urbana**: Menor riesgo en todos los dominios comparado con área rural
- **Grupo étnico no indígena**: Menor riesgo en resolución de problemas y desarrollo socio individual
- **Mayor nivel educativo materno**: Tendencia protectora consistente en todos los dominios

### Interpretación Clínica

#### Magnitud de Asociaciones
- **OR = 1.0**: Sin asociación
- **OR = 1.1 - 1.4**: Asociación débil
- **OR = 1.5 - 2.9**: Asociación moderada ✓
- **OR = 3.0 - 9.9**: Asociación fuerte
- **OR ≥ 10.0**: Asociación muy fuerte

#### Relevancia para Salud Pública
- **OR ≥ 2.0**: Relevancia ALTA - Requiere intervención prioritaria
- **OR ≥ 1.5**: Relevancia MODERADA - Requiere atención especial
- **OR < 1.5**: Relevancia BAJA - Monitoreo regular

## Métricas Adicionales Calculadas

### Para cada asociación significativa:
- **Diferencia de Riesgo Absoluto**: Diferencia porcentual entre grupos
- **Número Necesario para Tratar (NNT)**: Pacientes a tratar para prevenir 1 caso
- **Riesgo Atribuible**: Porcentaje de riesgo atribuible a la exposición

## Recomendaciones Clínicas

### Poblaciones Prioritarias
1. **Niños con retardo del crecimiento**: Screening integral del desarrollo
2. **Niños con desnutrición aguda**: Evaluación socio-individual prioritaria
3. **Prematuros**: Seguimiento específico en resolución de problemas
4. **Población rural**: Intervención comunitaria en desarrollo neuromotor

### Intervenciones Sugeridas
- **Nivel educativo materno**: Programas de educación parental
- **Nutrición**: Intervención nutricional temprana
- **Seguimiento**: Protocolo de seguimiento para prematuros
- **Acceso**: Mejorar acceso a servicios en áreas rurales

## Validación Estadística

### Supuestos del Chi-cuadrado
- Verificación de frecuencias esperadas ≥ 5
- Corrección de Yates cuando apropiado
- Test exacto de Fisher para conteos pequeños

### Intervalos de Confianza
- IC 95% para todos los OR
- Interpretación de significancia estadística
- Evaluación de precisión de estimaciones

## Uso de los Scripts

### Análisis Principal
```bash
python3 analisis_chi_cuadrado_odds_ratios.py
```

### Análisis Complementario
```bash
python3 analisis_complementario.py
```

## Dependencias
- pandas
- numpy  
- scipy
- matplotlib
- seaborn

## Formato de Salida

### Ejemplo de Interpretación Detallada
```
**Odds Ratio e Interpretación:**
OR = 2.03 (IC 95%: 1.26 - 3.25)

**Interpretación clínica:**
- Los niños con retardo del crecimiento tienen 2.03 veces mayor probabilidad de presentar trastornos socio-individuales
- El riesgo es MODERADO según la magnitud del OR (1.5 - 2.9)

**Significancia clínica:**
- Diferencia de riesgo absoluto: 7.8%
- Número necesario para tratar: 13 pacientes
- Relevancia para salud pública: ALTA

**Conclusión clínica:**
La población con retardo del crecimiento requiere intervención prioritaria en el desarrollo socio-individual.
```

## Limitaciones

1. **Diseño transversal**: No permite inferir causalidad
2. **Variables confusoras**: Pueden existir factores no controlados
3. **Categorización**: Simplificación de variables continuas
4. **Generalización**: Específico para la población estudiada

## Interpretación de Resultados

### Significancia Estadística vs. Clínica
- Todos los OR reportados son estadísticamente significativos (p < 0.05)
- La relevancia clínica se evalúa por magnitud del OR y contexto
- Las recomendaciones priorizan asociaciones con mayor impacto clínico

### Direccionalidad
- OR > 1.0: Factor de riesgo
- OR < 1.0: Factor protector
- OR = 1.0: Sin asociación

## Contacto y Soporte

Para dudas sobre la metodología o interpretación de resultados, consultar la documentación técnica incluida en cada script.