#!/usr/bin/env python3
"""
Análisis de Chi-cuadrado con interpretaciones detalladas de Odds Ratios
para resultados estadísticamente significativos en desarrollo neuromotor
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, fisher_exact
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

class AnalisisChiCuadradoOR:
    """
    Clase para realizar análisis de chi-cuadrado con interpretaciones detalladas
    de Odds Ratios para resultados estadísticamente significativos
    """
    
    def __init__(self, data_path: str):
        """
        Inicializar el análisis con los datos
        
        Args:
            data_path: Ruta al archivo CSV con los datos
        """
        self.df = pd.read_csv(data_path)
        self.dominios_desarrollo = [
            'zscore_desarrollo_comunicacion',
            'zscore_desarrollo_motricidad_gruesa', 
            'zscore_desarrollo_motricidad_fina',
            'zscore_desarrollo_resolucion_problemas',
            'zscore_desarrollo_socio_individual'
        ]
        
        # Variables categóricas para el análisis
        self.variables_categoricas = [
            'area_residencia',
            'sexo_nino',
            'grupo_etnico',
            'nivel_educativo_madre',
            'nivel_educativo_padre',
            'nacimiento_prematuro',
            'retardo_crecimiento',
            'desnutricion_aguda',
            'vacunacion_completa',
            'seguro_social',
            'situacion_laboral_madre',
            'tipo_empleo_madre',
            'estado_civil_cuidador',
            'propiedad_vivienda',
            'fuente_agua_consumo',
            'tipo_sanitario',
            'manejo_basura'
        ]
        
        # Preparar datos
        self._categorizar_desarrollo()
        self._limpiar_datos()
        
        # Almacenar resultados
        self.resultados_significativos = []
        self.resultados_no_significativos = []
    
    def _categorizar_desarrollo(self):
        """
        Categorizar los z-scores de desarrollo en:
        - 'Riesgo combinado' (z < -1): Combina alto riesgo + riesgo de trastorno
        - 'Desarrollo adecuado' (z >= -1): Desarrollo normal
        """
        for dominio in self.dominios_desarrollo:
            categoria_col = dominio.replace('zscore_', 'categoria_')
            self.df[categoria_col] = np.where(
                self.df[dominio] < -1.0,
                'Riesgo combinado',
                'Desarrollo adecuado'
            )
    
    def _limpiar_datos(self):
        """
        Limpiar datos eliminando valores faltantes en variables clave
        """
        # Eliminar filas con valores faltantes en dominios de desarrollo
        self.df = self.df.dropna(subset=self.dominios_desarrollo)
        
        # Limpiar variables categóricas
        for var in self.variables_categoricas:
            if var in self.df.columns:
                self.df[var] = self.df[var].fillna('No especificado')
    
    def calcular_odds_ratio(self, tabla_contingencia: pd.DataFrame) -> Dict:
        """
        Calcular Odds Ratio con intervalo de confianza al 95%
        
        Args:
            tabla_contingencia: Tabla de contingencia 2x2
            
        Returns:
            Dict con OR, IC inferior, IC superior, p-valor
        """
        # Asegurar que es una tabla 2x2
        if tabla_contingencia.shape != (2, 2):
            return None
            
        # Extraer valores de la tabla
        a, b = tabla_contingencia.iloc[0, 0], tabla_contingencia.iloc[0, 1]
        c, d = tabla_contingencia.iloc[1, 0], tabla_contingencia.iloc[1, 1]
        
        # Calcular OR
        if b == 0 or c == 0:
            # Corrección de continuidad
            a += 0.5
            b += 0.5
            c += 0.5
            d += 0.5
        
        or_value = (a * d) / (b * c)
        
        # Calcular intervalo de confianza
        log_or = np.log(or_value)
        se_log_or = np.sqrt(1/a + 1/b + 1/c + 1/d)
        
        # IC al 95%
        z_alpha = 1.96  # Para 95% de confianza
        ic_inferior = np.exp(log_or - z_alpha * se_log_or)
        ic_superior = np.exp(log_or + z_alpha * se_log_or)
        
        # Test exacto de Fisher para p-valor
        _, p_valor = fisher_exact([[a, b], [c, d]])
        
        return {
            'OR': or_value,
            'IC_inferior': ic_inferior,
            'IC_superior': ic_superior,
            'p_valor': p_valor,
            'tabla': tabla_contingencia
        }
    
    def clasificar_magnitud_or(self, or_value: float) -> str:
        """
        Clasificar la magnitud del OR según criterios clínicos
        
        Args:
            or_value: Valor del Odds Ratio
            
        Returns:
            Clasificación de la magnitud
        """
        if or_value == 1.0:
            return "Sin asociación"
        elif 1.1 <= or_value <= 1.4:
            return "Asociación débil"
        elif 1.5 <= or_value <= 2.9:
            return "Asociación moderada"
        elif 3.0 <= or_value <= 9.9:
            return "Asociación fuerte"
        elif or_value >= 10.0:
            return "Asociación muy fuerte"
        else:
            return "Sin clasificación"
    
    def calcular_metricas_adicionales(self, tabla_contingencia: pd.DataFrame) -> Dict:
        """
        Calcular métricas adicionales: diferencia de riesgo absoluto, NNT
        
        Args:
            tabla_contingencia: Tabla de contingencia 2x2
            
        Returns:
            Dict con métricas adicionales
        """
        # Calcular proporciones de riesgo
        total_fila1 = tabla_contingencia.iloc[0, :].sum()
        total_fila2 = tabla_contingencia.iloc[1, :].sum()
        
        riesgo_grupo1 = tabla_contingencia.iloc[0, 0] / total_fila1
        riesgo_grupo2 = tabla_contingencia.iloc[1, 0] / total_fila2
        
        # Diferencia de riesgo absoluto
        diferencia_riesgo = abs(riesgo_grupo1 - riesgo_grupo2)
        
        # Número necesario para tratar (NNT)
        nnt = 1 / diferencia_riesgo if diferencia_riesgo > 0 else float('inf')
        
        return {
            'riesgo_grupo1': riesgo_grupo1,
            'riesgo_grupo2': riesgo_grupo2,
            'diferencia_riesgo_absoluto': diferencia_riesgo,
            'nnt': nnt
        }
    
    def realizar_analisis_completo(self):
        """
        Realizar análisis completo de chi-cuadrado y OR para todas las combinaciones
        """
        print("=== ANÁLISIS DE CHI-CUADRADO CON INTERPRETACIONES DETALLADAS DE ODDS RATIOS ===\n")
        
        for dominio in self.dominios_desarrollo:
            categoria_col = dominio.replace('zscore_', 'categoria_')
            dominio_nombre = dominio.replace('zscore_desarrollo_', '').replace('_', ' ').title()
            
            print(f"\n{'='*80}")
            print(f"DOMINIO: {dominio_nombre}")
            print(f"{'='*80}")
            
            for variable in self.variables_categoricas:
                if variable not in self.df.columns:
                    continue
                    
                # Crear tabla de contingencia
                tabla = pd.crosstab(self.df[variable], self.df[categoria_col])
                
                # Verificar que tenemos al menos 2 categorías en cada variable
                if tabla.shape[0] < 2 or tabla.shape[1] < 2:
                    continue
                
                # Realizar chi-cuadrado
                chi2, p_valor, dof, expected = chi2_contingency(tabla)
                
                print(f"\n### Variable: {variable} vs Dominio: {dominio}")
                print(f"\n**Tabla de contingencia:**")
                print(tabla.to_string())
                
                # Solo proceder si es estadísticamente significativo
                if p_valor < 0.05:
                    print(f"\n**Interpretación:**")
                    print(f"La asociación ES ESTADÍSTICAMENTE SIGNIFICATIVA (χ² = {chi2:.2f}, p = {p_valor:.3f}).")
                    
                    # Para OR necesitamos tabla 2x2
                    if tabla.shape == (2, 2):
                        resultado_or = self.calcular_odds_ratio(tabla)
                        metricas = self.calcular_metricas_adicionales(tabla)
                        
                        if resultado_or:
                            self._generar_interpretacion_detallada(
                                variable, dominio_nombre, resultado_or, metricas, tabla
                            )
                            
                            # Almacenar resultado significativo
                            self.resultados_significativos.append({
                                'variable': variable,
                                'dominio': dominio_nombre,
                                'chi2': chi2,
                                'p_valor': p_valor,
                                'OR': resultado_or['OR'],
                                'IC_inferior': resultado_or['IC_inferior'],
                                'IC_superior': resultado_or['IC_superior'],
                                'tabla': tabla
                            })
                    else:
                        print(f"\n**Nota:** Tabla no es 2x2 ({tabla.shape}). OR no calculado.")
                        print(f"La asociación es significativa pero requiere análisis más detallado.")
                        
                        # Para tablas más grandes, mostrar análisis post-hoc
                        self._analizar_tabla_multiple(tabla, variable, dominio_nombre)
                
                else:
                    print(f"\n**Interpretación:**")
                    print(f"La asociación NO ES ESTADÍSTICAMENTE SIGNIFICATIVA (χ² = {chi2:.2f}, p = {p_valor:.3f}).")
                    
                    # Almacenar resultado no significativo
                    self.resultados_no_significativos.append({
                        'variable': variable,
                        'dominio': dominio_nombre,
                        'chi2': chi2,
                        'p_valor': p_valor
                    })
        
        # Generar resumen final
        self._generar_resumen_final()
        
        # Generar tabla resumen de resultados significativos
        self._generar_tabla_resumen()
    
    def _analizar_tabla_multiple(self, tabla: pd.DataFrame, variable: str, dominio: str):
        """
        Analizar tabla de contingencia con más de 2 categorías
        """
        print(f"\n**Análisis detallado para variable multicategórica:**")
        
        # Calcular proporciones de riesgo por categoría
        print(f"Proporciones de riesgo por categoría:")
        for categoria in tabla.index:
            total = tabla.loc[categoria, :].sum()
            riesgo = tabla.loc[categoria, 'Riesgo combinado']
            proporcion = riesgo / total
            print(f"- {categoria}: {riesgo}/{total} = {proporcion:.1%}")
        
        # Identificar categorías de mayor y menor riesgo
        proporciones = {}
        for categoria in tabla.index:
            total = tabla.loc[categoria, :].sum()
            riesgo = tabla.loc[categoria, 'Riesgo combinado']
            proporciones[categoria] = riesgo / total
        
        categoria_mayor_riesgo = max(proporciones, key=proporciones.get)
        categoria_menor_riesgo = min(proporciones, key=proporciones.get)
        
        print(f"\n**Categorías extremas:**")
        print(f"- Mayor riesgo: {categoria_mayor_riesgo} ({proporciones[categoria_mayor_riesgo]:.1%})")
        print(f"- Menor riesgo: {categoria_menor_riesgo} ({proporciones[categoria_menor_riesgo]:.1%})")
        
        # Calcular OR entre categorías extremas si es posible
        if len(tabla.index) >= 2:
            tabla_2x2 = tabla.loc[[categoria_mayor_riesgo, categoria_menor_riesgo], :]
            if tabla_2x2.shape == (2, 2):
                resultado_or = self.calcular_odds_ratio(tabla_2x2)
                if resultado_or:
                    print(f"\n**OR entre categorías extremas:**")
                    print(f"OR = {resultado_or['OR']:.2f} (IC 95%: {resultado_or['IC_inferior']:.2f} - {resultado_or['IC_superior']:.2f})")
                    magnitud = self.clasificar_magnitud_or(resultado_or['OR'])
                    print(f"Magnitud: {magnitud}")
    
    def _generar_tabla_resumen(self):
        """
        Generar tabla resumen de todos los resultados significativos
        """
        if not self.resultados_significativos:
            return
        
        print(f"\n\n{'='*80}")
        print("TABLA RESUMEN DE RESULTADOS SIGNIFICATIVOS")
        print(f"{'='*80}")
        
        # Crear DataFrame con resultados
        datos_resumen = []
        for resultado in self.resultados_significativos:
            datos_resumen.append({
                'Variable': resultado['variable'],
                'Dominio': resultado['dominio'],
                'Chi²': f"{resultado['chi2']:.2f}",
                'p-valor': f"{resultado['p_valor']:.3f}",
                'OR': f"{resultado['OR']:.2f}",
                'IC 95%': f"{resultado['IC_inferior']:.2f}-{resultado['IC_superior']:.2f}",
                'Magnitud': self.clasificar_magnitud_or(resultado['OR'])
            })
        
        df_resumen = pd.DataFrame(datos_resumen)
        df_resumen = df_resumen.sort_values('OR', ascending=False)
        
        print(df_resumen.to_string(index=False))
        
        # Guardar tabla como CSV
        df_resumen.to_csv('/home/runner/work/data-tesis/data-tesis/resumen_resultados_significativos.csv', index=False)
        print(f"\nTabla resumen guardada como 'resumen_resultados_significativos.csv'")
    
    def generar_informe_completo(self, archivo_salida: str = 'informe_analisis_odds_ratios.txt'):
        """
        Generar informe completo en archivo de texto
        """
        import sys
        from io import StringIO
        
        # Capturar la salida del análisis
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            self.realizar_analisis_completo()
        finally:
            sys.stdout = old_stdout
        
        # Guardar en archivo
        with open(f'/home/runner/work/data-tesis/data-tesis/{archivo_salida}', 'w', encoding='utf-8') as f:
            f.write(captured_output.getvalue())
        
        print(f"Informe completo guardado como '{archivo_salida}'")
        
        return captured_output.getvalue()
    
    def _generar_interpretacion_detallada(self, variable: str, dominio: str, 
                                        resultado_or: Dict, metricas: Dict, tabla: pd.DataFrame):
        """
        Generar interpretación detallada según el formato requerido
        """
        or_value = resultado_or['OR']
        ic_inf = resultado_or['IC_inferior']
        ic_sup = resultado_or['IC_superior']
        
        # Determinar grupos de riesgo basado en la proporción de riesgo combinado
        categorias = tabla.index.tolist()
        riesgo_grupo1 = tabla.iloc[0, 1] / tabla.iloc[0, :].sum()  # Proporción de riesgo combinado grupo 1
        riesgo_grupo2 = tabla.iloc[1, 1] / tabla.iloc[1, :].sum()  # Proporción de riesgo combinado grupo 2
        
        if riesgo_grupo1 > riesgo_grupo2:
            grupo_mayor_riesgo = categorias[0]
            grupo_referencia = categorias[1]
            riesgo_mayor = riesgo_grupo1
            riesgo_menor = riesgo_grupo2
        else:
            grupo_mayor_riesgo = categorias[1]
            grupo_referencia = categorias[0]
            riesgo_mayor = riesgo_grupo2
            riesgo_menor = riesgo_grupo1
        
        print(f"\n**Análisis detallado:**")
        print(f"- {grupo_mayor_riesgo} presenta mayor riesgo de trastornos del neurodesarrollo")
        print(f"- Riesgo combinado: {grupo_mayor_riesgo} {riesgo_mayor*100:.1f}% vs {grupo_referencia} {riesgo_menor*100:.1f}% (diferencia de {(riesgo_mayor-riesgo_menor)*100:.1f}%)")
        
        print(f"\n**Odds Ratio e Interpretación:**")
        print(f"OR = {or_value:.2f} (IC 95%: {ic_inf:.2f} - {ic_sup:.2f})")
        
        print(f"\n**Interpretación clínica:**")
        if or_value > 1.0:
            print(f"- Los {grupo_mayor_riesgo} tienen {or_value:.2f} veces mayor probabilidad de presentar trastornos del neurodesarrollo en {dominio.lower()} comparado con {grupo_referencia}")
        else:
            print(f"- Los {grupo_referencia} tienen {1/or_value:.2f} veces mayor probabilidad de presentar trastornos del neurodesarrollo en {dominio.lower()} comparado con {grupo_mayor_riesgo}")
        
        # Calcular ratio de desarrollo adecuado
        desarrollo_grupo1 = tabla.iloc[0, 0] / tabla.iloc[0, :].sum()  # Proporción desarrollo adecuado grupo 1
        desarrollo_grupo2 = tabla.iloc[1, 0] / tabla.iloc[1, :].sum()  # Proporción desarrollo adecuado grupo 2
        
        if desarrollo_grupo1 > desarrollo_grupo2:
            grupo_mejor_desarrollo = categorias[0]
            grupo_peor_desarrollo = categorias[1]
            ratio_desarrollo = (desarrollo_grupo1 / desarrollo_grupo2) * 100
            print(f"- Esto significa que por cada 100 niños con desarrollo adecuado en {grupo_peor_desarrollo}, hay {ratio_desarrollo:.0f} niños con desarrollo adecuado en {grupo_mejor_desarrollo}")
        else:
            grupo_mejor_desarrollo = categorias[1]
            grupo_peor_desarrollo = categorias[0]
            ratio_desarrollo = (desarrollo_grupo2 / desarrollo_grupo1) * 100
            print(f"- Esto significa que por cada 100 niños con desarrollo adecuado en {grupo_peor_desarrollo}, hay {ratio_desarrollo:.0f} niños con desarrollo adecuado en {grupo_mejor_desarrollo}")
        
        magnitud = self.clasificar_magnitud_or(or_value)
        print(f"- El riesgo es {magnitud.upper()} según la magnitud del OR")
        
        print(f"\n**Significancia clínica:**")
        print(f"- Diferencia de riesgo absoluto: {(riesgo_mayor-riesgo_menor)*100:.1f}%")
        nnt = 1 / (riesgo_mayor - riesgo_menor) if (riesgo_mayor - riesgo_menor) > 0 else float('inf')
        print(f"- Número necesario para tratar (NNT): {nnt:.0f} pacientes" if nnt != float('inf') else "- NNT: No calculable")
        
        # Relevancia para salud pública basada en OR ajustado
        or_abs = abs(or_value - 1.0) + 1.0  # Magnitud del OR sin importar dirección
        if or_abs >= 2.0:
            relevancia = "ALTA"
        elif or_abs >= 1.5:
            relevancia = "MODERADA"
        else:
            relevancia = "BAJA"
        
        print(f"- Relevancia para salud pública: {relevancia}")
        
        print(f"\n**Conclusión clínica:**")
        if or_abs >= 2.0:
            print(f"La población {grupo_mayor_riesgo.lower()} requiere intervención prioritaria en el desarrollo de {dominio.lower()}, con un riesgo más del doble comparado con {grupo_referencia.lower()}.")
        elif or_abs >= 1.5:
            print(f"La población {grupo_mayor_riesgo.lower()} requiere atención especial en el desarrollo de {dominio.lower()}, con riesgo moderadamente elevado comparado con {grupo_referencia.lower()}.")
        else:
            print(f"Aunque estadísticamente significativa, la asociación entre {variable} y {dominio.lower()} es clínicamente débil.")
    
    def _generar_resumen_final(self):
        """
        Generar resumen final con hallazgos principales
        """
        print(f"\n\n{'='*80}")
        print("RESUMEN DE HALLAZGOS PRINCIPALES")
        print(f"{'='*80}")
        
        if self.resultados_significativos:
            # Ordenar por OR descendente
            resultados_ordenados = sorted(self.resultados_significativos, 
                                        key=lambda x: x['OR'], reverse=True)
            
            print(f"\n**RESULTADOS ESTADÍSTICAMENTE SIGNIFICATIVOS (p < 0.05):**")
            print(f"Total de asociaciones significativas: {len(resultados_ordenados)}")
            
            print(f"\n**TOP 10 ASOCIACIONES MÁS FUERTES:**")
            for i, resultado in enumerate(resultados_ordenados[:10], 1):
                magnitud = self.clasificar_magnitud_or(resultado['OR'])
                print(f"{i}. {resultado['variable']} → {resultado['dominio']}: OR = {resultado['OR']:.2f} (IC: {resultado['IC_inferior']:.2f}-{resultado['IC_superior']:.2f}) - {magnitud}")
            
            # Análisis por dominio
            print(f"\n**ANÁLISIS POR DOMINIO:**")
            dominios_afectados = {}
            for resultado in resultados_ordenados:
                dominio = resultado['dominio']
                if dominio not in dominios_afectados:
                    dominios_afectados[dominio] = []
                dominios_afectados[dominio].append(resultado)
            
            for dominio, resultados in dominios_afectados.items():
                print(f"\n{dominio}: {len(resultados)} asociaciones significativas")
                for resultado in resultados[:3]:  # Top 3 por dominio
                    print(f"  - {resultado['variable']}: OR = {resultado['OR']:.2f}")
        
        else:
            print("\n**No se encontraron asociaciones estadísticamente significativas.**")
        
        if self.resultados_no_significativos:
            print(f"\n**RESULTADOS NO SIGNIFICATIVOS:**")
            print(f"Total de asociaciones no significativas: {len(self.resultados_no_significativos)}")
            print("Estas asociaciones no se interpretan debido a falta de significancia estadística.")
    
    def generar_grafico_forest_plot(self, top_n: int = 10):
        """
        Generar gráfico de forest plot para los top N resultados
        """
        if not self.resultados_significativos:
            print("No hay resultados significativos para graficar.")
            return
        
        # Ordenar resultados por OR
        resultados_ordenados = sorted(self.resultados_significativos, 
                                    key=lambda x: x['OR'], reverse=True)[:top_n]
        
        # Preparar datos para el gráfico
        labels = [f"{r['variable']} → {r['dominio']}" for r in resultados_ordenados]
        ors = [r['OR'] for r in resultados_ordenados]
        ic_inf = [r['IC_inferior'] for r in resultados_ordenados]
        ic_sup = [r['IC_superior'] for r in resultados_ordenados]
        
        # Crear gráfico
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Crear forest plot
        y_pos = np.arange(len(labels))
        
        # Puntos para OR
        ax.scatter(ors, y_pos, color='red', s=100, zorder=3)
        
        # Líneas para IC
        for i, (or_val, ic_i, ic_s) in enumerate(zip(ors, ic_inf, ic_sup)):
            ax.plot([ic_i, ic_s], [i, i], 'k-', linewidth=2)
            ax.plot([ic_i, ic_i], [i-0.1, i+0.1], 'k-', linewidth=2)
            ax.plot([ic_s, ic_s], [i-0.1, i+0.1], 'k-', linewidth=2)
        
        # Línea de referencia en OR = 1
        ax.axvline(x=1, color='blue', linestyle='--', alpha=0.7, linewidth=2)
        
        # Configurar ejes
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.set_xlabel('Odds Ratio (IC 95%)')
        ax.set_title(f'Forest Plot - Top {len(resultados_ordenados)} Asociaciones Significativas')
        ax.grid(True, alpha=0.3)
        
        # Escala logarítmica si hay OR muy altos
        if max(ors) > 10:
            ax.set_xscale('log')
        
        plt.tight_layout()
        plt.savefig('/home/runner/work/data-tesis/data-tesis/forest_plot_odds_ratios.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nGráfico de forest plot guardado como 'forest_plot_odds_ratios.png'")


def main():
    """
    Función principal para ejecutar el análisis
    """
    try:
        # Crear instancia del análisis
        analisis = AnalisisChiCuadradoOR('/home/runner/work/data-tesis/data-tesis/datos_optimizados.csv')
        
        # Realizar análisis completo
        analisis.realizar_analisis_completo()
        
        # Generar gráfico de forest plot
        analisis.generar_grafico_forest_plot(top_n=10)
        
        # Generar informe completo
        analisis.generar_informe_completo()
        
        print(f"\n{'='*80}")
        print("ANÁLISIS COMPLETADO EXITOSAMENTE")
        print(f"{'='*80}")
        print("\nArchivos generados:")
        print("- forest_plot_odds_ratios.png")
        print("- resumen_resultados_significativos.csv")
        print("- informe_analisis_odds_ratios.txt")
        
    except Exception as e:
        print(f"Error durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()