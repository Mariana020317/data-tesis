# Configuración de Visualizaciones PDF para Papel

## Cambios Implementados

### 1. Fondo Transparente
- **Configuración**: `facecolor='none'`, `transparent=True`
- **Beneficio**: Los gráficos se adaptan al fondo del documento donde se insertan
- **Aplicación**: Todos los gráficos PDF generados

### 2. Tema Nord Optimizado para Papel

#### Colores Adaptados
- **Fondo**: Transparente (anteriormente oscuro)
- **Área de graficación**: Blanco (anteriormente gris oscuro)
- **Texto**: Oscuro `#2E3440` (anteriormente claro)
- **Grillas**: Sutil `#E5E9F0` con mayor opacidad (anteriormente oscura)

#### Paleta de Colores
Mantenemos la identidad Nord pero con colores más contrastantes:
- **Azul**: `#5E81AC` (más oscuro para mejor contraste)
- **Rojo**: `#BF616A` (mantiene buen contraste)
- **Verde**: `#A3BE8C` (mantiene buen contraste)
- **Naranja**: `#D08770` (más oscuro para papel)
- **Púrpura**: `#B48EAD` (mantiene identidad Nord)

### 3. Mejoras en Legibilidad

#### Leyendas
- **Fondo**: Blanco con borde sutil
- **Transparencia**: Optimizada para lectura
- **Bordes**: Líneas delgadas para mayor refinamiento

#### Texto en Heatmap
- **Lógica mejorada**: Texto blanco para valores >20%, texto oscuro para valores menores
- **Contraste**: Optimizado para diferentes intensidades de color

#### Colormap
- **Heatmap**: Cambiado a `RdBu_r` (Rojo-Azul) para mejor impresión en papel
- **Contraste**: Mejorado para distinguir valores en impresión

### 4. Configuración Técnica

#### Matplotlib Settings
```python
'savefig.transparent': True,
'savefig.facecolor': 'none',
'figure.facecolor': 'none',
'axes.facecolor': 'white'
```

#### Resolución
- **DPI**: 300 (alta calidad para impresión)
- **Formato**: PDF vectorial (escala sin pérdida)

## Archivos Generados

1. **`prevalencia_edad_nord.pdf`**
   - Gráfico de líneas con prevalencia por edad
   - Fondo transparente, texto oscuro
   - Leyenda optimizada para papel

2. **`odds_ratios_nord.pdf`**
   - Gráfico de barras horizontales con OR
   - Colores categorizados por nivel de riesgo
   - Transparente y listo para inserción

3. **`heatmap_riesgo_edad_nord.pdf`**
   - Mapa de calor con colormap RdBu_r
   - Texto contrastante según intensidad
   - Colorbar optimizada para papel

## Beneficios para Impresión

### ✅ Calidad de Impresión
- **Resolución**: 300 DPI para impresión profesional
- **Vectorial**: PDF escalable sin pérdida de calidad
- **Colores**: Optimizados para impresoras láser y tinta

### ✅ Integración en Documentos
- **Transparencia**: Se adapta a cualquier fondo de documento
- **Contraste**: Texto oscuro garantiza legibilidad
- **Estilo**: Mantiene identidad Nord pero apropiada para papel

### ✅ Accesibilidad
- **Contraste**: Cumple estándares de accesibilidad visual
- **Legibilidad**: Texto oscuro sobre fondo claro
- **Coherencia**: Estilo uniforme en todos los gráficos

## Validación de Odds Ratios

Los cálculos de odds ratios han sido validados con múltiples métodos:
- ✅ Fisher's exact test
- ✅ Cálculo manual
- ✅ StatsModels
- ✅ Intervalos de confianza correctos

## Recomendaciones de Uso

1. **Inserción en documentos**: Los PDFs se pueden insertar directamente
2. **Impresión**: Configurar impresora en alta calidad (300+ DPI)
3. **Visualización**: Funciona tanto en pantalla como en papel
4. **Edición**: Mantener formato PDF para escalabilidad

---

*Generado automáticamente por el sistema de análisis estadístico*
*Fecha: Julio 2025*