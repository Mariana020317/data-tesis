#!/usr/bin/env python3
"""
Visualización de hallazgos clave del análisis chi-cuadrado
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def crear_visualizaciones():
    """Crear visualizaciones clave de los hallazgos"""
    
    print("Generando visualizaciones de hallazgos clave...")
    
    # Cargar datos
    df = pd.read_csv("datos_optimizados.csv")
    
    # Configurar estilo
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análisis Chi-Cuadrado: Hallazgos Clave del Neurodesarrollo', fontsize=16, fontweight='bold')
    
    # Categorizar z-scores
    dominios = [
        "zscore_desarrollo_comunicacion",
        "zscore_desarrollo_motricidad_gruesa", 
        "zscore_desarrollo_motricidad_fina",
        "zscore_desarrollo_resolucion_problemas",
        "zscore_desarrollo_socio_individual"
    ]
    
    for dominio in dominios:
        if dominio in df.columns:
            zscore_col = df[dominio]
            categoria_col = f"{dominio}_categoria"
            
            # Crear categorías
            zscore_valid = ~pd.isna(zscore_col)
            condiciones = [
                zscore_valid & (zscore_col < -2),
                zscore_valid & (zscore_col >= -2) & (zscore_col < -1),
                zscore_valid & (zscore_col >= -1)
            ]
            
            categorias = [
                "Alto riesgo",
                "Riesgo moderado",
                "Desarrollo adecuado"
            ]
            
            df[categoria_col] = np.select(condiciones, categorias, default="Sin datos")
    
    # Gráfico 1: Distribución de riesgo por grupo étnico
    ax1 = axes[0, 0]
    if 'grupo_etnico' in df.columns and 'zscore_desarrollo_comunicacion_categoria' in df.columns:
        tabla_etnico = pd.crosstab(df['grupo_etnico'], df['zscore_desarrollo_comunicacion_categoria'])
        tabla_etnico_pct = tabla_etnico.div(tabla_etnico.sum(axis=1), axis=0) * 100
        
        tabla_etnico_pct.plot(kind='bar', ax=ax1, color=['#d62728', '#ff7f0e', '#2ca02c'])
        ax1.set_title('Riesgo de Desarrollo en Comunicación por Grupo Étnico', fontweight='bold')
        ax1.set_xlabel('Grupo Étnico')
        ax1.set_ylabel('Porcentaje')
        ax1.legend(title='Nivel de Riesgo', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.tick_params(axis='x', rotation=45)
    
    # Gráfico 2: Riesgo por área de residencia
    ax2 = axes[0, 1]
    if 'area_residencia' in df.columns and 'zscore_desarrollo_motricidad_gruesa_categoria' in df.columns:
        tabla_area = pd.crosstab(df['area_residencia'], df['zscore_desarrollo_motricidad_gruesa_categoria'])
        tabla_area_pct = tabla_area.div(tabla_area.sum(axis=1), axis=0) * 100
        
        tabla_area_pct.plot(kind='bar', ax=ax2, color=['#d62728', '#ff7f0e', '#2ca02c'])
        ax2.set_title('Riesgo de Desarrollo en Motricidad Gruesa por Área', fontweight='bold')
        ax2.set_xlabel('Área de Residencia')
        ax2.set_ylabel('Porcentaje')
        ax2.legend(title='Nivel de Riesgo', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.tick_params(axis='x', rotation=45)
    
    # Gráfico 3: Riesgo por nivel educativo materno
    ax3 = axes[1, 0]
    if 'nivel_educativo_madre' in df.columns and 'zscore_desarrollo_resolucion_problemas_categoria' in df.columns:
        # Agrupar niveles educativos para mejor visualización
        df_temp = df.copy()
        df_temp['nivel_educativo_madre_agrupado'] = df_temp['nivel_educativo_madre'].replace({
            'Ninguna': 'Sin educación',
            'Primaria': 'Primaria',
            'Básico': 'Básico',
            'Diversificado': 'Diversificado',
            'Universitario': 'Universitario'
        })
        
        tabla_educacion = pd.crosstab(df_temp['nivel_educativo_madre_agrupado'], 
                                     df_temp['zscore_desarrollo_resolucion_problemas_categoria'])
        tabla_educacion_pct = tabla_educacion.div(tabla_educacion.sum(axis=1), axis=0) * 100
        
        tabla_educacion_pct.plot(kind='bar', ax=ax3, color=['#d62728', '#ff7f0e', '#2ca02c'])
        ax3.set_title('Riesgo en Resolución de Problemas por Educación Materna', fontweight='bold')
        ax3.set_xlabel('Nivel Educativo Materno')
        ax3.set_ylabel('Porcentaje')
        ax3.legend(title='Nivel de Riesgo', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax3.tick_params(axis='x', rotation=45)
    
    # Gráfico 4: Resumen general de riesgo por dominio
    ax4 = axes[1, 1]
    resumen_dominios = []
    nombres_dominios = []
    
    for dominio in dominios:
        categoria_col = f"{dominio}_categoria"
        if categoria_col in df.columns:
            conteos = df[categoria_col].value_counts()
            if 'Alto riesgo' in conteos:
                alto_riesgo_pct = conteos['Alto riesgo'] / conteos.sum() * 100
            else:
                alto_riesgo_pct = 0
            
            resumen_dominios.append(alto_riesgo_pct)
            nombres_dominios.append(dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title())
    
    bars = ax4.bar(nombres_dominios, resumen_dominios, color='#d62728', alpha=0.7)
    ax4.set_title('Porcentaje de Alto Riesgo por Dominio del Neurodesarrollo', fontweight='bold')
    ax4.set_xlabel('Dominio del Neurodesarrollo')
    ax4.set_ylabel('Porcentaje en Alto Riesgo')
    ax4.tick_params(axis='x', rotation=45)
    
    # Añadir etiquetas de porcentaje en las barras
    for bar, pct in zip(bars, resumen_dominios):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('hallazgos_neurodesarrollo.png', dpi=300, bbox_inches='tight')
    plt.savefig('hallazgos_neurodesarrollo.pdf', bbox_inches='tight')
    
    print("Visualizaciones guardadas:")
    print("- hallazgos_neurodesarrollo.png")
    print("- hallazgos_neurodesarrollo.pdf")
    
    # Crear gráfico adicional: heatmap de correlaciones
    plt.figure(figsize=(12, 8))
    
    # Crear matriz de correlaciones entre dominios
    zscore_data = df[dominios].dropna()
    if len(zscore_data) > 0:
        corr_matrix = zscore_data.corr()
        
        # Crear heatmap
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='RdYlBu_r', center=0,
                   square=True, fmt='.2f', cbar_kws={"shrink": .8})
        
        plt.title('Correlaciones entre Dominios del Neurodesarrollo', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('correlaciones_dominios.png', dpi=300, bbox_inches='tight')
        plt.savefig('correlaciones_dominios.pdf', bbox_inches='tight')
        
        print("- correlaciones_dominios.png")
        print("- correlaciones_dominios.pdf")
    
    plt.close('all')

def generar_tabla_resumen():
    """Generar tabla resumen de estadísticas clave"""
    
    print("\nGenerando tabla resumen de estadísticas...")
    
    # Cargar datos
    df = pd.read_csv("datos_optimizados.csv")
    
    # Calcular estadísticas por dominio
    dominios = [
        "zscore_desarrollo_comunicacion",
        "zscore_desarrollo_motricidad_gruesa", 
        "zscore_desarrollo_motricidad_fina",
        "zscore_desarrollo_resolucion_problemas",
        "zscore_desarrollo_socio_individual"
    ]
    
    estadisticas = []
    
    for dominio in dominios:
        if dominio in df.columns:
            zscore_data = df[dominio].dropna()
            
            # Calcular porcentajes por categoría
            alto_riesgo = (zscore_data < -2).sum()
            riesgo_moderado = ((zscore_data >= -2) & (zscore_data < -1)).sum()
            desarrollo_adecuado = (zscore_data >= -1).sum()
            total = len(zscore_data)
            
            estadisticas.append({
                'Dominio': dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title(),
                'N': total,
                'Alto Riesgo (%)': f"{alto_riesgo/total*100:.1f}",
                'Riesgo Moderado (%)': f"{riesgo_moderado/total*100:.1f}",
                'Desarrollo Adecuado (%)': f"{desarrollo_adecuado/total*100:.1f}",
                'Media Z-Score': f"{zscore_data.mean():.3f}",
                'DE Z-Score': f"{zscore_data.std():.3f}"
            })
    
    # Crear DataFrame y guardarlo
    df_stats = pd.DataFrame(estadisticas)
    df_stats.to_csv('estadisticas_resumen_dominios.csv', index=False)
    
    # Guardar como tabla formateada
    with open('estadisticas_resumen_dominios.txt', 'w', encoding='utf-8') as f:
        f.write("# ESTADÍSTICAS RESUMEN POR DOMINIO DEL NEURODESARROLLO\n")
        f.write("=" * 80 + "\n\n")
        f.write(df_stats.to_string(index=False))
        f.write("\n\n")
        f.write("## INTERPRETACIÓN:\n")
        f.write("- Alto Riesgo: Z-score < -2 (requiere intervención inmediata)\n")
        f.write("- Riesgo Moderado: -2 ≤ Z-score < -1 (requiere seguimiento)\n")
        f.write("- Desarrollo Adecuado: Z-score ≥ -1 (desarrollo normal)\n")
        f.write("\n")
        f.write("## RECOMENDACIONES:\n")
        f.write("- Priorizar intervención en dominios con mayor % de alto riesgo\n")
        f.write("- Implementar programas de seguimiento para riesgo moderado\n")
        f.write("- Mantener programas de promoción para desarrollo adecuado\n")
    
    print("Tabla resumen guardada en:")
    print("- estadisticas_resumen_dominios.csv")
    print("- estadisticas_resumen_dominios.txt")
    
    return df_stats

def main():
    """Función principal"""
    print("=== GENERACIÓN DE VISUALIZACIONES Y RESÚMENES ===\n")
    
    # Crear visualizaciones
    crear_visualizaciones()
    
    # Generar tabla resumen
    df_stats = generar_tabla_resumen()
    
    print("\n=== RESUMEN DE ARCHIVOS GENERADOS ===")
    print("Análisis completo:")
    print("- analisis_chi_cuadrado_completo.txt (análisis detallado)")
    print("- resumen_hallazgos_significativos.txt (resumen ejecutivo)")
    print("\nVisualizaciones:")
    print("- hallazgos_neurodesarrollo.png/pdf (gráficos principales)")
    print("- correlaciones_dominios.png/pdf (correlaciones)")
    print("\nTablas resumen:")
    print("- estadisticas_resumen_dominios.csv/txt (estadísticas por dominio)")
    
    print(f"\nTotal de observaciones analizadas: {len(pd.read_csv('datos_optimizados.csv'))}")
    print("Análisis chi-cuadrado completado exitosamente!")

if __name__ == "__main__":
    main()