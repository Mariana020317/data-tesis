# Análisis Reorganizado por Variable: Documentación

## Descripción General

Este repositorio contiene un análisis estadístico reorganizado que clasifica los resultados por variable (en lugar de por dominio) siguiendo la secuencia obligatoria: **Chi-cuadrado → Descripción de resultados significativos → Odds Ratio**.

## Estructura del Análisis

### 1. Metodología Implementada

El análisis sigue la estructura especificada en los requerimientos:

- **Organización por variable**: Cada variable se analiza completa antes de pasar a la siguiente
- **Secuencia obligatoria**: Chi-cuadrado → Descripción → Odds Ratio
- **Cinco dominios del neurodesarrollo**: Comunicación, Motricidad gruesa, Motricidad fina, Resolución de problemas, Socio-individual
- **Orden de variables**: Según prioridad clínica (sociodemográficas, educativas, socioeconómicas, etc.)

### 2. Archivos Principales

- `analisis_reorganizado.R`: Script completo con todas las variables del estudio
- `analisis_demo.R`: Script de demostración con variables prioritarias
- `test_analisis.R`: Script de validación de la funcionalidad básica
- `datos_optimizados.csv`: Datos del estudio

## Uso del Análisis

### Ejecución del Script de Demostración

```bash
R --vanilla < analisis_demo.R > resultados_demo.txt
```

### Ejecución del Análisis Completo

```bash
R --vanilla < analisis_reorganizado.R > resultados_completos.txt
```

## Ejemplo de Salida

### Estructura por Variable

```
================================================================================
### VARIABLE: AREA_RESIDENCIA
================================================================================

#### DOMINIO: Comunicación
--------------------------------------------------
**Chi-cuadrado:**
χ² = 8.70, gl = 1, p = 0.003

**Descripción de resultados:**
- La prueba indica una asociación estadísticamente significativa entre area_residencia y Comunicación
- Las diferencias observadas en las proporciones no se deben al azar
- El estadístico chi-cuadrado de 8.70 con 1 grados de libertad supera el valor crítico
- La significancia es moderada (p 0.003), indicando evidencia sólida de asociación

**Tabla de contingencia:**
        Desarrollo adecuado  Riesgo  Total
Rural                 232      25    257
Urbano               1396      72   1468
Total                1628      97   1725

**Proporciones:**
- Rural: 9.7% riesgo vs 90.3% desarrollo adecuado
- Urbano: 4.9% riesgo vs 95.1% desarrollo adecuado
- Diferencia de riesgo: 4.8% mayor en Rural

**Odds Ratio:**
OR = 0.48 (IC 95%: 0.30 - 0.77)
**Interpretación:** Asociación débil
- El riesgo de retraso en Comunicación es 2.09 veces menor en el grupo de referencia
- Factor protector con magnitud: moderada
```

### Tabla Resumen por Variable

```
================================================================================
### RESUMEN: AREA_RESIDENCIA
================================================================================

| Dominio | Chi-cuadrado | p-valor | OR | IC 95% | Significativo |
|---------|--------------|---------|----|---------|--------------| 
| Comunicación | 8.70 | 0.003 | 0.48 | 0.30-0.77 | Sí |
| Motricidad gruesa | 12.62 | < 0.001 | 0.56 | 0.41-0.77 | Sí |
| Motricidad fina | 1.73 | 0.188 | - | - | No |
| Resolución de problemas | 25.13 | < 0.001 | 0.36 | 0.24-0.54 | Sí |
| Socio-individual | 15.06 | < 0.001 | 0.43 | 0.29-0.66 | Sí |

**Conclusión clínica:**
area_residencia afecta significativamente 4 de 5 dominios del neurodesarrollo, 
con mayor impacto en Motricidad gruesa (OR = 0.56).
Prioridad de intervención: ALTA
```

### Resumen General

```
## RESUMEN GENERAL DE VARIABLES ANALIZADAS

| Variable | Dominios afectados | OR máximo | Dominio de mayor impacto | Prioridad |
|----------|-------------------|-----------|--------------------------|----------|
| area_residencia | 4/5 | 0.56 | Motricidad gruesa | Alta |
| grupo_etnico | 2/5 | 0.66 | Resolución de problemas | Media |
| nivel_educativo_madre | 5/5 | 0.00 | Comunicación | Alta |
| seguro_social | 0/5 | - | - | Baja |
| retardo_crecimiento | 2/5 | 2.03 | Socio-individual | Media |
```

## Características Técnicas

### Validación Estadística

- **Supuestos del Chi-cuadrado**: Verificación automática antes de cada análisis
- **Corrección para tablas pequeñas**: Uso automático del test exacto de Fisher cuando es apropiado
- **Manejo de errores**: Simulación automática cuando Fisher falla con tablas grandes
- **Intervalos de confianza**: Cálculo automático del IC 95% para todos los OR significativos

### Interpretación Clínica

- **Magnitud del OR**: Clasificación automática (débil, moderada, fuerte, muy fuerte)
- **Diferencia de riesgo**: Cálculo automático para tablas 2x2
- **Prioridad de intervención**: Basada en número de dominios afectados
- **Contexto clínico**: Interpretación específica para cada variable

## Variables Incluidas

### 1. Variables Sociodemográficas
- edad_meses_nino
- grupo_etnico
- area_residencia
- sexo_jefe_hogar

### 2. Variables Educativas
- nivel_educativo_madre
- nivel_educativo_padre

### 3. Variables Socioeconómicas
- situacion_laboral_madre
- situacion_laboral_padre
- tipo_empleo_madre
- tipo_empleo_padre
- seguro_social
- propiedad_vivienda

### 4. Variables de Vivienda y Servicios
- fuente_agua_consumo
- tipo_sanitario
- manejo_basura
- tipo_energia_luz
- tipo_energia_cocina

### 5. Variables Familiares
- edad_anos_madre
- edad_anos_padre
- total_personas_hogar
- total_hermanos
- posicion_nino_hermanos
- estado_civil_cuidador

### 6. Variables de Cuidado
- horas_pantalla
- horas_juego_cuidador

### 7. Variables Prenatales
- numero_controles_prenatales
- ultrasonido_embarazo
- prenatales_primeros_3_meses
- prenatales_resto_embarazo
- servicio_asistencia_parto
- tipo_parto
- razon_cesarea_emergencia

### 8. Variables Nutricionales
- lactancia_primeros_6_meses
- lactancia_6-12_meses
- lactancia_12-24_meses
- vitamina_a_6-12_meses
- vitamina_a_12-18_meses
- vitamina_a_18-24_meses
- vitaminas_minerales_6-12_meses
- vitaminas_minerales_12-18_meses
- vitaminas_minerales_18-24_meses

### 9. Variables de Salud
- retardo_crecimiento
- desnutricion_aguda
- hospitalizado_neonatal
- razon_hospitalizado_neonatal
- hospitalizado_infancia
- razon_hospitalizado_infancia
- vacunacion_completa

## Dominios del Neurodesarrollo

1. **Comunicación**: Habilidades de lenguaje receptivo y expresivo
2. **Motricidad gruesa**: Coordinación y control de movimientos corporales grandes
3. **Motricidad fina**: Coordinación y control de movimientos precisos
4. **Resolución de problemas**: Capacidades cognitivas y de razonamiento
5. **Socio-individual**: Habilidades sociales y de auto-cuidado

## Ventajas del Nuevo Formato

### Para Investigadores
- **Análisis integral**: Cada variable se evalúa completamente antes de pasar a la siguiente
- **Priorización clara**: Identificación inmediata de variables de alta prioridad
- **Interpretación clínica**: Contextualización automática de resultados estadísticos

### Para Clínicos
- **Toma de decisiones**: Información organizada para priorizar intervenciones
- **Comprensión rápida**: Formato estructurado que facilita la interpretación
- **Aplicación práctica**: Recomendaciones basadas en evidencia estadística

### Para Salud Pública
- **Política basada en evidencia**: Identificación de factores de riesgo prioritarios
- **Asignación de recursos**: Priorización clara de intervenciones
- **Monitoreo y evaluación**: Métricas claras para seguimiento

## Requisitos Técnicos

- **Software**: R versión 4.0 o superior
- **Dependencias**: Utiliza solo funciones base de R (sin paquetes adicionales)
- **Datos**: Archivo CSV con estructura específica
- **Memoria**: Aproximadamente 100MB para procesamiento completo

## Mantenimiento y Actualización

El script está diseñado para ser fácilmente actualizable:
- Nuevas variables pueden agregarse al lista `variables_analisis`
- Criterios de interpretación pueden modificarse en las funciones correspondientes
- Formato de salida puede personalizarse según necesidades específicas

## Contacto y Soporte

Para preguntas técnicas o modificaciones específicas, consulte la documentación del código o contacte al equipo de desarrollo.