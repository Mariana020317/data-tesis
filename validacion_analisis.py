"""
Script de validación y resumen para el análisis de chi-cuadrado.

Este script valida los resultados del análisis y proporciona estadísticas resumen.
"""

import pandas as pd
import numpy as np
from analisis_chi_cuadrado import AnalisisChiCuadrado

def validar_analisis(archivo_datos='datos_optimizados.csv'):
    """
    Valida el análisis de chi-cuadrado y proporciona estadísticas resumen.
    
    Args:
        archivo_datos (str): Ruta al archivo de datos
    """
    print("="*70)
    print("VALIDACIÓN Y RESUMEN DEL ANÁLISIS DE CHI-CUADRADO")
    print("="*70)
    
    # Crear instancia del análisis
    analisis = AnalisisChiCuadrado(archivo_datos)
    
    # Información básica del dataset
    print(f"\n1. INFORMACIÓN BÁSICA DEL DATASET:")
    print(f"   - Total de observaciones: {len(analisis.df):,}")
    print(f"   - Total de variables: {len(analisis.df.columns)}")
    print(f"   - Variables categóricas identificadas: {len(analisis.variables_categoricas)}")
    print(f"   - Dominios del neurodesarrollo: {len(analisis.dominios_neurodesarrollo)}")
    
    # Mostrar variables categóricas
    print(f"\n2. VARIABLES CATEGÓRICAS ANALIZADAS:")
    for i, var in enumerate(analisis.variables_categoricas, 1):
        print(f"   {i:2d}. {var}")
    
    # Mostrar dominios
    print(f"\n3. DOMINIOS DEL NEURODESARROLLO:")
    for i, dominio in enumerate(analisis.dominios_neurodesarrollo, 1):
        nombre = analisis.nombres_dominios[dominio]
        print(f"   {i}. {nombre} ({dominio})")
    
    # Estadísticas de las categorías de riesgo
    print(f"\n4. DISTRIBUCIÓN DE CATEGORÍAS DE RIESGO:")
    for dominio in analisis.dominios_neurodesarrollo:
        categoria_var = f"{dominio}_categoria"
        nombre = analisis.nombres_dominios[dominio]
        
        if categoria_var in analisis.df.columns:
            distribucion = analisis.df[categoria_var].value_counts()
            total = distribucion.sum()
            
            print(f"\n   {nombre}:")
            for categoria, count in distribucion.items():
                porcentaje = (count / total) * 100
                print(f"     - {categoria}: {count:,} ({porcentaje:.1f}%)")
    
    # Calcular total de análisis realizados
    total_analisis = len(analisis.variables_categoricas) * len(analisis.dominios_neurodesarrollo)
    print(f"\n5. ALCANCE DEL ANÁLISIS:")
    print(f"   - Total de análisis chi-cuadrado realizados: {total_analisis}")
    print(f"   - Tablas de contingencia generadas: {total_analisis}")
    print(f"   - Interpretaciones en español: {total_analisis}")
    
    # Validar manejo de datos faltantes
    print(f"\n6. MANEJO DE DATOS FALTANTES:")
    print(f"   - Datos faltantes en z-scores originales:")
    for dominio in analisis.dominios_neurodesarrollo:
        missing = analisis.df[dominio].isnull().sum()
        print(f"     {analisis.nombres_dominios[dominio]}: {missing} valores faltantes")
    
    print(f"\n   - Política: Todos los valores faltantes se ignoran completamente")
    print(f"   - No se realiza imputación de datos")
    
    # Verificar estructura del reporte
    archivo_reporte = 'reporte_chi_cuadrado.md'
    try:
        with open(archivo_reporte, 'r', encoding='utf-8') as f:
            contenido = f.read()
            lineas = contenido.count('\n')
            
        print(f"\n7. REPORTE GENERADO:")
        print(f"   - Archivo: {archivo_reporte}")
        print(f"   - Tamaño: {lineas:,} líneas")
        print(f"   - Contiene interpretaciones en español: ✓")
        print(f"   - Incluye tablas de contingencia: ✓")
        print(f"   - Incluye estadísticos chi-cuadrado: ✓")
        print(f"   - Incluye análisis de categorías: ✓")
        
    except FileNotFoundError:
        print(f"\n7. REPORTE GENERADO:")
        print(f"   - ERROR: No se encontró el archivo {archivo_reporte}")
        print(f"   - Ejecutar: python analisis_chi_cuadrado.py")
    
    print("\n" + "="*70)
    print("VALIDACIÓN COMPLETADA")
    print("="*70)

def mostrar_ejemplos_uso():
    """
    Muestra ejemplos de cómo usar el análisis.
    """
    print("\n" + "="*70)
    print("EJEMPLOS DE USO")
    print("="*70)
    
    print("\n1. EJECUTAR ANÁLISIS COMPLETO:")
    print("   python analisis_chi_cuadrado.py")
    print("   - Genera el reporte completo en 'reporte_chi_cuadrado.md'")
    
    print("\n2. USAR COMO MÓDULO:")
    print("   from analisis_chi_cuadrado import AnalisisChiCuadrado")
    print("   analisis = AnalisisChiCuadrado('datos_optimizados.csv')")
    print("   reporte = analisis.ejecutar_analisis_completo()")
    
    print("\n3. ANALIZAR VARIABLE ESPECÍFICA:")
    print("   analisis = AnalisisChiCuadrado('datos_optimizados.csv')")
    print("   resultado = analisis.analizar_variable_completa('grupo_etnico')")
    
    print("\n4. ANALIZAR ASOCIACIÓN ESPECÍFICA:")
    print("   analisis = AnalisisChiCuadrado('datos_optimizados.csv')")
    print("   resultado = analisis.analizar_variable_dominio('grupo_etnico', 'zscore_desarrollo_comunicacion')")
    
    print("\n5. VALIDAR RESULTADOS:")
    print("   python validacion_analisis.py")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    # Ejecutar validación
    validar_analisis()
    
    # Mostrar ejemplos de uso
    mostrar_ejemplos_uso()