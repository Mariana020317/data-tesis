#!/usr/bin/env python3
"""
Análisis de los Top 10 Odds Ratios Más Significativos
Enfocado en asociaciones específicas edad-dominio con OR, Chi², p-value y CI
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from pathlib import Path

def load_and_process_data():
    """Carga y procesa los datos para calcular estadísticas completas"""
    
    # Cargar odds ratios de 21 categorías
    or_data = pd.read_csv('odds_ratios_21_categorias_edad.csv')
    
    # Cargar datos originales para calcular chi-square específicos
    data = pd.read_csv('datos_optimizados.csv')
    
    return or_data, data

def calculate_chi_square_for_or(data, edad, dominio):
    """Calcula el chi-square específico para una combinación edad-dominio"""
    
    try:
        # Filtrar datos para la edad específica
        edad_data = data[data['edad_meses'] == edad].copy()
        
        if len(edad_data) == 0:
            return np.nan, np.nan
        
        # Determinar la columna del dominio
        dominio_cols = {
            'Comunicación': 'riesgo_comunicacion',
            'Motricidad Gruesa': 'riesgo_motricidad_gruesa', 
            'Motricidad Fina': 'riesgo_motricidad_fina',
            'Resolución de Problemas': 'riesgo_resolucion_problemas',
            'Desarrollo Socio-Individual': 'riesgo_socio_individual',
            'Riesgo Global': 'riesgo_global'
        }
        
        if dominio not in dominio_cols:
            return np.nan, np.nan
        
        col_riesgo = dominio_cols[dominio]
        
        if col_riesgo not in edad_data.columns:
            return np.nan, np.nan
        
        # Crear tabla de contingencia: edad vs resto, riesgo vs no riesgo
        edad_data['edad_grupo'] = 'Edad_Específica'
        resto_data = data[data['edad_meses'] != edad].copy()
        resto_data['edad_grupo'] = 'Otras_Edades'
        
        combined_data = pd.concat([edad_data, resto_data])
        
        # Tabla de contingencia
        contingency = pd.crosstab(combined_data['edad_grupo'], combined_data[col_riesgo])
        
        if contingency.shape != (2, 2):
            return np.nan, np.nan
        
        # Calcular chi-square
        chi2_stat, p_val, _, _ = chi2_contingency(contingency)
        
        return chi2_stat, p_val
        
    except Exception as e:
        return np.nan, np.nan

def create_comprehensive_table(or_data, data):
    """Crea tabla comprensiva con OR, Chi², p-values y CI"""
    
    results = []
    
    print("📊 Calculando estadísticas chi-square específicas...")
    
    for _, row in or_data.iterrows():
        if row['significativo'] and pd.notna(row['odds_ratio']):
            
            # Calcular chi-square específico para esta combinación
            chi2_stat, chi2_p = calculate_chi_square_for_or(data, row['edad_meses'], row['dominio'])
            
            result = {
                'edad_meses': int(row['edad_meses']),
                'dominio': row['dominio'],
                'descripcion': f"{int(row['edad_meses'])} meses - {row['dominio']}",
                'odds_ratio': row['odds_ratio'],
                'or_p_value': row['p_value'],
                'ci_lower': row['ci_lower'],
                'ci_upper': row['ci_upper'],
                'ci_95': f"({row['ci_lower']:.2f} - {row['ci_upper']:.2f})",
                'chi2_stat': chi2_stat,
                'chi2_p_value': chi2_p,
                'significativo': row['significativo']
            }
            results.append(result)
    
    return pd.DataFrame(results)

def create_top_10_or_table(results_df):
    """Crea la tabla de top 10 OR más significativos"""
    
    # Filtrar solo resultados con OR válidos
    valid_or = results_df[pd.notna(results_df['odds_ratio'])].copy()
    
    # Ordenar por p-value del OR (menor = más significativo)
    top_10 = valid_or.nsmallest(10, 'or_p_value').copy()
    
    # Formatear valores
    top_10['or_formatted'] = top_10['odds_ratio'].apply(lambda x: f"{x:.2f}")
    top_10['or_p_formatted'] = top_10['or_p_value'].apply(lambda x: f"{x:.2e}" if x < 0.001 else f"{x:.3f}")
    top_10['chi2_formatted'] = top_10['chi2_stat'].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "N/A")
    top_10['chi2_p_formatted'] = top_10['chi2_p_value'].apply(lambda x: f"{x:.2e}" if pd.notna(x) and x < 0.001 else f"{x:.3f}" if pd.notna(x) else "N/A")
    
    # Interpretación de significancia
    def interpret_significance(p_val):
        if pd.isna(p_val):
            return ""
        elif p_val < 0.001:
            return "***"
        elif p_val < 0.01:
            return "**"
        elif p_val < 0.05:
            return "*"
        else:
            return ""
    
    top_10['or_sig'] = top_10['or_p_value'].apply(interpret_significance)
    top_10['chi2_sig'] = top_10['chi2_p_value'].apply(interpret_significance)
    
    # Interpretación clínica del OR
    def interpret_or(or_value):
        if pd.isna(or_value):
            return "N/A"
        elif or_value > 3.0:
            return "Riesgo muy alto"
        elif or_value > 2.0:
            return "Riesgo alto"
        elif or_value > 1.5:
            return "Riesgo moderado"
        elif or_value > 1.0:
            return "Riesgo leve"
        elif or_value > 0.67:
            return "Protección leve"
        elif or_value > 0.5:
            return "Protección moderada"
        elif or_value > 0.33:
            return "Protección alta"
        else:
            return "Protección muy alta"
    
    top_10['interpretacion_or'] = top_10['odds_ratio'].apply(interpret_or)
    
    return top_10

def format_publication_table(top_10):
    """Formatea tabla para publicación"""
    
    pub_table = top_10[[
        'descripcion', 'or_formatted', 'ci_95', 'or_p_formatted', 'or_sig',
        'chi2_formatted', 'chi2_p_formatted', 'chi2_sig', 'interpretacion_or'
    ]].copy()
    
    pub_table.columns = [
        'Edad - Dominio', 'OR', 'IC 95%', 'p-valor (OR)', 'Sig. OR',
        'Chi²', 'p-valor (χ²)', 'Sig. χ²', 'Interpretación'
    ]
    
    return pub_table

def analyze_patterns(top_10):
    """Analiza patrones en los resultados"""
    
    patterns = {
        'edades_criticas': top_10['edad_meses'].value_counts().head(3),
        'dominios_criticos': top_10['dominio'].value_counts().head(3),
        'or_promedio': top_10['odds_ratio'].mean(),
        'or_maximo': top_10['odds_ratio'].max(),
        'or_minimo': top_10['odds_ratio'].min(),
        'riesgo_alto_count': len(top_10[top_10['odds_ratio'] > 2.0]),
        'proteccion_count': len(top_10[top_10['odds_ratio'] < 1.0])
    }
    
    return patterns

def main():
    """Función principal"""
    
    print("🏆 ANÁLISIS TOP 10 ODDS RATIOS MÁS SIGNIFICATIVOS")
    print("=" * 70)
    
    # Cargar datos
    print("📊 Cargando datos...")
    or_data, data = load_and_process_data()
    
    # Crear tabla comprensiva
    print("🔬 Procesando análisis estadístico comprensivo...")
    results_df = create_comprehensive_table(or_data, data)
    
    # Crear top 10
    print("🥇 Identificando top 10 OR más significativos...")
    top_10 = create_top_10_or_table(results_df)
    
    # Analizar patrones
    patterns = analyze_patterns(top_10)
    
    # Mostrar resultados
    print(f"\n📈 RESUMEN ESTADÍSTICO")
    print(f"Total de OR significativos analizados: {len(results_df)}")
    print(f"OR p-valor mínimo: {top_10['or_p_value'].min():.2e}")
    print(f"OR máximo en top 10: {patterns['or_maximo']:.2f}")
    print(f"OR mínimo en top 10: {patterns['or_minimo']:.2f}")
    
    print(f"\n🏅 TOP 10 ODDS RATIOS MÁS SIGNIFICATIVOS")
    print("=" * 90)
    
    for i, (_, row) in enumerate(top_10.iterrows(), 1):
        print(f"\n{i:2d}. {row['descripcion']}")
        print(f"     OR: {row['or_formatted']} {row['or_sig']} | IC 95%: {row['ci_95']}")
        print(f"     p-valor (OR): {row['or_p_formatted']} | χ²: {row['chi2_formatted']} (p: {row['chi2_p_formatted']} {row['chi2_sig']})")
        print(f"     Interpretación: {row['interpretacion_or']}")
    
    # Guardar resultados
    print(f"\n💾 Guardando resultados...")
    
    # Tabla principal
    top_10_complete = top_10[[
        'edad_meses', 'dominio', 'descripcion', 'odds_ratio', 'ci_lower', 'ci_upper',
        'ci_95', 'or_p_value', 'chi2_stat', 'chi2_p_value', 'interpretacion_or'
    ]].copy()
    
    top_10_complete.columns = [
        'Edad_Meses', 'Dominio', 'Descripción', 'OR', 'CI_Inferior', 'CI_Superior',
        'IC_95%', 'p_valor_OR', 'Chi²', 'p_valor_Chi²', 'Interpretación_OR'
    ]
    
    top_10_complete.to_csv('top_10_odds_ratios_mas_significativos.csv', index=False)
    
    # Tabla para publicación
    pub_table = format_publication_table(top_10)
    pub_table.to_csv('tabla_publicacion_top_10_or.csv', index=False)
    
    # Tabla LaTeX optimizada
    latex_table = top_10[['descripcion', 'or_formatted', 'ci_95', 'or_p_formatted', 
                         'chi2_formatted', 'interpretacion_or']].copy()
    latex_table.columns = ['Edad - Dominio', 'OR', 'IC 95%', 'p-valor', 'χ²', 'Interpretación']
    latex_table.to_csv('tabla_latex_top_10_or_final.csv', index=False)
    
    print("✅ Archivos generados:")
    print("   - top_10_odds_ratios_mas_significativos.csv")
    print("   - tabla_publicacion_top_10_or.csv")
    print("   - tabla_latex_top_10_or_final.csv")
    
    # Análisis de patrones
    print(f"\n📊 ANÁLISIS DE PATRONES")
    print("=" * 40)
    
    print(f"\nEdades más críticas (top 3):")
    for edad, count in patterns['edades_criticas'].items():
        print(f"   {edad} meses: {count} resultado(s)")
    
    print(f"\nDominios más afectados (top 3):")
    for dominio, count in patterns['dominios_criticos'].items():
        print(f"   {dominio}: {count} resultado(s)")
    
    print(f"\nDistribución de riesgo:")
    print(f"   Riesgo alto (OR > 2.0): {patterns['riesgo_alto_count']} casos")
    print(f"   Efecto protector (OR < 1.0): {patterns['proteccion_count']} casos")
    print(f"   OR promedio: {patterns['or_promedio']:.2f}")
    
    print(f"\n🎯 INTERPRETACIÓN CLÍNICA PRINCIPAL")
    print("=" * 50)
    
    # Identificar el resultado más significativo
    most_sig = top_10.iloc[0]
    print(f"Resultado más significativo:")
    print(f"   {most_sig['descripcion']}")
    print(f"   OR = {most_sig['or_formatted']} {most_sig['ci_95']}")
    print(f"   p = {most_sig['or_p_formatted']} {most_sig['or_sig']}")
    print(f"   {most_sig['interpretacion_or']}")
    
    print(f"\n*** p < 0.001 | ** p < 0.01 | * p < 0.05")

if __name__ == "__main__":
    main()