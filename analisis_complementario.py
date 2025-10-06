#!/usr/bin/env python3
"""
Análisis complementario para variables categóricas múltiples
con interpretaciones específicas para cada categoría
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisisComplementario:
    """
    Análisis complementario para variables con múltiples categorías
    """
    
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)
        self.dominios_desarrollo = [
            'zscore_desarrollo_comunicacion',
            'zscore_desarrollo_motricidad_gruesa', 
            'zscore_desarrollo_motricidad_fina',
            'zscore_desarrollo_resolucion_problemas',
            'zscore_desarrollo_socio_individual'
        ]
        self._categorizar_desarrollo()
    
    def _categorizar_desarrollo(self):
        """Categorizar los z-scores de desarrollo"""
        for dominio in self.dominios_desarrollo:
            categoria_col = dominio.replace('zscore_', 'categoria_')
            self.df[categoria_col] = np.where(
                self.df[dominio] < -1.0,
                'Riesgo combinado',
                'Desarrollo adecuado'
            )
    
    def analizar_nivel_educativo_madre(self):
        """Análisis específico para nivel educativo de la madre"""
        print("=== ANÁLISIS ESPECÍFICO: NIVEL EDUCATIVO DE LA MADRE ===\n")
        
        for dominio in self.dominios_desarrollo:
            categoria_col = dominio.replace('zscore_', 'categoria_')
            dominio_nombre = dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title()
            
            print(f"\n{'='*60}")
            print(f"DOMINIO: {dominio_nombre}")
            print(f"{'='*60}")
            
            # Crear tabla de contingencia
            tabla = pd.crosstab(self.df['nivel_educativo_madre'], self.df[categoria_col])
            
            # Limpiar categorías no especificadas
            if 'No especificado' in tabla.index:
                tabla = tabla.drop('No especificado')
            
            if tabla.shape[0] < 2:
                continue
            
            print(f"\n**Tabla de contingencia:**")
            print(tabla.to_string())
            
            # Test de chi-cuadrado
            chi2, p_valor, dof, expected = chi2_contingency(tabla)
            print(f"\n**Test de chi-cuadrado:**")
            print(f"χ² = {chi2:.2f}, p = {p_valor:.3f}")
            
            if p_valor < 0.05:
                print(f"\n**Interpretación:**")
                print(f"La asociación ES ESTADÍSTICAMENTE SIGNIFICATIVA")
                
                # Calcular proporciones de riesgo por nivel educativo
                self._analizar_proporciones_riesgo(tabla, 'nivel educativo materno', dominio_nombre)
                
                # Ordenar por nivel educativo
                orden_educativo = ['Ninguna', 'Primaria', 'Básico', 'Diversificado', 'Universitario']
                tabla_ordenada = tabla.reindex([cat for cat in orden_educativo if cat in tabla.index])
                
                # Análisis de tendencia
                self._analizar_tendencia_educativa(tabla_ordenada, dominio_nombre)
            else:
                print(f"\n**Interpretación:**")
                print(f"La asociación NO ES ESTADÍSTICAMENTE SIGNIFICATIVA")
    
    def _analizar_proporciones_riesgo(self, tabla: pd.DataFrame, variable_nombre: str, dominio: str):
        """Analizar proporciones de riesgo por categoría"""
        print(f"\n**Proporciones de riesgo por {variable_nombre}:**")
        
        proporciones = {}
        for categoria in tabla.index:
            total = tabla.loc[categoria, :].sum()
            riesgo = tabla.loc[categoria, 'Riesgo combinado']
            proporcion = riesgo / total if total > 0 else 0
            proporciones[categoria] = proporcion
            print(f"- {categoria}: {riesgo}/{total} = {proporcion:.1%}")
        
        # Identificar extremos
        if len(proporciones) > 1:
            categoria_mayor_riesgo = max(proporciones, key=proporciones.get)
            categoria_menor_riesgo = min(proporciones, key=proporciones.get)
            
            print(f"\n**Categorías extremas:**")
            print(f"- Mayor riesgo: {categoria_mayor_riesgo} ({proporciones[categoria_mayor_riesgo]:.1%})")
            print(f"- Menor riesgo: {categoria_menor_riesgo} ({proporciones[categoria_menor_riesgo]:.1%})")
            
            # Diferencia de riesgo
            diferencia = proporciones[categoria_mayor_riesgo] - proporciones[categoria_menor_riesgo]
            print(f"- Diferencia de riesgo: {diferencia:.1%}")
            
            # Interpretación clínica
            print(f"\n**Interpretación clínica:**")
            if diferencia > 0.1:  # 10% de diferencia
                print(f"Existe una diferencia CLÍNICAMENTE SIGNIFICATIVA en el riesgo de trastornos de {dominio.lower()}")
                print(f"entre {categoria_mayor_riesgo.lower()} y {categoria_menor_riesgo.lower()}.")
            elif diferencia > 0.05:  # 5% de diferencia
                print(f"Existe una diferencia MODERADA en el riesgo de trastornos de {dominio.lower()}")
                print(f"entre {categoria_mayor_riesgo.lower()} y {categoria_menor_riesgo.lower()}.")
            else:
                print(f"Aunque estadísticamente significativa, la diferencia clínica es PEQUEÑA.")
    
    def _analizar_tendencia_educativa(self, tabla: pd.DataFrame, dominio: str):
        """Analizar tendencia según nivel educativo"""
        print(f"\n**Análisis de tendencia educativa:**")
        
        # Calcular proporciones ordenadas
        proporciones = []
        niveles = []
        for categoria in tabla.index:
            total = tabla.loc[categoria, :].sum()
            riesgo = tabla.loc[categoria, 'Riesgo combinado']
            proporcion = riesgo / total if total > 0 else 0
            proporciones.append(proporcion)
            niveles.append(categoria)
        
        # Verificar tendencia
        if len(proporciones) > 2:
            # Calcular coeficiente de correlación entre orden y riesgo
            orden_numerico = list(range(len(proporciones)))
            correlacion = np.corrcoef(orden_numerico, proporciones)[0, 1]
            
            print(f"Coeficiente de correlación: {correlacion:.3f}")
            
            if correlacion < -0.3:
                print("**TENDENCIA IDENTIFICADA:** A mayor nivel educativo materno, MENOR riesgo de trastornos")
                print(f"del neurodesarrollo en {dominio.lower()}.")
            elif correlacion > 0.3:
                print("**TENDENCIA IDENTIFICADA:** A mayor nivel educativo materno, MAYOR riesgo de trastornos")
                print(f"del neurodesarrollo en {dominio.lower()}.")
            else:
                print("**No se observa una tendencia clara** entre nivel educativo y riesgo.")
    
    def generar_graficos_complementarios(self):
        """Generar gráficos complementarios para el análisis"""
        # Gráfico de barras para nivel educativo materno
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, dominio in enumerate(self.dominios_desarrollo):
            categoria_col = dominio.replace('zscore_', 'categoria_')
            dominio_nombre = dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title()
            
            # Crear tabla de contingencia
            tabla = pd.crosstab(self.df['nivel_educativo_madre'], self.df[categoria_col])
            
            # Limpiar categorías no especificadas
            if 'No especificado' in tabla.index:
                tabla = tabla.drop('No especificado')
            
            # Calcular proporciones
            proporciones = tabla.div(tabla.sum(axis=1), axis=0)
            
            # Crear gráfico de barras
            proporciones.plot(kind='bar', ax=axes[i], color=['lightblue', 'salmon'])
            axes[i].set_title(f'{dominio_nombre}')
            axes[i].set_ylabel('Proporción')
            axes[i].set_xlabel('Nivel Educativo Materno')
            axes[i].legend(title='Categoría')
            axes[i].tick_params(axis='x', rotation=45)
        
        # Eliminar subplot vacío
        fig.delaxes(axes[5])
        
        plt.tight_layout()
        plt.savefig('/home/runner/work/data-tesis/data-tesis/graficos_nivel_educativo_materno.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Gráficos guardados como 'graficos_nivel_educativo_materno.png'")
    
    def generar_resumen_variables_multiples(self):
        """Generar resumen para todas las variables de múltiples categorías"""
        variables_multiples = ['nivel_educativo_madre', 'nivel_educativo_padre']
        
        print("=== RESUMEN VARIABLES CATEGÓRICAS MÚLTIPLES ===\n")
        
        for variable in variables_multiples:
            if variable not in self.df.columns:
                continue
                
            print(f"\n{'='*60}")
            print(f"VARIABLE: {variable.replace('_', ' ').title()}")
            print(f"{'='*60}")
            
            resultados_significativos = []
            
            for dominio in self.dominios_desarrollo:
                categoria_col = dominio.replace('zscore_', 'categoria_')
                dominio_nombre = dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title()
                
                # Crear tabla de contingencia
                tabla = pd.crosstab(self.df[variable], self.df[categoria_col])
                
                # Limpiar categorías no especificadas
                if 'No especificado' in tabla.index:
                    tabla = tabla.drop('No especificado')
                
                if tabla.shape[0] < 2:
                    continue
                
                # Test de chi-cuadrado
                chi2, p_valor, dof, expected = chi2_contingency(tabla)
                
                if p_valor < 0.05:
                    resultados_significativos.append({
                        'dominio': dominio_nombre,
                        'chi2': chi2,
                        'p_valor': p_valor,
                        'tabla': tabla
                    })
            
            if resultados_significativos:
                print(f"\n**Dominios con asociación significativa:**")
                for resultado in resultados_significativos:
                    print(f"- {resultado['dominio']}: χ² = {resultado['chi2']:.2f}, p = {resultado['p_valor']:.3f}")
                
                print(f"\n**Recomendaciones clínicas:**")
                if len(resultados_significativos) >= 3:
                    print(f"La variable {variable.replace('_', ' ')} muestra asociación significativa")
                    print(f"con múltiples dominios del neurodesarrollo. Se requiere:")
                    print(f"- Evaluación integral del desarrollo neuromotor")
                    print(f"- Intervención temprana dirigida")
                    print(f"- Seguimiento longitudinal")
                else:
                    print(f"La variable {variable.replace('_', ' ')} muestra asociación específica")
                    print(f"con algunos dominios. Se requiere evaluación focalizada.")
            else:
                print(f"\n**No se encontraron asociaciones significativas**")


def main():
    """Ejecutar análisis complementario"""
    analisis = AnalisisComplementario('/home/runner/work/data-tesis/data-tesis/datos_optimizados.csv')
    
    # Análisis específico para nivel educativo materno
    analisis.analizar_nivel_educativo_madre()
    
    # Generar gráficos
    analisis.generar_graficos_complementarios()
    
    # Resumen de variables múltiples
    analisis.generar_resumen_variables_multiples()
    
    print(f"\n{'='*80}")
    print("ANÁLISIS COMPLEMENTARIO COMPLETADO")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()