#!/usr/bin/env python3
"""
Generador de resumen de hallazgos significativos del análisis chi-cuadrado
"""

import pandas as pd
import re

def extraer_resultados_significativos(archivo_analisis):
    """Extraer resultados significativos del análisis completo"""
    
    with open(archivo_analisis, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Buscar patrones de resultados significativos
    patron_significativo = r'### Variable: (.+?) vs Dominio: (.+?)\n\n\*\*Interpretación:\*\*\nLa asociación entre (.+?) y (.+?) ES ESTADÍSTICAMENTE SIGNIFICATIVA \((.+?)\)\.'
    
    resultados = re.findall(patron_significativo, contenido)
    
    # Buscar estadísticos
    patron_estadisticos = r'- Test: (.+?)\n(?:- χ² = (.+?)\n)?- p-value = (.+?)\n'
    estadisticos = re.findall(patron_estadisticos, contenido)
    
    return resultados, estadisticos

def generar_resumen_hallazgos():
    """Generar resumen de hallazgos significativos"""
    
    print("Generando resumen de hallazgos significativos...")
    
    # Leer el archivo de análisis
    try:
        resultados, estadisticos = extraer_resultados_significativos("analisis_chi_cuadrado_completo.txt")
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo de análisis")
        return
    
    # Crear archivo de resumen
    archivo_resumen = "resumen_hallazgos_significativos.txt"
    
    with open(archivo_resumen, 'w', encoding='utf-8') as f:
        f.write("# RESUMEN DE HALLAZGOS SIGNIFICATIVOS\n")
        f.write("# Análisis Chi-Cuadrado: Variables Categóricas vs Neurodesarrollo\n\n")
        
        f.write("## RESUMEN EJECUTIVO\n")
        f.write("=" * 60 + "\n")
        f.write(f"- **Total de análisis realizados**: 240 combinaciones\n")
        f.write(f"- **Asociaciones estadísticamente significativas**: {len(resultados)}\n")
        f.write(f"- **Porcentaje de significancia**: {len(resultados)/240*100:.1f}%\n\n")
        
        f.write("## VARIABLES CON MAYOR NÚMERO DE ASOCIACIONES SIGNIFICATIVAS\n")
        f.write("=" * 60 + "\n")
        
        # Contar por variable
        conteo_variables = {}
        for resultado in resultados:
            variable = resultado[0]
            if variable in conteo_variables:
                conteo_variables[variable] += 1
            else:
                conteo_variables[variable] = 1
        
        # Ordenar por número de asociaciones significativas
        variables_ordenadas = sorted(conteo_variables.items(), key=lambda x: x[1], reverse=True)
        
        for i, (variable, count) in enumerate(variables_ordenadas[:10], 1):
            f.write(f"{i}. **{variable}**: {count} dominios afectados\n")
        
        f.write("\n")
        
        f.write("## DOMINIOS CON MAYOR NÚMERO DE ASOCIACIONES SIGNIFICATIVAS\n")
        f.write("=" * 60 + "\n")
        
        # Contar por dominio
        conteo_dominios = {}
        for resultado in resultados:
            dominio = resultado[1]
            if dominio in conteo_dominios:
                conteo_dominios[dominio] += 1
            else:
                conteo_dominios[dominio] = 1
        
        # Ordenar por número de asociaciones significativas
        dominios_ordenados = sorted(conteo_dominios.items(), key=lambda x: x[1], reverse=True)
        
        for i, (dominio, count) in enumerate(dominios_ordenados, 1):
            f.write(f"{i}. **{dominio}**: {count} variables asociadas\n")
        
        f.write("\n")
        
        f.write("## INTERPRETACIÓN CLÍNICA GENERAL\n")
        f.write("=" * 60 + "\n")
        
        f.write("### Factores de Mayor Riesgo Identificados:\n\n")
        
        # Variables más críticas
        variables_criticas = [var for var, count in variables_ordenadas[:5]]
        
        for variable in variables_criticas:
            f.write(f"**{variable}**:\n")
            f.write(f"- Asociada significativamente con {conteo_variables[variable]} dominios del neurodesarrollo\n")
            f.write(f"- Requiere intervención prioritaria y seguimiento especializado\n\n")
        
        f.write("### Dominios más Vulnerables:\n\n")
        
        # Dominios más afectados
        dominios_criticos = [dom for dom, count in dominios_ordenados[:3]]
        
        for dominio in dominios_criticos:
            f.write(f"**{dominio}**:\n")
            f.write(f"- Afectado por {conteo_dominios[dominio]} variables categóricas diferentes\n")
            f.write(f"- Requiere programas de intervención temprana específicos\n\n")
        
        f.write("## RECOMENDACIONES PARA SALUD PÚBLICA\n")
        f.write("=" * 60 + "\n")
        
        f.write("1. **Priorización de Intervenciones**:\n")
        f.write("   - Enfocar recursos en las variables con mayor número de asociaciones\n")
        f.write("   - Implementar programas específicos para cada dominio vulnerable\n\n")
        
        f.write("2. **Monitoreo Continuo**:\n")
        f.write("   - Seguimiento especial para población con factores de riesgo identificados\n")
        f.write("   - Evaluación periódica del desarrollo neurológico\n\n")
        
        f.write("3. **Intervención Temprana**:\n")
        f.write("   - Programas de estimulación temprana dirigidos\n")
        f.write("   - Capacitación a cuidadores y profesionales de salud\n\n")
        
        f.write("## LIMITACIONES DEL ESTUDIO\n")
        f.write("=" * 60 + "\n")
        
        f.write("- Análisis transversal: no establece causalidad\n")
        f.write("- Múltiples comparaciones: posible inflación del error tipo I\n")
        f.write("- Necesidad de validación en estudios longitudinales\n\n")
        
        f.write("---\n")
        f.write("**Para análisis detallado de cada asociación, consultar**: analisis_chi_cuadrado_completo.txt\n")
        f.write("**Metodología completa disponible en**: analisis_chi_cuadrado_completo.py\n")
    
    print(f"Resumen de hallazgos generado en: {archivo_resumen}")
    
    # Mostrar estadísticas básicas
    print(f"\nEstadísticas del análisis:")
    print(f"- Total de análisis: 240")
    print(f"- Asociaciones significativas: {len(resultados)}")
    print(f"- Tasa de significancia: {len(resultados)/240*100:.1f}%")
    print(f"- Variables con más asociaciones: {variables_ordenadas[0][0]} ({variables_ordenadas[0][1]} dominios)")
    print(f"- Dominio más afectado: {dominios_ordenados[0][0]} ({dominios_ordenados[0][1]} variables)")

if __name__ == "__main__":
    generar_resumen_hallazgos()