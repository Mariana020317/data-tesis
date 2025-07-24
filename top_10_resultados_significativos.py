#!/usr/bin/env python3
"""
Análisis de los Top 10 Resultados Más Significativos
Incluye chi-square, p-value, odds ratio y CI para las asociaciones más significativas
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    """Carga todos los archivos de resultados estadísticos"""
    
    # Cargar datos de odds ratios de 21 categorías
    or_21_cat = pd.read_csv('odds_ratios_21_categorias_edad.csv')
    
    # Cargar datos de chi-square de 21 categorías  
    chi2_21_cat = pd.read_csv('chi2_21_categorias_edad.csv')
    
    # Cargar datos de chi-square de grupos de edad
    chi2_grupos = pd.read_csv('resultados_chi2.csv')
    
    return or_21_cat, chi2_21_cat, chi2_grupos

def extract_significant_results(or_21_cat, chi2_21_cat, chi2_grupos):
    """Extrae y combina los resultados más significativos"""
    
    results = []
    
    # 1. Resultados de odds ratios de 21 categorías (más granular)
    for _, row in or_21_cat.iterrows():
        if row['significativo']:
            result = {
                'tipo_analisis': f"OR Edad-Específico",
                'descripcion': f"{row['edad_meses']} meses - {row['dominio']}",
                'edad_meses': row['edad_meses'],
                'dominio': row['dominio'],
                'chi2': np.nan,  # No disponible en análisis OR
                'p_value': row['p_value'],
                'odds_ratio': row['odds_ratio'],
                'ci_lower': row['ci_lower'],
                'ci_upper': row['ci_upper'],
                'ci_95': f"({row['ci_lower']:.2f} - {row['ci_upper']:.2f})"
            }
            results.append(result)
    
    # 2. Resultados de chi-square de 21 categorías (análisis global por dominio)
    for _, row in chi2_21_cat.iterrows():
        if row['significativo']:
            result = {
                'tipo_analisis': "Chi² Global 21 Edades",
                'descripcion': f"Análisis global - {row['dominio']}",
                'edad_meses': 'Todas las edades',
                'dominio': row['dominio'],
                'chi2': row['chi2'],
                'p_value': row['p_value'],
                'odds_ratio': np.nan,  # No aplica para chi-square global
                'ci_lower': np.nan,
                'ci_upper': np.nan,
                'ci_95': 'N/A'
            }
            results.append(result)
    
    # 3. Resultados de chi-square de grupos de edad
    for _, row in chi2_grupos.iterrows():
        if row['significativo']:
            result = {
                'tipo_analisis': "Chi² Grupos Edad",
                'descripcion': f"Análisis por grupos - {row['dominio']}",
                'edad_meses': 'Grupos de edad',
                'dominio': row['dominio'],
                'chi2': row['chi2_statistic'],
                'p_value': row['p_value'],
                'odds_ratio': np.nan,  # No aplica para chi-square de grupos
                'ci_lower': np.nan,
                'ci_upper': np.nan,
                'ci_95': 'N/A'
            }
            results.append(result)
    
    return pd.DataFrame(results)

def create_top_10_table(results_df):
    """Crea la tabla de top 10 resultados más significativos"""
    
    # Ordenar por p-value (menor = más significativo)
    top_10 = results_df.nsmallest(10, 'p_value').copy()
    
    # Formatear p-values
    top_10['p_value_formatted'] = top_10['p_value'].apply(lambda x: f"{x:.2e}" if x < 0.001 else f"{x:.3f}")
    
    # Formatear chi-square
    top_10['chi2_formatted'] = top_10['chi2'].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "N/A")
    
    # Formatear odds ratio
    top_10['or_formatted'] = top_10['odds_ratio'].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "N/A")
    
    # Crear interpretación de significancia
    def interpret_significance(p_val):
        if p_val < 0.001:
            return "***"
        elif p_val < 0.01:
            return "**"
        elif p_val < 0.05:
            return "*"
        else:
            return ""
    
    top_10['significancia'] = top_10['p_value'].apply(interpret_significance)
    
    return top_10

def format_for_latex(df):
    """Formatea la tabla para LaTeX"""
    
    latex_df = df[['descripcion', 'chi2_formatted', 'p_value_formatted', 'or_formatted', 'ci_95', 'significancia']].copy()
    latex_df.columns = ['Análisis', 'Chi²', 'p-valor', 'OR', 'IC 95%', 'Sig.']
    
    return latex_df

def generate_summary_statistics(results_df, top_10):
    """Genera estadísticas resumen"""
    
    stats = {
        'total_resultados_significativos': len(results_df),
        'p_value_minimo': results_df['p_value'].min(),
        'p_value_maximo': results_df['p_value'].max(),
        'or_minimo': results_df['odds_ratio'].min(),
        'or_maximo': results_df['odds_ratio'].max(),
        'chi2_minimo': results_df['chi2'].min(),
        'chi2_maximo': results_df['chi2'].max(),
        'dominios_representados': results_df['dominio'].nunique(),
        'tipos_analisis': results_df['tipo_analisis'].nunique()
    }
    
    return stats

def main():
    """Función principal"""
    
    print("🔬 ANÁLISIS TOP 10 RESULTADOS MÁS SIGNIFICATIVOS")
    print("=" * 60)
    
    # Cargar datos
    print("📊 Cargando datos estadísticos...")
    or_21_cat, chi2_21_cat, chi2_grupos = load_data()
    
    # Extraer resultados significativos
    print("🔍 Extrayendo resultados significativos...")
    results_df = extract_significant_results(or_21_cat, chi2_21_cat, chi2_grupos)
    
    # Crear top 10
    print("🏆 Identificando top 10 resultados más significativos...")
    top_10 = create_top_10_table(results_df)
    
    # Generar estadísticas resumen
    stats = generate_summary_statistics(results_df, top_10)
    
    # Mostrar resultados
    print(f"\n📈 RESUMEN ESTADÍSTICO")
    print(f"Total de resultados significativos analizados: {stats['total_resultados_significativos']}")
    print(f"P-valor mínimo encontrado: {stats['p_value_minimo']:.2e}")
    print(f"P-valor máximo en top 10: {top_10['p_value'].max():.2e}")
    print(f"Dominios representados: {stats['dominios_representados']}")
    
    print(f"\n🏅 TOP 10 RESULTADOS MÁS SIGNIFICATIVOS")
    print("=" * 80)
    
    for i, (_, row) in enumerate(top_10.iterrows(), 1):
        print(f"\n{i}. {row['descripcion']}")
        print(f"   Chi²: {row['chi2_formatted']} | p-valor: {row['p_value_formatted']} {row['significancia']}")
        print(f"   OR: {row['or_formatted']} | IC 95%: {row['ci_95']}")
        print(f"   Tipo: {row['tipo_analisis']}")
    
    # Guardar tablas
    print(f"\n💾 Guardando resultados...")
    
    # Tabla completa del top 10
    top_10_clean = top_10[['descripcion', 'tipo_analisis', 'dominio', 'edad_meses', 
                          'chi2_formatted', 'p_value_formatted', 'or_formatted', 
                          'ci_95', 'significancia']].copy()
    top_10_clean.columns = ['Descripción', 'Tipo_Análisis', 'Dominio', 'Edad_Meses',
                           'Chi²', 'p-valor', 'OR', 'IC_95%', 'Significancia']
    
    top_10_clean.to_csv('top_10_resultados_mas_significativos.csv', index=False)
    
    # Tabla para LaTeX
    latex_table = format_for_latex(top_10)
    latex_table.to_csv('tabla_latex_top_10_significativos.csv', index=False)
    
    # Tabla con todos los resultados significativos
    all_results = results_df.copy()
    all_results['p_value_formatted'] = all_results['p_value'].apply(lambda x: f"{x:.2e}" if x < 0.001 else f"{x:.3f}")
    all_results['chi2_formatted'] = all_results['chi2'].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "N/A")
    all_results['or_formatted'] = all_results['odds_ratio'].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "N/A")
    all_results.to_csv('todos_resultados_significativos.csv', index=False)
    
    print("✅ Archivos generados:")
    print("   - top_10_resultados_mas_significativos.csv")
    print("   - tabla_latex_top_10_significativos.csv") 
    print("   - todos_resultados_significativos.csv")
    
    # Análisis de patrones
    print(f"\n📋 ANÁLISIS DE PATRONES EN TOP 10")
    print("=" * 50)
    
    # Dominios más representados
    dominio_counts = top_10['dominio'].value_counts()
    print(f"\nDominios más representados en top 10:")
    for dominio, count in dominio_counts.items():
        print(f"   {dominio}: {count} resultados")
    
    # Tipos de análisis más representados
    tipo_counts = top_10['tipo_analisis'].value_counts()
    print(f"\nTipos de análisis más representados:")
    for tipo, count in tipo_counts.items():
        print(f"   {tipo}: {count} resultados")
    
    # Edades específicas en top 10 (solo para análisis OR)
    or_results = top_10[top_10['tipo_analisis'] == 'OR Edad-Específico']
    if len(or_results) > 0:
        print(f"\nEdades específicas con mayor significancia:")
        edad_counts = or_results['edad_meses'].value_counts()
        for edad, count in edad_counts.items():
            print(f"   {edad} meses: {count} resultado(s)")
    
    print(f"\n🎯 INTERPRETACIÓN CLÍNICA")
    print("=" * 40)
    print("*** p < 0.001 (altamente significativo)")
    print("**  p < 0.01 (muy significativo)")  
    print("*   p < 0.05 (significativo)")
    print(f"\nLos resultados muestran las asociaciones estadísticamente más fuertes")
    print(f"entre edad y riesgo neurodevelopmental en la muestra analizada.")

if __name__ == "__main__":
    main()