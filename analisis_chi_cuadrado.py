#!/usr/bin/env python3
"""
Análisis de chi-cuadrado para identificar poblaciones en riesgo de trastornos del neurodesarrollo

Este script realiza análisis de chi-cuadrado para identificar qué poblaciones presentan
mayor riesgo de trastornos del neurodesarrollo, con interpretaciones enfocadas en
la identificación de grupos vulnerables.
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple, List

def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    """Carga los datos desde el archivo CSV"""
    return pd.read_csv(ruta_archivo)

def categorizar_desarrollo(zscore: float) -> str:
    """
    Categoriza el desarrollo según el z-score
    
    Args:
        zscore: Z-score del desarrollo
        
    Returns:
        Categoría de desarrollo
    """
    if zscore < -2:
        return "Alto riesgo"
    elif zscore < -1:
        return "Riesgo de trastorno"
    else:
        return "Sin riesgo"

def aplicar_categorizacion_desarrollo(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica la categorización de desarrollo a todos los dominios"""
    dominios = [
        'zscore_desarrollo_comunicacion',
        'zscore_desarrollo_motricidad_gruesa',
        'zscore_desarrollo_motricidad_fina',
        'zscore_desarrollo_resolucion_problemas',
        'zscore_desarrollo_socio_individual'
    ]
    
    for dominio in dominios:
        cat_nombre = dominio.replace('zscore_desarrollo_', 'cat_desarrollo_')
        df[cat_nombre] = df[dominio].apply(categorizar_desarrollo)
    
    return df

def calcular_chi_cuadrado(df: pd.DataFrame, var_independiente: str, var_dependiente: str) -> Dict:
    """
    Calcula chi-cuadrado y devuelve resultados detallados
    
    Args:
        df: DataFrame con los datos
        var_independiente: Variable independiente (ej. 'area_residencia')
        var_dependiente: Variable dependiente (ej. 'cat_desarrollo_comunicacion')
        
    Returns:
        Diccionario con resultados del análisis
    """
    # Crear tabla de contingencia
    tabla_contingencia = pd.crosstab(df[var_independiente], df[var_dependiente])
    
    # Calcular chi-cuadrado
    chi2, p_valor, dof, expected = chi2_contingency(tabla_contingencia)
    
    # Calcular porcentajes por fila
    porcentajes = pd.crosstab(df[var_independiente], df[var_dependiente], normalize='index') * 100
    
    # Calcular riesgo combinado (Alto riesgo + Riesgo de trastorno)
    riesgo_combinado = {}
    for grupo in porcentajes.index:
        alto_riesgo = porcentajes.loc[grupo, 'Alto riesgo'] if 'Alto riesgo' in porcentajes.columns else 0
        riesgo_trastorno = porcentajes.loc[grupo, 'Riesgo de trastorno'] if 'Riesgo de trastorno' in porcentajes.columns else 0
        riesgo_combinado[grupo] = alto_riesgo + riesgo_trastorno
    
    return {
        'chi2': chi2,
        'p_valor': p_valor,
        'dof': dof,
        'tabla_contingencia': tabla_contingencia,
        'porcentajes': porcentajes,
        'riesgo_combinado': riesgo_combinado
    }

def generar_interpretacion_mejorada(var_independiente: str, var_dependiente: str, 
                                   resultados: Dict) -> str:
    """
    Genera interpretación mejorada enfocada en identificar poblaciones de mayor riesgo
    
    Args:
        var_independiente: Variable independiente
        var_dependiente: Variable dependiente
        resultados: Resultados del análisis chi-cuadrado
        
    Returns:
        Interpretación mejorada como string
    """
    chi2 = resultados['chi2']
    p_valor = resultados['p_valor']
    porcentajes = resultados['porcentajes']
    riesgo_combinado = resultados['riesgo_combinado']
    
    # Determinar dominio del desarrollo
    dominio_map = {
        'cat_desarrollo_comunicacion': 'desarrollo de comunicación',
        'cat_desarrollo_motricidad_gruesa': 'desarrollo de motricidad gruesa',
        'cat_desarrollo_motricidad_fina': 'desarrollo de motricidad fina',
        'cat_desarrollo_resolucion_problemas': 'desarrollo de resolución de problemas',
        'cat_desarrollo_socio_individual': 'desarrollo socio-individual'
    }
    
    dominio = dominio_map.get(var_dependiente, var_dependiente)
    
    # Identificar grupo de mayor riesgo
    grupo_mayor_riesgo = max(riesgo_combinado.keys(), key=lambda k: riesgo_combinado[k])
    grupos_ordenados = sorted(riesgo_combinado.items(), key=lambda x: x[1], reverse=True)
    
    # Generar interpretación
    interpretacion = f"""
**Interpretación:**
La asociación entre {var_independiente} y {dominio} {'ES ESTADÍSTICAMENTE SIGNIFICATIVA' if p_valor < 0.05 else 'NO ES ESTADÍSTICAMENTE SIGNIFICATIVA'} (χ² = {chi2:.3f}, p = {p_valor:.3f}).

**Análisis detallado:**"""
    
    if p_valor < 0.05:
        riesgo_mayor = riesgo_combinado[grupo_mayor_riesgo]
        grupo_menor_riesgo = min(riesgo_combinado.keys(), key=lambda k: riesgo_combinado[k])
        riesgo_menor = riesgo_combinado[grupo_menor_riesgo]
        diferencia = riesgo_mayor - riesgo_menor
        
        interpretacion += f"""
- {grupo_mayor_riesgo} presenta mayor riesgo de trastornos del neurodesarrollo en {dominio}
- Riesgo combinado: {grupo_mayor_riesgo} {riesgo_mayor:.1f}% vs {grupo_menor_riesgo} {riesgo_menor:.1f}% (diferencia de {diferencia:.1f}%)"""
        
        # Identificar la categoría específica que más contribuye
        if 'Alto riesgo' in porcentajes.columns:
            alto_riesgo_mayor = porcentajes.loc[grupo_mayor_riesgo, 'Alto riesgo']
            alto_riesgo_menor = porcentajes.loc[grupo_menor_riesgo, 'Alto riesgo']
            if alto_riesgo_mayor > alto_riesgo_menor:
                interpretacion += f"""
- Esta diferencia se debe principalmente a mayor "Alto riesgo" en {grupo_mayor_riesgo} ({alto_riesgo_mayor:.1f}% vs {alto_riesgo_menor:.1f}%, diferencia de {alto_riesgo_mayor - alto_riesgo_menor:.1f}%)"""
        
        if 'Riesgo de trastorno' in porcentajes.columns:
            riesgo_trastorno_mayor = porcentajes.loc[grupo_mayor_riesgo, 'Riesgo de trastorno']
            riesgo_trastorno_menor = porcentajes.loc[grupo_menor_riesgo, 'Riesgo de trastorno']
            if riesgo_trastorno_mayor > riesgo_trastorno_menor:
                interpretacion += f"""
- También hay mayor "Riesgo de trastorno" en {grupo_mayor_riesgo} ({riesgo_trastorno_mayor:.1f}% vs {riesgo_trastorno_menor:.1f}%, diferencia de {riesgo_trastorno_mayor - riesgo_trastorno_menor:.1f}%)"""
        
        # Calcular ratio de riesgo
        if riesgo_menor > 0:
            ratio_riesgo = riesgo_mayor / riesgo_menor
            interpretacion += f"""

**Conclusión clínica:**
Los niños en {grupo_mayor_riesgo} tienen aproximadamente {ratio_riesgo:.1f} veces mayor probabilidad de presentar algún nivel de riesgo en el {dominio} comparado con {grupo_menor_riesgo}."""
        else:
            interpretacion += f"""

**Conclusión clínica:**
Los niños en {grupo_mayor_riesgo} presentan riesgo sustancialmente mayor en el {dominio}, mientras que {grupo_menor_riesgo} no presenta riesgo significativo."""
    
    else:
        interpretacion += f"""
- No se encontraron diferencias estadísticamente significativas entre los grupos
- Los riesgos combinados son similares entre grupos: {' vs '.join([f'{k} {v:.1f}%' for k, v in grupos_ordenados])}

**Conclusión clínica:**
No hay evidencia de diferencias significativas en el riesgo de trastornos del neurodesarrollo en {dominio} entre los grupos de {var_independiente}."""
    
    return interpretacion

def analizar_area_residencia(df: pd.DataFrame) -> str:
    """Analiza el riesgo por área de residencia"""
    resultados_texto = "\n# ANÁLISIS POR ÁREA DE RESIDENCIA\n"
    
    dominios = [
        'cat_desarrollo_comunicacion',
        'cat_desarrollo_motricidad_gruesa', 
        'cat_desarrollo_motricidad_fina',
        'cat_desarrollo_resolucion_problemas',
        'cat_desarrollo_socio_individual'
    ]
    
    for dominio in dominios:
        resultados = calcular_chi_cuadrado(df, 'area_residencia', dominio)
        interpretacion = generar_interpretacion_mejorada('area_residencia', dominio, resultados)
        resultados_texto += f"\n## {dominio.replace('cat_desarrollo_', '').upper()}\n"
        resultados_texto += interpretacion + "\n"
    
    return resultados_texto

def analizar_grupo_etnico(df: pd.DataFrame) -> str:
    """Analiza el riesgo por grupo étnico"""
    resultados_texto = "\n# ANÁLISIS POR GRUPO ÉTNICO\n"
    
    dominios = [
        'cat_desarrollo_comunicacion',
        'cat_desarrollo_motricidad_gruesa',
        'cat_desarrollo_motricidad_fina', 
        'cat_desarrollo_resolucion_problemas',
        'cat_desarrollo_socio_individual'
    ]
    
    for dominio in dominios:
        resultados = calcular_chi_cuadrado(df, 'grupo_etnico', dominio)
        interpretacion = generar_interpretacion_mejorada('grupo_etnico', dominio, resultados)
        resultados_texto += f"\n## {dominio.replace('cat_desarrollo_', '').upper()}\n"
        resultados_texto += interpretacion + "\n"
    
    return resultados_texto

def analizar_nivel_educativo_madre(df: pd.DataFrame) -> str:
    """Analiza el riesgo por nivel educativo de la madre"""
    resultados_texto = "\n# ANÁLISIS POR NIVEL EDUCATIVO DE LA MADRE\n"
    
    dominios = [
        'cat_desarrollo_comunicacion',
        'cat_desarrollo_motricidad_gruesa',
        'cat_desarrollo_motricidad_fina',
        'cat_desarrollo_resolucion_problemas', 
        'cat_desarrollo_socio_individual'
    ]
    
    for dominio in dominios:
        resultados = calcular_chi_cuadrado(df, 'nivel_educativo_madre', dominio)
        interpretacion = generar_interpretacion_mejorada('nivel_educativo_madre', dominio, resultados)
        resultados_texto += f"\n## {dominio.replace('cat_desarrollo_', '').upper()}\n"
        resultados_texto += interpretacion + "\n"
    
    return resultados_texto

def main():
    """Función principal que ejecuta todos los análisis"""
    # Cargar datos
    df = cargar_datos('datos_optimizados.csv')
    
    # Aplicar categorización de desarrollo
    df = aplicar_categorizacion_desarrollo(df)
    
    # Generar análisis completo
    resultados_completos = ""
    resultados_completos += "# ANÁLISIS DE CHI-CUADRADO PARA IDENTIFICACIÓN DE POBLACIONES EN RIESGO\n"
    resultados_completos += "# DE TRASTORNOS DEL NEURODESARROLLO\n\n"
    
    # Análisis por área de residencia
    resultados_completos += analizar_area_residencia(df)
    
    # Análisis por grupo étnico
    resultados_completos += analizar_grupo_etnico(df)
    
    # Análisis por nivel educativo de la madre
    resultados_completos += analizar_nivel_educativo_madre(df)
    
    # Guardar resultados
    with open('resultados_analisis_chi_cuadrado.md', 'w', encoding='utf-8') as f:
        f.write(resultados_completos)
    
    print("Análisis completado. Resultados guardados en 'resultados_analisis_chi_cuadrado.md'")
    
    return resultados_completos

if __name__ == "__main__":
    main()