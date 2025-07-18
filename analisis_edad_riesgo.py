#!/usr/bin/env python3
"""
Análisis de Asociación entre Edad y Riesgo en Neurodesarrollo

Este script realiza un análisis estadístico completo para establecer la asociación
entre puntajes Z en diferentes edades y riesgo en el neurodesarrollo.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, levene, bartlett
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.contingency_tables import mcnemar
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnalisisNeurodesarrollo:
    """Clase para realizar análisis estadístico de neurodesarrollo"""
    
    def __init__(self, filepath):
        """Inicializar con el archivo de datos"""
        self.filepath = filepath
        self.data = None
        self.dominios = [
            'zscore_desarrollo_comunicacion',
            'zscore_desarrollo_motricidad_gruesa', 
            'zscore_desarrollo_motricidad_fina',
            'zscore_desarrollo_resolucion_problemas',
            'zscore_desarrollo_socio_individual'
        ]
        self.nombres_dominios = {
            'zscore_desarrollo_comunicacion': 'Comunicación',
            'zscore_desarrollo_motricidad_gruesa': 'Motricidad Gruesa',
            'zscore_desarrollo_motricidad_fina': 'Motricidad Fina', 
            'zscore_desarrollo_resolucion_problemas': 'Resolución de Problemas',
            'zscore_desarrollo_socio_individual': 'Desarrollo Socio-Individual'
        }
        
    def cargar_datos(self):
        """Cargar y preparar los datos"""
        print("Cargando datos...")
        self.data = pd.read_csv(self.filepath)
        print(f"Dataset cargado: {len(self.data)} registros")
        
        # Verificar columnas requeridas
        columnas_requeridas = ['edad_meses_nino'] + self.dominios
        for col in columnas_requeridas:
            if col not in self.data.columns:
                raise ValueError(f"Columna requerida no encontrada: {col}")
        
        # Convertir edad a numérica (remover " meses" del texto)
        self.data['edad_meses_nino'] = self.data['edad_meses_nino'].str.replace(' meses', '').astype(float)
        
        print("Columnas de análisis verificadas correctamente")
        
    def crear_variables_riesgo(self):
        """Crear variables de riesgo (Z ≤ -1 = riesgo, Z > -1 = adecuado)"""
        print("Creando variables de riesgo...")
        
        # Crear variables de riesgo por dominio
        for dominio in self.dominios:
            riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
            self.data[riesgo_col] = (self.data[dominio] <= -1).astype(int)
            
        # Crear variable de riesgo global (riesgo en al menos 1 dominio)
        columnas_riesgo = [f"riesgo_{dominio.replace('zscore_desarrollo_', '')}" 
                          for dominio in self.dominios]
        self.data['riesgo_global'] = (self.data[columnas_riesgo].sum(axis=1) >= 1).astype(int)
        
        print("Variables de riesgo creadas:")
        for col in columnas_riesgo + ['riesgo_global']:
            n_riesgo = self.data[col].sum()
            pct_riesgo = (n_riesgo / len(self.data)) * 100
            print(f"  {col}: {n_riesgo} ({pct_riesgo:.1f}%)")
            
    def crear_grupos_edad(self):
        """Crear grupos de edad para análisis"""
        print("Creando grupos de edad...")
        
        # Análisis de distribución de edades
        edad_min = self.data['edad_meses_nino'].min()
        edad_max = self.data['edad_meses_nino'].max()
        print(f"Rango de edades: {edad_min:.0f} - {edad_max:.0f} meses")
        
        # Crear grupos de edad apropiados
        # Basado en hitos del desarrollo infantil
        bins = [0, 6, 12, 18, 24, 36, 48, 60, np.inf]
        labels = ['0-6m', '6-12m', '12-18m', '18-24m', '24-36m', '36-48m', '48-60m', '60m+']
        
        self.data['grupo_edad'] = pd.cut(self.data['edad_meses_nino'], 
                                        bins=bins, labels=labels, right=False)
        
        # Mostrar distribución por grupo
        print("Distribución por grupo de edad:")
        print(self.data['grupo_edad'].value_counts().sort_index())
        
    def estadisticas_descriptivas(self):
        """Calcular estadísticas descriptivas por grupo de edad"""
        print("Calculando estadísticas descriptivas...")
        
        # Estadísticas por grupo de edad
        stats_por_grupo = self.data.groupby('grupo_edad')[self.dominios].agg([
            'count', 'mean', 'std', 'min', 'max', 
            lambda x: np.percentile(x, 25),
            lambda x: np.percentile(x, 50), 
            lambda x: np.percentile(x, 75)
        ]).round(3)
        
        # Renombrar columnas de percentiles
        stats_por_grupo.columns = stats_por_grupo.columns.droplevel(0)
        new_columns = []
        for col in stats_por_grupo.columns:
            if '<lambda>' in str(col):
                if '25' in str(col):
                    new_columns.append('Q1')
                elif '50' in str(col):
                    new_columns.append('Q2')
                else:
                    new_columns.append('Q3')
            else:
                new_columns.append(col)
        stats_por_grupo.columns = new_columns
        
        # Guardar estadísticas
        stats_por_grupo.to_csv('/home/runner/work/data-tesis/data-tesis/estadisticas_descriptivas.csv')
        print("Estadísticas descriptivas guardadas en 'estadisticas_descriptivas.csv'")
        
        return stats_por_grupo
        
    def pruebas_normalidad(self):
        """Realizar pruebas de normalidad por grupo de edad"""
        print("Realizando pruebas de normalidad...")
        
        resultados_normalidad = {}
        
        for dominio in self.dominios:
            resultados_normalidad[dominio] = {}
            
            for grupo in self.data['grupo_edad'].cat.categories:
                datos_grupo = self.data[self.data['grupo_edad'] == grupo][dominio].dropna()
                
                if len(datos_grupo) < 3:
                    continue
                    
                # Shapiro-Wilk (recomendado para n < 5000)
                if len(datos_grupo) <= 5000:
                    shapiro_stat, shapiro_p = stats.shapiro(datos_grupo)
                else:
                    shapiro_stat, shapiro_p = np.nan, np.nan
                
                # Kolmogorov-Smirnov
                ks_stat, ks_p = stats.kstest(datos_grupo, 'norm', 
                                           args=(datos_grupo.mean(), datos_grupo.std()))
                
                resultados_normalidad[dominio][grupo] = {
                    'n': len(datos_grupo),
                    'shapiro_stat': shapiro_stat,
                    'shapiro_p': shapiro_p,
                    'ks_stat': ks_stat,
                    'ks_p': ks_p,
                    'normal_shapiro': shapiro_p > 0.05 if not np.isnan(shapiro_p) else None,
                    'normal_ks': ks_p > 0.05
                }
        
        # Convertir a DataFrame para guardar
        normalidad_df = []
        for dominio in resultados_normalidad:
            for grupo in resultados_normalidad[dominio]:
                row = {'dominio': dominio, 'grupo_edad': grupo}
                row.update(resultados_normalidad[dominio][grupo])
                normalidad_df.append(row)
        
        normalidad_df = pd.DataFrame(normalidad_df)
        normalidad_df.to_csv('/home/runner/work/data-tesis/data-tesis/pruebas_normalidad.csv', index=False)
        print("Pruebas de normalidad guardadas en 'pruebas_normalidad.csv'")
        
        return resultados_normalidad
        
    def pruebas_homogeneidad(self):
        """Realizar pruebas de homogeneidad de varianzas"""
        print("Realizando pruebas de homogeneidad de varianzas...")
        
        resultados_homogeneidad = {}
        
        for dominio in self.dominios:
            # Obtener datos por grupo
            grupos_datos = []
            for grupo in self.data['grupo_edad'].cat.categories:
                datos_grupo = self.data[self.data['grupo_edad'] == grupo][dominio].dropna()
                if len(datos_grupo) >= 2:  # Mínimo 2 observaciones
                    grupos_datos.append(datos_grupo)
            
            if len(grupos_datos) < 2:
                continue
                
            # Prueba de Levene
            levene_stat, levene_p = levene(*grupos_datos)
            
            # Prueba de Bartlett
            bartlett_stat, bartlett_p = bartlett(*grupos_datos)
            
            resultados_homogeneidad[dominio] = {
                'levene_stat': levene_stat,
                'levene_p': levene_p,
                'bartlett_stat': bartlett_stat,
                'bartlett_p': bartlett_p,
                'homogeneo_levene': levene_p > 0.05,
                'homogeneo_bartlett': bartlett_p > 0.05
            }
        
        # Convertir a DataFrame para guardar
        homogeneidad_df = pd.DataFrame(resultados_homogeneidad).T
        homogeneidad_df.to_csv('/home/runner/work/data-tesis/data-tesis/pruebas_homogeneidad.csv')
        print("Pruebas de homogeneidad guardadas en 'pruebas_homogeneidad.csv'")
        
        return resultados_homogeneidad
        
    def analisis_anova(self):
        """Realizar análisis ANOVA para comparar medias entre grupos de edad"""
        print("Realizando análisis ANOVA...")
        
        resultados_anova = {}
        
        for dominio in self.dominios:
            # Obtener datos por grupo
            grupos_datos = []
            for grupo in self.data['grupo_edad'].cat.categories:
                datos_grupo = self.data[self.data['grupo_edad'] == grupo][dominio].dropna()
                if len(datos_grupo) >= 2:
                    grupos_datos.append(datos_grupo)
            
            if len(grupos_datos) < 2:
                continue
                
            # ANOVA de una vía
            f_stat, p_value = f_oneway(*grupos_datos)
            
            # Calcular eta cuadrado (tamaño del efecto)
            # SS_between / SS_total
            n_total = sum(len(grupo) for grupo in grupos_datos)
            grand_mean = np.concatenate(grupos_datos).mean()
            
            ss_between = sum(len(grupo) * (grupo.mean() - grand_mean)**2 for grupo in grupos_datos)
            ss_total = sum(((grupo - grand_mean)**2).sum() for grupo in grupos_datos)
            
            eta_squared = ss_between / ss_total if ss_total > 0 else 0
            
            resultados_anova[dominio] = {
                'f_statistic': f_stat,
                'p_value': p_value,
                'eta_squared': eta_squared,
                'significativo': p_value < 0.05,
                'n_grupos': len(grupos_datos),
                'n_total': n_total
            }
        
        # Convertir a DataFrame para guardar
        anova_df = pd.DataFrame(resultados_anova).T
        anova_df.to_csv('/home/runner/work/data-tesis/data-tesis/resultados_anova.csv')
        print("Resultados ANOVA guardados en 'resultados_anova.csv'")
        
        return resultados_anova
        
    def analisis_chi_cuadrado(self):
        """Realizar análisis Chi-cuadrado para asociación entre edad y riesgo"""
        print("Realizando análisis Chi-cuadrado...")
        
        resultados_chi2 = {}
        
        # Análisis por dominio
        for dominio in self.dominios:
            riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
            
            # Crear tabla de contingencia
            tabla_contingencia = pd.crosstab(self.data['grupo_edad'], 
                                           self.data[riesgo_col])
            
            # Chi-cuadrado
            chi2_stat, p_value, dof, expected = chi2_contingency(tabla_contingencia)
            
            # V de Cramer (tamaño del efecto)
            n = tabla_contingencia.sum().sum()
            cramer_v = np.sqrt(chi2_stat / (n * (min(tabla_contingencia.shape) - 1)))
            
            resultados_chi2[dominio] = {
                'chi2_statistic': chi2_stat,
                'p_value': p_value,
                'degrees_freedom': dof,
                'cramer_v': cramer_v,
                'significativo': p_value < 0.05,
                'tabla_contingencia': tabla_contingencia
            }
        
        # Análisis para riesgo global
        tabla_contingencia_global = pd.crosstab(self.data['grupo_edad'], 
                                              self.data['riesgo_global'])
        chi2_stat, p_value, dof, expected = chi2_contingency(tabla_contingencia_global)
        n = tabla_contingencia_global.sum().sum()
        cramer_v = np.sqrt(chi2_stat / (n * (min(tabla_contingencia_global.shape) - 1)))
        
        resultados_chi2['riesgo_global'] = {
            'chi2_statistic': chi2_stat,
            'p_value': p_value,
            'degrees_freedom': dof,
            'cramer_v': cramer_v,
            'significativo': p_value < 0.05,
            'tabla_contingencia': tabla_contingencia_global
        }
        
        # Guardar resultados
        chi2_summary = []
        for dominio in resultados_chi2:
            if dominio != 'riesgo_global':
                nombre_dominio = self.nombres_dominios.get(dominio, dominio)
            else:
                nombre_dominio = 'Riesgo Global'
                
            chi2_summary.append({
                'dominio': nombre_dominio,
                'chi2_statistic': resultados_chi2[dominio]['chi2_statistic'],
                'p_value': resultados_chi2[dominio]['p_value'],
                'degrees_freedom': resultados_chi2[dominio]['degrees_freedom'],
                'cramer_v': resultados_chi2[dominio]['cramer_v'],
                'significativo': resultados_chi2[dominio]['significativo']
            })
        
        chi2_df = pd.DataFrame(chi2_summary)
        chi2_df.to_csv('/home/runner/work/data-tesis/data-tesis/resultados_chi2.csv', index=False)
        print("Resultados Chi-cuadrado guardados en 'resultados_chi2.csv'")
        
        return resultados_chi2
        
    def analisis_post_hoc(self):
        """Realizar análisis post-hoc para comparaciones múltiples"""
        print("Realizando análisis post-hoc...")
        
        resultados_post_hoc = {}
        
        for dominio in self.dominios:
            # Preparar datos para Tukey HSD
            datos_tukey = self.data[['grupo_edad', dominio]].dropna()
            
            if len(datos_tukey) < 10:  # Mínimo de datos
                continue
                
            # Tukey HSD
            tukey_results = pairwise_tukeyhsd(datos_tukey[dominio], 
                                            datos_tukey['grupo_edad'])
            
            # Convertir resultados a DataFrame
            tukey_df = pd.DataFrame(data=tukey_results.summary().data[1:], 
                                  columns=tukey_results.summary().data[0])
            
            resultados_post_hoc[dominio] = {
                'tukey_results': tukey_results,
                'tukey_df': tukey_df,
                'significant_pairs': tukey_df[tukey_df['reject'] == True]
            }
        
        # Guardar resultados significativos
        for dominio in resultados_post_hoc:
            if not resultados_post_hoc[dominio]['significant_pairs'].empty:
                filename = f"/home/runner/work/data-tesis/data-tesis/tukey_{dominio.replace('zscore_desarrollo_', '')}.csv"
                resultados_post_hoc[dominio]['significant_pairs'].to_csv(filename, index=False)
        
        print("Análisis post-hoc completado")
        return resultados_post_hoc
        
    def crear_visualizaciones(self):
        """Crear visualizaciones principales"""
        print("Creando visualizaciones...")
        
        # Crear directorio para gráficos
        import os
        os.makedirs('/home/runner/work/data-tesis/data-tesis/graficos', exist_ok=True)
        
        # 1. Boxplots por dominio y grupo de edad
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, dominio in enumerate(self.dominios):
            sns.boxplot(data=self.data, x='grupo_edad', y=dominio, ax=axes[i])
            axes[i].set_title(f'{self.nombres_dominios[dominio]}')
            axes[i].axhline(y=-1, color='red', linestyle='--', alpha=0.7, label='Umbral de riesgo')
            axes[i].tick_params(axis='x', rotation=45)
            axes[i].legend()
        
        # Ocultar el último subplot
        axes[-1].set_visible(False)
        
        plt.tight_layout()
        plt.savefig('/home/runner/work/data-tesis/data-tesis/graficos/boxplots_dominios.png', 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Gráfico de barras para prevalencia de riesgo por edad
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Calcular prevalencia por grupo de edad
        prevalencia_data = []
        for grupo in self.data['grupo_edad'].cat.categories:
            subset = self.data[self.data['grupo_edad'] == grupo]
            for dominio in self.dominios:
                riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
                prevalencia = (subset[riesgo_col].sum() / len(subset)) * 100
                prevalencia_data.append({
                    'grupo_edad': grupo,
                    'dominio': self.nombres_dominios[dominio],
                    'prevalencia': prevalencia
                })
        
        prevalencia_df = pd.DataFrame(prevalencia_data)
        
        # Crear gráfico de barras agrupadas
        sns.barplot(data=prevalencia_df, x='grupo_edad', y='prevalencia', 
                   hue='dominio', ax=ax)
        ax.set_title('Prevalencia de Riesgo por Grupo de Edad y Dominio')
        ax.set_xlabel('Grupo de Edad')
        ax.set_ylabel('Prevalencia de Riesgo (%)')
        ax.legend(title='Dominio', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('/home/runner/work/data-tesis/data-tesis/graficos/prevalencia_riesgo.png', 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. Heatmap de correlaciones entre dominios
        fig, ax = plt.subplots(figsize=(10, 8))
        
        correlaciones = self.data[self.dominios].corr()
        correlaciones.index = [self.nombres_dominios[col] for col in correlaciones.index]
        correlaciones.columns = [self.nombres_dominios[col] for col in correlaciones.columns]
        
        sns.heatmap(correlaciones, annot=True, cmap='coolwarm', center=0, 
                   square=True, ax=ax)
        ax.set_title('Correlaciones entre Dominios del Desarrollo')
        
        plt.tight_layout()
        plt.savefig('/home/runner/work/data-tesis/data-tesis/graficos/correlaciones_dominios.png', 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        print("Visualizaciones guardadas en directorio 'graficos/'")
        
    def ejecutar_analisis_completo(self):
        """Ejecutar análisis completo"""
        print("=== ANÁLISIS DE ASOCIACIÓN ENTRE EDAD Y RIESGO EN NEURODESARROLLO ===\n")
        
        # 1. Cargar datos
        self.cargar_datos()
        
        # 2. Preparar variables
        self.crear_variables_riesgo()
        self.crear_grupos_edad()
        
        # 3. Análisis descriptivo
        stats_descriptivas = self.estadisticas_descriptivas()
        
        # 4. Pruebas de supuestos
        normalidad = self.pruebas_normalidad()
        homogeneidad = self.pruebas_homogeneidad()
        
        # 5. Análisis inferenciales
        anova_results = self.analisis_anova()
        chi2_results = self.analisis_chi_cuadrado()
        post_hoc_results = self.analisis_post_hoc()
        
        # 6. Visualizaciones
        self.crear_visualizaciones()
        
        print("\n=== ANÁLISIS COMPLETADO ===")
        print("Archivos generados:")
        print("- estadisticas_descriptivas.csv")
        print("- pruebas_normalidad.csv")
        print("- pruebas_homogeneidad.csv")
        print("- resultados_anova.csv")
        print("- resultados_chi2.csv")
        print("- tukey_*.csv (para comparaciones significativas)")
        print("- graficos/ (directorio con visualizaciones)")
        
        return {
            'estadisticas_descriptivas': stats_descriptivas,
            'normalidad': normalidad,
            'homogeneidad': homogeneidad,
            'anova': anova_results,
            'chi2': chi2_results,
            'post_hoc': post_hoc_results
        }


def main():
    """Función principal"""
    # Inicializar análisis
    analisis = AnalisisNeurodesarrollo('/home/runner/work/data-tesis/data-tesis/datos_optimizados.csv')
    
    # Ejecutar análisis completo
    resultados = analisis.ejecutar_analisis_completo()
    
    return resultados

if __name__ == "__main__":
    resultados = main()