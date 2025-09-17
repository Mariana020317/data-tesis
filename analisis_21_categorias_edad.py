#!/usr/bin/env python3
"""
Análisis de 21 Categorías de Edad y Riesgo en Neurodesarrollo

Este script analiza cada una de las 21 categorías de edad específicas en el dataset
y su relación con el riesgo en el neurodesarrollo en los 5 dominios del desarrollo.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact
import warnings
warnings.filterwarnings('ignore')

class Analisis21CategoriasEdad:
    """Análisis detallado de 21 categorías de edad y riesgo neurodevelopmental"""
    
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
        
        # Convertir edad a numérica
        self.data['edad_meses_nino'] = self.data['edad_meses_nino'].str.replace(' meses', '').astype(float)
        
        # Verificar las 21 categorías de edad
        edades_unicas = sorted(self.data['edad_meses_nino'].unique())
        print(f"Categorías de edad encontradas: {len(edades_unicas)}")
        print(f"Edades: {edades_unicas}")
        
        # Crear variables de riesgo (Z ≤ -1 = riesgo)
        for dominio in self.dominios:
            riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
            self.data[riesgo_col] = (self.data[dominio] <= -1).astype(int)
            
        # Riesgo global (al menos 1 dominio en riesgo)
        columnas_riesgo = [f"riesgo_{dominio.replace('zscore_desarrollo_', '')}" 
                          for dominio in self.dominios]
        self.data['riesgo_global'] = (self.data[columnas_riesgo].sum(axis=1) >= 1).astype(int)
        
        print(f"Dataset preparado: {len(self.data)} registros")
        
    def analizar_prevalencia_por_edad(self):
        """Analizar prevalencia de riesgo por cada edad específica"""
        print("\n=== ANÁLISIS DE PREVALENCIA POR EDAD ===")
        
        # Obtener todas las edades únicas
        edades = sorted(self.data['edad_meses_nino'].unique())
        
        resultados = []
        
        for edad in edades:
            datos_edad = self.data[self.data['edad_meses_nino'] == edad]
            n_total = len(datos_edad)
            
            resultado_edad = {
                'edad_meses': edad,
                'n_total': n_total,
                'riesgo_global_n': datos_edad['riesgo_global'].sum(),
                'riesgo_global_pct': (datos_edad['riesgo_global'].sum() / n_total) * 100
            }
            
            # Análisis por dominio
            for dominio in self.dominios:
                riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
                n_riesgo = datos_edad[riesgo_col].sum()
                pct_riesgo = (n_riesgo / n_total) * 100
                
                resultado_edad[f'{dominio}_n'] = n_riesgo
                resultado_edad[f'{dominio}_pct'] = pct_riesgo
                
            resultados.append(resultado_edad)
            
        # Crear DataFrame con resultados
        df_resultados = pd.DataFrame(resultados)
        
        # Mostrar resultados
        print(f"\nPrevalencia de riesgo por edad (n = {len(self.data)}):")
        print("=" * 80)
        
        for _, row in df_resultados.iterrows():
            print(f"\nEdad: {row['edad_meses']:.0f} meses (n = {row['n_total']})")
            print(f"  Riesgo Global: {row['riesgo_global_n']:.0f} ({row['riesgo_global_pct']:.1f}%)")
            
            for dominio in self.dominios:
                nombre = self.nombres_dominios[dominio]
                n_col = f'{dominio}_n'
                pct_col = f'{dominio}_pct'
                print(f"  {nombre}: {row[n_col]:.0f} ({row[pct_col]:.1f}%)")
        
        return df_resultados
    
    def analizar_asociacion_chi2(self, df_resultados):
        """Analizar asociación entre edad y riesgo usando chi-cuadrado"""
        print("\n=== ANÁLISIS DE ASOCIACIÓN CHI-CUADRADO ===")
        
        resultados_chi2 = []
        
        # Análisis para riesgo global
        tabla_contingencia = pd.crosstab(self.data['edad_meses_nino'], self.data['riesgo_global'])
        chi2, p_value, dof, expected = chi2_contingency(tabla_contingencia)
        
        # Calcular V de Cramer
        n = tabla_contingencia.sum().sum()
        min_dim = min(tabla_contingencia.shape) - 1
        cramers_v = np.sqrt(chi2 / (n * min_dim))
        
        resultado_global = {
            'dominio': 'Riesgo Global',
            'chi2': chi2,
            'p_value': p_value,
            'grados_libertad': dof,
            'cramers_v': cramers_v,
            'significativo': p_value < 0.05
        }
        resultados_chi2.append(resultado_global)
        
        print(f"Riesgo Global:")
        print(f"  χ² = {chi2:.2f}, p = {p_value:.4f}, gl = {dof}")
        print(f"  V de Cramer = {cramers_v:.3f}")
        print(f"  Significativo: {'Sí' if p_value < 0.05 else 'No'}")
        
        # Análisis por dominio
        for dominio in self.dominios:
            riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
            tabla_contingencia = pd.crosstab(self.data['edad_meses_nino'], self.data[riesgo_col])
            
            chi2, p_value, dof, expected = chi2_contingency(tabla_contingencia)
            
            # V de Cramer
            n = tabla_contingencia.sum().sum()
            min_dim = min(tabla_contingencia.shape) - 1
            cramers_v = np.sqrt(chi2 / (n * min_dim))
            
            resultado_dominio = {
                'dominio': self.nombres_dominios[dominio],
                'chi2': chi2,
                'p_value': p_value,
                'grados_libertad': dof,
                'cramers_v': cramers_v,
                'significativo': p_value < 0.05
            }
            resultados_chi2.append(resultado_dominio)
            
            print(f"\n{self.nombres_dominios[dominio]}:")
            print(f"  χ² = {chi2:.2f}, p = {p_value:.4f}, gl = {dof}")
            print(f"  V de Cramer = {cramers_v:.3f}")
            print(f"  Significativo: {'Sí' if p_value < 0.05 else 'No'}")
        
        return pd.DataFrame(resultados_chi2)
    
    def identificar_edades_mayor_riesgo(self, df_resultados):
        """Identificar las edades con mayor riesgo por dominio"""
        print("\n=== EDADES CON MAYOR RIESGO POR DOMINIO ===")
        
        # Riesgo global
        max_global = df_resultados.loc[df_resultados['riesgo_global_pct'].idxmax()]
        print(f"\nRiesgo Global - Mayor prevalencia:")
        print(f"  Edad: {max_global['edad_meses']:.0f} meses")
        print(f"  Prevalencia: {max_global['riesgo_global_pct']:.1f}% ({max_global['riesgo_global_n']:.0f}/{max_global['n_total']})")
        
        # Top 5 edades con mayor riesgo global
        top_5_global = df_resultados.nlargest(5, 'riesgo_global_pct')
        print(f"\nTop 5 edades con mayor riesgo global:")
        for i, row in top_5_global.iterrows():
            print(f"  {row['edad_meses']:.0f} meses: {row['riesgo_global_pct']:.1f}% (n={row['n_total']})")
        
        # Análisis por dominio
        edades_mayor_riesgo = {}
        
        for dominio in self.dominios:
            pct_col = f'{dominio}_pct'
            n_col = f'{dominio}_n'
            
            max_dominio = df_resultados.loc[df_resultados[pct_col].idxmax()]
            
            nombre_dominio = self.nombres_dominios[dominio]
            edades_mayor_riesgo[nombre_dominio] = {
                'edad': max_dominio['edad_meses'],
                'prevalencia': max_dominio[pct_col],
                'n_riesgo': max_dominio[n_col],
                'n_total': max_dominio['n_total']
            }
            
            print(f"\n{nombre_dominio} - Mayor prevalencia:")
            print(f"  Edad: {max_dominio['edad_meses']:.0f} meses")
            print(f"  Prevalencia: {max_dominio[pct_col]:.1f}% ({max_dominio[n_col]:.0f}/{max_dominio['n_total']})")
            
            # Top 3 edades para este dominio
            top_3 = df_resultados.nlargest(3, pct_col)
            print(f"  Top 3 edades:")
            for j, row in top_3.iterrows():
                print(f"    {row['edad_meses']:.0f} meses: {row[pct_col]:.1f}% (n={row['n_total']})")
        
        return edades_mayor_riesgo
    
    def calcular_odds_ratios(self):
        """Calcular odds ratios para cada edad vs el resto"""
        print("\n=== CÁLCULO DE ODDS RATIOS POR EDAD ===")
        
        edades = sorted(self.data['edad_meses_nino'].unique())
        
        resultados_or = []
        
        for edad in edades:
            # Crear variable binaria: esta edad vs todas las demás
            edad_target = (self.data['edad_meses_nino'] == edad).astype(int)
            
            # Análisis para riesgo global
            tabla_2x2 = pd.crosstab(edad_target, self.data['riesgo_global'])
            
            if tabla_2x2.shape == (2, 2):
                # Calcular OR usando scipy
                oddsratio, pvalue = stats.fisher_exact(tabla_2x2)
                
                # Calcular IC 95%
                log_or = np.log(oddsratio)
                se_log_or = np.sqrt(np.sum(1.0/tabla_2x2.values))
                ci_lower = np.exp(log_or - 1.96 * se_log_or)
                ci_upper = np.exp(log_or + 1.96 * se_log_or)
                
                resultado_or = {
                    'edad_meses': edad,
                    'dominio': 'Riesgo Global',
                    'odds_ratio': oddsratio,
                    'p_value': pvalue,
                    'ci_lower': ci_lower,
                    'ci_upper': ci_upper,
                    'significativo': pvalue < 0.05
                }
                resultados_or.append(resultado_or)
                
            # Análisis por dominio
            for dominio in self.dominios:
                riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
                tabla_2x2 = pd.crosstab(edad_target, self.data[riesgo_col])
                
                if tabla_2x2.shape == (2, 2):
                    oddsratio, pvalue = stats.fisher_exact(tabla_2x2)
                    
                    log_or = np.log(oddsratio)
                    se_log_or = np.sqrt(np.sum(1.0/tabla_2x2.values))
                    ci_lower = np.exp(log_or - 1.96 * se_log_or)
                    ci_upper = np.exp(log_or + 1.96 * se_log_or)
                    
                    resultado_or = {
                        'edad_meses': edad,
                        'dominio': self.nombres_dominios[dominio],
                        'odds_ratio': oddsratio,
                        'p_value': pvalue,
                        'ci_lower': ci_lower,
                        'ci_upper': ci_upper,
                        'significativo': pvalue < 0.05
                    }
                    resultados_or.append(resultado_or)
        
        df_or = pd.DataFrame(resultados_or)
        
        # Mostrar resultados significativos
        print("Odds Ratios significativos (p < 0.05):")
        print("=" * 80)
        
        df_significativos = df_or[df_or['significativo'] == True].sort_values('odds_ratio', ascending=False)
        
        for _, row in df_significativos.iterrows():
            print(f"{row['dominio']} - Edad {row['edad_meses']:.0f} meses:")
            print(f"  OR = {row['odds_ratio']:.2f} (IC95%: {row['ci_lower']:.2f}-{row['ci_upper']:.2f})")
            print(f"  p = {row['p_value']:.4f}")
            print()
        
        return df_or
    
    def generar_resumen_ejecutivo(self, df_resultados, df_chi2, edades_mayor_riesgo, df_or):
        """Generar resumen ejecutivo del análisis"""
        print("\n" + "="*80)
        print("RESUMEN EJECUTIVO - ANÁLISIS DE 21 CATEGORÍAS DE EDAD")
        print("="*80)
        
        # Información general
        print(f"\n📊 INFORMACIÓN GENERAL:")
        print(f"  • Total de participantes: {len(self.data):,}")
        print(f"  • Categorías de edad analizadas: 21")
        print(f"  • Rango de edad: {self.data['edad_meses_nino'].min():.0f} - {self.data['edad_meses_nino'].max():.0f} meses")
        print(f"  • Dominios del desarrollo: 5")
        
        # Prevalencia general
        riesgo_global_total = (self.data['riesgo_global'].sum() / len(self.data)) * 100
        print(f"\n📈 PREVALENCIA GENERAL:")
        print(f"  • Riesgo global: {riesgo_global_total:.1f}%")
        
        for dominio in self.dominios:
            riesgo_col = f"riesgo_{dominio.replace('zscore_desarrollo_', '')}"
            prev = (self.data[riesgo_col].sum() / len(self.data)) * 100
            print(f"  • {self.nombres_dominios[dominio]}: {prev:.1f}%")
        
        # Asociaciones significativas
        print(f"\n🔍 ASOCIACIONES ESTADÍSTICAS:")
        dominios_significativos = df_chi2[df_chi2['significativo'] == True]
        print(f"  • Dominios con asociación significativa edad-riesgo: {len(dominios_significativos)}/6")
        
        for _, row in dominios_significativos.iterrows():
            print(f"    - {row['dominio']}: χ² = {row['chi2']:.2f}, p = {row['p_value']:.4f}")
        
        # Edades de mayor riesgo
        print(f"\n🎯 EDADES DE MAYOR RIESGO:")
        
        # Riesgo global
        max_global = df_resultados.loc[df_resultados['riesgo_global_pct'].idxmax()]
        print(f"  • Riesgo Global: {max_global['edad_meses']:.0f} meses ({max_global['riesgo_global_pct']:.1f}%)")
        
        # Por dominio
        for dominio, info in edades_mayor_riesgo.items():
            print(f"  • {dominio}: {info['edad']:.0f} meses ({info['prevalencia']:.1f}%)")
        
        # Odds ratios más altos
        print(f"\n📊 ODDS RATIOS MÁS ELEVADOS:")
        df_or_significativos = df_or[df_or['significativo'] == True]
        if len(df_or_significativos) > 0:
            top_or = df_or_significativos.nlargest(5, 'odds_ratio')
            for _, row in top_or.iterrows():
                print(f"  • {row['dominio']} - {row['edad_meses']:.0f} meses: OR = {row['odds_ratio']:.2f}")
        
        return {
            'total_participantes': len(self.data),
            'riesgo_global_prevalencia': riesgo_global_total,
            'dominios_significativos': len(dominios_significativos),
            'edades_mayor_riesgo': edades_mayor_riesgo
        }
    
    def ejecutar_analisis_completo(self):
        """Ejecutar análisis completo"""
        print("INICIANDO ANÁLISIS DE 21 CATEGORÍAS DE EDAD")
        print("="*60)
        
        # Cargar datos
        self.cargar_datos()
        
        # Análisis de prevalencia
        df_resultados = self.analizar_prevalencia_por_edad()
        
        # Análisis de asociación
        df_chi2 = self.analizar_asociacion_chi2(df_resultados)
        
        # Identificar edades de mayor riesgo
        edades_mayor_riesgo = self.identificar_edades_mayor_riesgo(df_resultados)
        
        # Calcular odds ratios
        df_or = self.calcular_odds_ratios()
        
        # Generar resumen
        resumen = self.generar_resumen_ejecutivo(df_resultados, df_chi2, edades_mayor_riesgo, df_or)
        
        # Guardar resultados
        self.guardar_resultados(df_resultados, df_chi2, df_or, resumen)
        
        return df_resultados, df_chi2, df_or, resumen
    
    def guardar_resultados(self, df_resultados, df_chi2, df_or, resumen):
        """Guardar resultados en archivos CSV"""
        print("\n📁 GUARDANDO RESULTADOS...")
        
        # Guardar prevalencia por edad
        df_resultados.to_csv('prevalencia_21_categorias_edad.csv', index=False)
        print("  ✓ prevalencia_21_categorias_edad.csv")
        
        # Guardar resultados chi-cuadrado
        df_chi2.to_csv('chi2_21_categorias_edad.csv', index=False)
        print("  ✓ chi2_21_categorias_edad.csv")
        
        # Guardar odds ratios
        df_or.to_csv('odds_ratios_21_categorias_edad.csv', index=False)
        print("  ✓ odds_ratios_21_categorias_edad.csv")
        
        # Crear tablas LaTeX
        self.crear_tablas_latex(df_resultados, df_chi2, df_or)
        
        print("  ✓ Archivos guardados exitosamente")
    
    def crear_tablas_latex(self, df_resultados, df_chi2, df_or):
        """Crear tablas formateadas para LaTeX"""
        
        # Tabla de prevalencia
        tabla_prevalencia = df_resultados[['edad_meses', 'n_total', 'riesgo_global_pct']].copy()
        tabla_prevalencia.columns = ['Edad (meses)', 'N', 'Riesgo Global (%)']
        tabla_prevalencia['Riesgo Global (%)'] = tabla_prevalencia['Riesgo Global (%)'].round(1)
        tabla_prevalencia.to_csv('tabla_latex_prevalencia_21_edades.csv', index=False)
        
        # Tabla de chi-cuadrado
        tabla_chi2 = df_chi2[['dominio', 'chi2', 'p_value', 'cramers_v']].copy()
        tabla_chi2.columns = ['Dominio', 'χ²', 'p-valor', 'V de Cramer']
        tabla_chi2['χ²'] = tabla_chi2['χ²'].round(2)
        tabla_chi2['p-valor'] = tabla_chi2['p-valor'].round(4)
        tabla_chi2['V de Cramer'] = tabla_chi2['V de Cramer'].round(3)
        tabla_chi2.to_csv('tabla_latex_chi2_21_edades.csv', index=False)
        
        # Tabla de odds ratios significativos
        df_or_sig = df_or[df_or['significativo'] == True].copy()
        if len(df_or_sig) > 0:
            tabla_or = df_or_sig[['edad_meses', 'dominio', 'odds_ratio', 'ci_lower', 'ci_upper', 'p_value']].copy()
            tabla_or.columns = ['Edad (meses)', 'Dominio', 'OR', 'IC 95% Inferior', 'IC 95% Superior', 'p-valor']
            tabla_or['OR'] = tabla_or['OR'].round(2)
            tabla_or['IC 95% Inferior'] = tabla_or['IC 95% Inferior'].round(2)
            tabla_or['IC 95% Superior'] = tabla_or['IC 95% Superior'].round(2)
            tabla_or['p-valor'] = tabla_or['p-valor'].round(4)
            tabla_or.to_csv('tabla_latex_odds_ratios_21_edades.csv', index=False)


def main():
    """Función principal"""
    try:
        # Ejecutar análisis
        analisis = Analisis21CategoriasEdad('datos_optimizados.csv')
        df_resultados, df_chi2, df_or, resumen = analisis.ejecutar_analisis_completo()
        
        print("\n✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERROR durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()