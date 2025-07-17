# data-tesis

## Análisis de Chi-cuadrado para Identificación de Poblaciones en Riesgo de Trastornos del Neurodesarrollo

Este repositorio contiene un análisis estadístico enfocado en identificar poblaciones con mayor riesgo de trastornos del neurodesarrollo mediante pruebas de chi-cuadrado.

### Características del Análisis

El análisis implementa interpretaciones mejoradas que:

1. **Enfocan en poblaciones de mayor riesgo**: Identifican específicamente qué grupos tienen mayor probabilidad de presentar trastornos del neurodesarrollo
2. **Combinan categorías de riesgo**: Calculan riesgo combinado sumando "Alto riesgo" + "Riesgo de trastorno"
3. **Proporcionan conclusiones clínicas**: Incluyen ratios de riesgo y probabilidades comparativas
4. **Siguen formato estandarizado**: Estructura consistente con interpretación, análisis detallado y conclusión clínica

### Archivos Principales

- `analisis_chi_cuadrado.py`: Script principal que realiza el análisis
- `datos_optimizados.csv`: Datos de entrada con información sobre desarrollo neurológico
- `resultados_analisis_chi_cuadrado.md`: Resultados generados con interpretaciones mejoradas
- `requirements.txt`: Dependencias necesarias para ejecutar el análisis

### Uso

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar el análisis:
```bash
python analisis_chi_cuadrado.py
```

3. Revisar resultados en `resultados_analisis_chi_cuadrado.md`

### Dominios de Neurodesarrollo Analizados

- Desarrollo de comunicación
- Motricidad gruesa
- Motricidad fina
- Resolución de problemas
- Desarrollo socio-individual

### Variables Analizadas

- **Área de residencia**: Rural vs Urbano
- **Grupo étnico**: Indígena vs No indígena
- **Nivel educativo de la madre**: Ninguna, Primaria, Básico, Diversificado, Universitario

### Formato de Interpretación

Cada análisis incluye:

- **Interpretación**: Significancia estadística (χ², p-valor)
- **Análisis detallado**: Identificación del grupo de mayor riesgo, riesgo combinado, diferencias específicas
- **Conclusión clínica**: Ratio de riesgo y probabilidad comparativa

### Ejemplo de Interpretación

```
**Interpretación:**
La asociación entre area_residencia y desarrollo socio-individual ES ESTADÍSTICAMENTE SIGNIFICATIVA (χ² = 17.101, p = 0.000).

**Análisis detallado:**
- Rural presenta mayor riesgo de trastornos del neurodesarrollo en desarrollo socio-individual
- Riesgo combinado: Rural 13.2% vs Urbano 6.2% (diferencia de 7.0%)
- Esta diferencia se debe principalmente a mayor "Alto riesgo" en Rural (2.3% vs 0.7%, diferencia de 1.6%)
- También hay mayor "Riesgo de trastorno" en Rural (10.9% vs 5.4%, diferencia de 5.4%)

**Conclusión clínica:**
Los niños en Rural tienen aproximadamente 2.1 veces mayor probabilidad de presentar algún nivel de riesgo en el desarrollo socio-individual comparado con Urbano.
```