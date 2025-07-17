"""
Análisis exhaustivo de chi-cuadrado para evaluar asociaciones entre variables categóricas 
y los dominios del neurodesarrollo.

Este script realiza un análisis completo de chi-cuadrado siguiendo los requerimientos específicos:
1. Manejo adecuado de datos faltantes (ignorar completamente)
2. Generación de tablas completas para TODAS las asociaciones
3. Interpretación en español de cada resultado
4. Categorización de riesgo basada en z-scores
5. Análisis de los 5 dominios del neurodesarrollo
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

class AnalisisChiCuadrado:
    
    def __init__(self, archivo_datos):
        """
        Inicializa el análisis con los datos proporcionados.
        
        Args:
            archivo_datos (str): Ruta al archivo CSV con los datos
        """
        self.df = pd.read_csv(archivo_datos)
        
        # Definir los dominios del neurodesarrollo
        self.dominios_neurodesarrollo = [
            'zscore_desarrollo_comunicacion',
            'zscore_desarrollo_motricidad_gruesa',
            'zscore_desarrollo_motricidad_fina',
            'zscore_desarrollo_resolucion_problemas',
            'zscore_desarrollo_socio_individual'
        ]
        
        # Nombres descriptivos para los dominios
        self.nombres_dominios = {
            'zscore_desarrollo_comunicacion': 'Comunicación',
            'zscore_desarrollo_motricidad_gruesa': 'Motricidad Gruesa',
            'zscore_desarrollo_motricidad_fina': 'Motricidad Fina',
            'zscore_desarrollo_resolucion_problemas': 'Resolución de Problemas',
            'zscore_desarrollo_socio_individual': 'Desarrollo Socio-Individual'
        }
        
        # Identificar variables categóricas
        self.variables_categoricas = self._identificar_variables_categoricas()
        
        # Crear categorías de riesgo
        self._crear_categorias_riesgo()
    
    def _identificar_variables_categoricas(self):
        """
        Identifica todas las variables categóricas en el dataset.
        
        Returns:
            list: Lista de nombres de variables categóricas
        """
        categoricas = []
        
        for col in self.df.columns:
            if col not in self.dominios_neurodesarrollo:
                # Considerar como categórica si es object, bool, o tiene pocos valores únicos
                if (self.df[col].dtype == 'object' or 
                    self.df[col].dtype == 'bool' or
                    (self.df[col].dtype in ['int64', 'float64'] and 
                     self.df[col].nunique() < 20)):  # Menos de 20 valores únicos
                    categoricas.append(col)
        
        return categoricas
    
    def _crear_categorias_riesgo(self):
        """
        Crea categorías de riesgo para cada dominio del neurodesarrollo.
        
        Categorías:
        - Desarrollo adecuado: Z ≥ -1
        - Riesgo de trastornos: -2 ≤ Z < -1
        - Alto riesgo: Z < -2
        """
        for dominio in self.dominios_neurodesarrollo:
            nombre_categoria = f"{dominio}_categoria"
            
            # Crear categorías basadas en z-scores
            condiciones = [
                self.df[dominio] >= -1,
                (self.df[dominio] >= -2) & (self.df[dominio] < -1),
                self.df[dominio] < -2
            ]
            
            categorias = [
                'Desarrollo adecuado',
                'Riesgo de trastornos',
                'Alto riesgo'
            ]
            
            self.df[nombre_categoria] = np.select(condiciones, categorias, default=None)
    
    def _crear_tabla_contingencia(self, variable_categorica, dominio_riesgo):
        """
        Crea una tabla de contingencia entre una variable categórica y un dominio de riesgo.
        
        Args:
            variable_categorica (str): Nombre de la variable categórica
            dominio_riesgo (str): Nombre de la variable de riesgo del dominio
            
        Returns:
            tuple: (tabla_contingencia, tabla_porcentajes)
        """
        # Eliminar filas con valores faltantes
        datos_limpios = self.df[[variable_categorica, dominio_riesgo]].dropna()
        
        if len(datos_limpios) == 0:
            return None, None
        
        # Crear tabla de contingencia
        tabla_contingencia = pd.crosstab(
            datos_limpios[variable_categorica], 
            datos_limpios[dominio_riesgo],
            margins=True
        )
        
        # Crear tabla de porcentajes
        tabla_porcentajes = pd.crosstab(
            datos_limpios[variable_categorica], 
            datos_limpios[dominio_riesgo],
            normalize='index'
        ) * 100
        
        return tabla_contingencia, tabla_porcentajes
    
    def _calcular_chi_cuadrado(self, tabla_contingencia):
        """
        Calcula el estadístico chi-cuadrado y el valor p.
        
        Args:
            tabla_contingencia (DataFrame): Tabla de contingencia
            
        Returns:
            tuple: (chi2, p_valor, grados_libertad)
        """
        # Excluir fila y columna de totales
        tabla_sin_totales = tabla_contingencia.iloc[:-1, :-1]
        
        if tabla_sin_totales.shape[0] < 2 or tabla_sin_totales.shape[1] < 2:
            return None, None, None
        
        try:
            chi2, p_valor, dof, expected = chi2_contingency(tabla_sin_totales)
            return chi2, p_valor, dof
        except:
            return None, None, None
    
    def _interpretar_asociacion(self, variable, dominio, chi2, p_valor, tabla_contingencia, tabla_porcentajes):
        """
        Genera una interpretación en español de la asociación.
        
        Args:
            variable (str): Nombre de la variable categórica
            dominio (str): Nombre del dominio
            chi2 (float): Estadístico chi-cuadrado
            p_valor (float): Valor p
            tabla_contingencia (DataFrame): Tabla de contingencia
            tabla_porcentajes (DataFrame): Tabla de porcentajes
            
        Returns:
            str: Interpretación en español
        """
        nombre_dominio = self.nombres_dominios.get(dominio, dominio)
        
        # Determinar si es significativa
        es_significativa = p_valor < 0.05 if p_valor is not None else False
        
        interpretacion = f"\n**Interpretación:**\n"
        
        if chi2 is None or p_valor is None:
            interpretacion += f"No se pudo calcular el estadístico chi-cuadrado para la asociación entre {variable} y {nombre_dominio}."
            return interpretacion
        
        if es_significativa:
            interpretacion += f"La asociación entre {variable} y desarrollo de {nombre_dominio} **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = {chi2:.3f}, p = {p_valor:.3f}).\n\n"
            
            # Analizar qué categorías tienen mayor riesgo
            if tabla_porcentajes is not None:
                interpretacion += "**Análisis por categorías:**\n"
                
                # Buscar la categoría con mayor proporción de alto riesgo
                if 'Alto riesgo' in tabla_porcentajes.columns:
                    categoria_mayor_riesgo = tabla_porcentajes['Alto riesgo'].idxmax()
                    porcentaje_mayor_riesgo = tabla_porcentajes.loc[categoria_mayor_riesgo, 'Alto riesgo']
                    
                    interpretacion += f"- **{categoria_mayor_riesgo}** muestra la mayor proporción de alto riesgo ({porcentaje_mayor_riesgo:.1f}%)\n"
                
                # Buscar la categoría con mayor proporción de desarrollo adecuado
                if 'Desarrollo adecuado' in tabla_porcentajes.columns:
                    categoria_mejor_desarrollo = tabla_porcentajes['Desarrollo adecuado'].idxmax()
                    porcentaje_mejor_desarrollo = tabla_porcentajes.loc[categoria_mejor_desarrollo, 'Desarrollo adecuado']
                    
                    interpretacion += f"- **{categoria_mejor_desarrollo}** muestra la mayor proporción de desarrollo adecuado ({porcentaje_mejor_desarrollo:.1f}%)\n"
        
        else:
            interpretacion += f"La asociación entre {variable} y desarrollo de {nombre_dominio} **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = {chi2:.3f}, p = {p_valor:.3f}).\n"
            interpretacion += "No se puede concluir que exista una asociación significativa entre estas variables.\n"
        
        return interpretacion
    
    def _formatear_tabla_completa(self, tabla_contingencia, tabla_porcentajes):
        """
        Formatea las tablas de contingencia y porcentajes para mostrar juntas.
        
        Args:
            tabla_contingencia (DataFrame): Tabla de contingencia
            tabla_porcentajes (DataFrame): Tabla de porcentajes
            
        Returns:
            str: Tabla formateada
        """
        if tabla_contingencia is None or tabla_porcentajes is None:
            return "No se pudo generar la tabla de contingencia (datos insuficientes)."
        
        resultado = "\n**Tabla de Contingencia (Conteos absolutos):**\n"
        resultado += tabla_contingencia.to_string()
        
        resultado += "\n\n**Tabla de Porcentajes (% por fila):**\n"
        # Formatear porcentajes con una decimal
        tabla_porcentajes_formateada = tabla_porcentajes.round(1)
        resultado += tabla_porcentajes_formateada.to_string()
        
        return resultado
    
    def analizar_variable_dominio(self, variable, dominio):
        """
        Analiza la asociación entre una variable categórica y un dominio del neurodesarrollo.
        
        Args:
            variable (str): Nombre de la variable categórica
            dominio (str): Nombre del dominio del neurodesarrollo
            
        Returns:
            str: Análisis completo formateado
        """
        nombre_dominio = self.nombres_dominios.get(dominio, dominio)
        dominio_riesgo = f"{dominio}_categoria"
        
        resultado = f"\n#### {nombre_dominio}\n"
        
        # Crear tabla de contingencia
        tabla_contingencia, tabla_porcentajes = self._crear_tabla_contingencia(variable, dominio_riesgo)
        
        # Mostrar las tablas
        resultado += self._formatear_tabla_completa(tabla_contingencia, tabla_porcentajes)
        
        # Calcular estadísticos
        chi2, p_valor, dof = self._calcular_chi_cuadrado(tabla_contingencia)
        
        # Añadir estadísticos
        if chi2 is not None and p_valor is not None:
            resultado += f"\n\n**Estadísticos:**\n"
            resultado += f"- Chi-cuadrado: {chi2:.3f}\n"
            resultado += f"- Valor p: {p_valor:.3f}\n"
            resultado += f"- Grados de libertad: {dof}\n"
        
        # Añadir interpretación
        resultado += self._interpretar_asociacion(variable, dominio, chi2, p_valor, tabla_contingencia, tabla_porcentajes)
        
        return resultado
    
    def analizar_variable_completa(self, variable):
        """
        Analiza una variable categórica contra todos los dominios del neurodesarrollo.
        
        Args:
            variable (str): Nombre de la variable categórica
            
        Returns:
            str: Análisis completo de la variable
        """
        resultado = f"\n### Variable: {variable}\n"
        resultado += "="*50 + "\n"
        
        # Información básica de la variable
        valores_unicos = self.df[variable].value_counts().head(10)
        resultado += f"\n**Distribución de la variable {variable}:**\n"
        for categoria, count in valores_unicos.items():
            porcentaje = (count / len(self.df)) * 100
            resultado += f"- {categoria}: {count} ({porcentaje:.1f}%)\n"
        
        # Analizar contra cada dominio
        for dominio in self.dominios_neurodesarrollo:
            resultado += self.analizar_variable_dominio(variable, dominio)
            resultado += "\n" + "-"*80 + "\n"
        
        return resultado
    
    def ejecutar_analisis_completo(self):
        """
        Ejecuta el análisis completo para todas las variables categóricas.
        
        Returns:
            str: Reporte completo del análisis
        """
        reporte = "# ANÁLISIS EXHAUSTIVO DE CHI-CUADRADO\n"
        reporte += "## Asociaciones entre Variables Categóricas y Dominios del Neurodesarrollo\n"
        reporte += "="*80 + "\n\n"
        
        # Información general
        reporte += f"**Dataset:** {len(self.df)} observaciones, {len(self.df.columns)} variables\n"
        reporte += f"**Variables categóricas analizadas:** {len(self.variables_categoricas)}\n"
        reporte += f"**Dominios del neurodesarrollo:** {len(self.dominios_neurodesarrollo)}\n\n"
        
        # Criterios de categorización
        reporte += "**Criterios de categorización de riesgo:**\n"
        reporte += "- Desarrollo adecuado: Z ≥ -1\n"
        reporte += "- Riesgo de trastornos: -2 ≤ Z < -1\n"
        reporte += "- Alto riesgo: Z < -2\n\n"
        
        reporte += "**Nota:** Se ignoran completamente los valores faltantes en todos los análisis.\n\n"
        
        # Analizar cada variable categórica
        for i, variable in enumerate(self.variables_categoricas, 1):
            reporte += f"\n\n## {i}. ANÁLISIS DE LA VARIABLE: {variable.upper()}\n"
            reporte += self.analizar_variable_completa(variable)
        
        return reporte
    
    def guardar_reporte(self, nombre_archivo="reporte_chi_cuadrado.md"):
        """
        Guarda el reporte completo en un archivo Markdown.
        
        Args:
            nombre_archivo (str): Nombre del archivo donde guardar el reporte
        """
        reporte = self.ejecutar_analisis_completo()
        
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(reporte)
        
        print(f"Reporte guardado en: {nombre_archivo}")
        return nombre_archivo

def main():
    """
    Función principal que ejecuta el análisis completo.
    """
    print("Iniciando análisis exhaustivo de chi-cuadrado...")
    
    # Crear instancia del análisis
    analisis = AnalisisChiCuadrado('datos_optimizados.csv')
    
    print(f"Variables categóricas identificadas: {len(analisis.variables_categoricas)}")
    print(f"Dominios del neurodesarrollo: {len(analisis.dominios_neurodesarrollo)}")
    
    # Ejecutar y guardar el análisis
    nombre_archivo = analisis.guardar_reporte()
    
    print(f"\nAnálisis completado. Reporte guardado en: {nombre_archivo}")
    
    # Mostrar resumen de las primeras variables
    print("\nPrimeras 5 variables categóricas a analizar:")
    for i, var in enumerate(analisis.variables_categoricas[:5], 1):
        print(f"{i}. {var}")

if __name__ == "__main__":
    main()