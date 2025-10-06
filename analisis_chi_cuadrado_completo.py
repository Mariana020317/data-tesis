#!/usr/bin/env python3
"""
Análisis completo de chi-cuadrado con todas las variables categóricas 
cruzadas con los 5 dominios del neurodesarrollo

Autor: Análisis automatizado
Fecha: 2024
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact
from statsmodels.stats.contingency_tables import mcnemar
from statsmodels.stats.proportion import proportions_ztest
import warnings
warnings.filterwarnings('ignore')

class AnalisisChiCuadrado:
    """Clase para realizar análisis completo de chi-cuadrado"""
    
    def __init__(self, archivo_datos="datos_optimizados.csv"):
        """Inicializar el análisis con los datos"""
        self.archivo_datos = archivo_datos
        self.variables_categoricas = [
            "edad_meses_nino", "edad_anos_madre", "edad_anos_padre", "grupo_etnico",
            "area_residencia", "nivel_educativo_madre", "nivel_educativo_padre",
            "fuente_agua_consumo", "tipo_sanitario", "manejo_basura", "tipo_energia_luz",
            "tipo_energia_cocina", "propiedad_vivienda", "sexo_jefe_hogar",
            "situacion_laboral_madre", "situacion_laboral_padre", "tipo_empleo_madre",
            "tipo_empleo_padre", "seguro_social", "total_personas_hogar", "total_hermanos",
            "posicion_nino_hermanos", "estado_civil_cuidador", "horas_pantalla",
            "horas_juego_cuidador", "numero_controles_prenatales", "ultrasonido_embarazo",
            "prenatales_primeros_3_meses", "prenatales_resto_embarazo", "servicio_asistencia_parto",
            "tipo_parto", "razon_cesarea_emergencia", "lactancia_primeros_6_meses",
            "lactancia_6-12_meses", "lactancia_12-24_meses", "vitamina_a_6-12_meses",
            "vitamina_a_12-18_meses", "vitamina_a_18-24_meses", "vitaminas_minerales_6-12_meses",
            "vitaminas_minerales_12-18_meses", "vitaminas_minerales_18-24_meses",
            "retardo_crecimiento", "desnutricion_aguda", "hospitalizado_neonatal",
            "razon_hospitalizado_neonatal", "hospitalizado_infancia", "razon_hospitalizado_infancia",
            "vacunacion_completa"
        ]
        
        self.dominios_neurodesarrollo = [
            "zscore_desarrollo_comunicacion",
            "zscore_desarrollo_motricidad_gruesa", 
            "zscore_desarrollo_motricidad_fina",
            "zscore_desarrollo_resolucion_problemas",
            "zscore_desarrollo_socio_individual"
        ]
        
        self.df = None
        self.archivo_salida = "analisis_chi_cuadrado_completo.txt"
        
    def cargar_datos(self):
        """Cargar y preparar los datos"""
        print("Cargando y preparando datos...")
        
        # Cargar datos
        self.df = pd.read_csv(self.archivo_datos)
        
        # Verificar variables disponibles
        variables_disponibles = [var for var in self.variables_categoricas if var in self.df.columns]
        variables_faltantes = [var for var in self.variables_categoricas if var not in self.df.columns]
        
        if variables_faltantes:
            print(f"Advertencia: Variables faltantes: {variables_faltantes}")
            
        self.variables_categoricas = variables_disponibles
        
        # Convertir variables categóricas a string para manejo consistente
        for var in self.variables_categoricas:
            self.df[var] = self.df[var].astype(str)
        
        # Categorizar z-scores según los criterios especificados
        for dominio in self.dominios_neurodesarrollo:
            if dominio in self.df.columns:
                zscore_col = self.df[dominio]
                categoria_col = f"{dominio}_categoria"
                
                # Crear categorías según los criterios
                # Primero, manejar valores faltantes
                zscore_valid = ~pd.isna(zscore_col)
                
                condiciones = [
                    zscore_valid & (zscore_col < -2),
                    zscore_valid & (zscore_col >= -2) & (zscore_col < -1),
                    zscore_valid & (zscore_col >= -1)
                ]
                
                categorias = [
                    "Alto riesgo (Z < -2)",
                    "Riesgo moderado (-2 ≤ Z < -1)",
                    "Desarrollo adecuado (Z ≥ -1)"
                ]
                
                self.df[categoria_col] = np.select(condiciones, categorias, default="Sin datos")
        
        print(f"Datos cargados exitosamente")
        print(f"Observaciones: {len(self.df)}")
        print(f"Variables categóricas disponibles: {len(self.variables_categoricas)}")
        print(f"Dominios del neurodesarrollo: {len(self.dominios_neurodesarrollo)}")
        
    def calcular_odds_ratio(self, tabla_contingencia):
        """Calcular odds ratio para tabla 2x2"""
        if tabla_contingencia.shape != (2, 2):
            return None
            
        # Extraer valores de la tabla
        a, b, c, d = tabla_contingencia.values.flatten()
        
        # Evitar división por cero
        if b == 0 or c == 0:
            return None
            
        # Calcular OR
        odds_ratio = (a * d) / (b * c)
        
        # Calcular IC 95% usando el método de Woolf
        if a == 0 or b == 0 or c == 0 or d == 0:
            return None
            
        log_or = np.log(odds_ratio)
        se_log_or = np.sqrt(1/a + 1/b + 1/c + 1/d)
        
        ci_lower = np.exp(log_or - 1.96 * se_log_or)
        ci_upper = np.exp(log_or + 1.96 * se_log_or)
        
        return {
            'odds_ratio': odds_ratio,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper
        }
    
    def realizar_test_estadistico(self, tabla_contingencia):
        """Realizar test chi-cuadrado o exacto de Fisher"""
        # Verificar si usar Fisher's exact test
        expected_freq = stats.chi2_contingency(tabla_contingencia)[3]
        usar_fisher = np.any(expected_freq < 5) or np.any(tabla_contingencia.values < 5)
        
        if usar_fisher and tabla_contingencia.shape == (2, 2):
            # Test exacto de Fisher para tablas 2x2
            odds_ratio, p_value = fisher_exact(tabla_contingencia.values)
            return {
                'test_type': "Fisher's Exact Test",
                'statistic': np.nan,
                'p_value': p_value,
                'df': np.nan,
                'method': 'exact'
            }
        else:
            # Test chi-cuadrado
            chi2, p_value, df, expected = chi2_contingency(tabla_contingencia.values)
            return {
                'test_type': "Chi-squared Test",
                'statistic': chi2,
                'p_value': p_value,
                'df': df,
                'method': 'chi-square'
            }
    
    def generar_interpretacion(self, variable_cat, dominio, tabla_contingencia, 
                             test_result, odds_ratio, porcentajes):
        """Generar interpretación en español"""
        
        # Extraer nombre del dominio
        nombre_dominio = dominio.replace("zscore_desarrollo_", "").replace("_", " ")
        
        # Determinar significancia
        es_significativo = test_result['p_value'] < 0.05
        
        # Calcular riesgo combinado por categoría
        if "Alto riesgo (Z < -2)" in porcentajes.columns and "Riesgo moderado (-2 ≤ Z < -1)" in porcentajes.columns:
            riesgo_combinado = porcentajes["Alto riesgo (Z < -2)"] + porcentajes["Riesgo moderado (-2 ≤ Z < -1)"]
        else:
            riesgo_combinado = porcentajes.iloc[:, 0]  # Usar primera columna como fallback
        
        # Encontrar categoría con mayor y menor riesgo
        categoria_mayor_riesgo = riesgo_combinado.idxmax()
        valor_mayor_riesgo = riesgo_combinado.max()
        
        categoria_menor_riesgo = riesgo_combinado.idxmin()
        valor_menor_riesgo = riesgo_combinado.min()
        
        # Generar interpretación
        interpretacion = f"""### Variable: {variable_cat} vs Dominio: {nombre_dominio}

**Interpretación:**
La asociación entre {variable_cat} y {nombre_dominio} {"ES ESTADÍSTICAMENTE SIGNIFICATIVA" if es_significativo else "NO ES ESTADÍSTICAMENTE SIGNIFICATIVA"} ({test_result['test_type']}{f" χ² = {test_result['statistic']:.3f}" if not np.isnan(test_result['statistic']) else ""}, p = {test_result['p_value']:.3e}).

**Análisis detallado:**
- {categoria_mayor_riesgo} presenta mayor riesgo de trastornos del neurodesarrollo ({valor_mayor_riesgo:.1f}%)
- Riesgo combinado: {categoria_mayor_riesgo} {valor_mayor_riesgo:.1f}% vs {categoria_menor_riesgo} {valor_menor_riesgo:.1f}% (diferencia de {valor_mayor_riesgo - valor_menor_riesgo:.1f}%)
- Esta diferencia se debe principalmente a mayor prevalencia de alto riesgo

"""
        
        # Agregar odds ratio si es significativo
        if es_significativo and odds_ratio is not None:
            interpretacion += f"""**Odds Ratio:**
Categorías de riesgo tienen OR = {odds_ratio['odds_ratio']:.2f} (IC 95%: {odds_ratio['ci_lower']:.2f} - {odds_ratio['ci_upper']:.2f}) veces mayor probabilidad de presentar trastornos del neurodesarrollo

"""
        
        # Conclusión clínica
        if es_significativo:
            interpretacion += f"""**Conclusión clínica:**
{categoria_mayor_riesgo} requiere intervención prioritaria en el desarrollo de {nombre_dominio}

"""
        else:
            interpretacion += f"""**Conclusión clínica:**
No se encontraron diferencias significativas entre grupos para {nombre_dominio}. Se requiere monitoreo uniforme.

"""
        
        return interpretacion
    
    def crear_tabla_para_or(self, tabla_contingencia):
        """Crear tabla 2x2 para cálculo de OR combinando categorías de riesgo"""
        if tabla_contingencia.shape[0] < 3:
            return tabla_contingencia
            
        # Combinar categorías de riesgo
        try:
            alto_riesgo = tabla_contingencia.loc[:, "Alto riesgo (Z < -2)"]
            riesgo_moderado = tabla_contingencia.loc[:, "Riesgo moderado (-2 ≤ Z < -1)"]
            desarrollo_adecuado = tabla_contingencia.loc[:, "Desarrollo adecuado (Z ≥ -1)"]
            
            # Crear nueva tabla 2x2
            tabla_2x2 = pd.DataFrame({
                'Riesgo combinado': alto_riesgo + riesgo_moderado,
                'Desarrollo adecuado': desarrollo_adecuado
            })
            
            return tabla_2x2
        except:
            return tabla_contingencia
    
    def realizar_analisis_completo(self):
        """Realizar análisis completo de chi-cuadrado"""
        
        # Cargar datos
        self.cargar_datos()
        
        # Crear archivo de salida
        with open(self.archivo_salida, 'w', encoding='utf-8') as f:
            f.write("# ANÁLISIS COMPLETO DE CHI-CUADRADO\n")
            f.write("# Variables categóricas cruzadas con dominios del neurodesarrollo\n")
            f.write("# Datos: datos_optimizados.csv\n")
            f.write(f"# Fecha: {pd.Timestamp.now().strftime('%d/%m/%Y')}\n\n")
        
        # Contadores para resumen
        total_analisis = len(self.variables_categoricas) * len(self.dominios_neurodesarrollo)
        analisis_completados = 0
        resultados_significativos = 0
        
        print(f"Iniciando análisis completo...")
        print(f"Total de análisis a realizar: {total_analisis}\n")
        
        # Iterar sobre todas las combinaciones
        for variable_cat in self.variables_categoricas:
            
            with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                f.write(f"## VARIABLE: {variable_cat.upper()}\n")
                f.write("=" * 80 + "\n\n")
            
            for dominio in self.dominios_neurodesarrollo:
                
                analisis_completados += 1
                dominio_categoria = f"{dominio}_categoria"
                
                print(f"Analizando: {variable_cat} vs {dominio} ({analisis_completados}/{total_analisis})")
                
                # Verificar que ambas variables existen
                if variable_cat not in self.df.columns or dominio_categoria not in self.df.columns:
                    with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                        f.write(f"### Variable: {variable_cat} vs Dominio: {dominio}\n")
                        f.write("ERROR: Variables no encontradas en los datos\n\n")
                    continue
                
                # Crear subset sin valores NA
                subset_datos = self.df.dropna(subset=[variable_cat, dominio_categoria])
                
                if len(subset_datos) < 10:
                    with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                        f.write(f"### Variable: {variable_cat} vs Dominio: {dominio}\n")
                        f.write("ERROR: Datos insuficientes para análisis (n < 10)\n\n")
                    continue
                
                # Crear tabla de contingencia
                tabla_contingencia = pd.crosstab(subset_datos[variable_cat], 
                                               subset_datos[dominio_categoria])
                
                # Verificar que la tabla tiene al menos 2x2
                if tabla_contingencia.shape[0] < 2 or tabla_contingencia.shape[1] < 2:
                    with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                        f.write(f"### Variable: {variable_cat} vs Dominio: {dominio}\n")
                        f.write("ERROR: Tabla de contingencia insuficiente\n\n")
                    continue
                
                # Realizar test estadístico
                test_result = self.realizar_test_estadistico(tabla_contingencia)
                
                # Calcular porcentajes por fila
                porcentajes = tabla_contingencia.div(tabla_contingencia.sum(axis=1), axis=0) * 100
                
                # Calcular odds ratio si es significativo
                odds_ratio = None
                if test_result['p_value'] < 0.05:
                    tabla_or = self.crear_tabla_para_or(tabla_contingencia)
                    if tabla_or.shape == (2, 2):
                        odds_ratio = self.calcular_odds_ratio(tabla_or)
                
                # Generar interpretación
                interpretacion = self.generar_interpretacion(variable_cat, dominio, 
                                                           tabla_contingencia, test_result, 
                                                           odds_ratio, porcentajes)
                
                # Escribir resultados al archivo
                with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                    f.write(interpretacion)
                    
                    # Tabla de contingencia
                    f.write("**Tabla de contingencia:**\n")
                    f.write("```\n")
                    f.write(tabla_contingencia.to_string())
                    f.write("\n```\n\n")
                    
                    # Proporciones por fila
                    f.write("**Proporciones por fila:**\n")
                    f.write("```\n")
                    f.write(porcentajes.round(1).to_string())
                    f.write("\n```\n\n")
                    
                    # Estadísticos
                    f.write("**Estadísticos:**\n")
                    f.write(f"- Test: {test_result['test_type']}\n")
                    if not np.isnan(test_result['statistic']):
                        f.write(f"- χ² = {test_result['statistic']:.3f}\n")
                    f.write(f"- p-value = {test_result['p_value']:.3e}\n")
                    if not np.isnan(test_result['df']):
                        f.write(f"- Grados de libertad = {test_result['df']}\n")
                    f.write("\n")
                    
                    f.write("---\n\n")
                
                # Contar si es significativo
                if test_result['p_value'] < 0.05:
                    resultados_significativos += 1
            
            with open(self.archivo_salida, 'a', encoding='utf-8') as f:
                f.write("\n")
        
        # Escribir resumen final
        with open(self.archivo_salida, 'a', encoding='utf-8') as f:
            f.write("# RESUMEN FINAL\n")
            f.write("=" * 80 + "\n")
            f.write(f"Total de análisis realizados: {analisis_completados}\n")
            f.write(f"Resultados estadísticamente significativos: {resultados_significativos}\n")
            f.write(f"Porcentaje de significancia: {resultados_significativos/analisis_completados*100:.1f}%\n")
            f.write(f"Archivo de salida: {self.archivo_salida}\n")
        
        print(f"\n¡Análisis completo finalizado!")
        print(f"Resultados guardados en: {self.archivo_salida}")
        print(f"Análisis completados: {analisis_completados}/{total_analisis}")
        print(f"Resultados significativos: {resultados_significativos}")
        
        return self.archivo_salida
    
    def generar_resumen_ejecutivo(self):
        """Generar resumen ejecutivo"""
        print("Generando resumen ejecutivo...")
        
        if not pd.io.common.file_exists(self.archivo_salida):
            print("ERROR: No se encontró el archivo de análisis completo")
            return None
        
        archivo_resumen = "resumen_ejecutivo_chi_cuadrado.txt"
        
        with open(archivo_resumen, 'w', encoding='utf-8') as f:
            f.write("# RESUMEN EJECUTIVO - ANÁLISIS CHI-CUADRADO\n")
            f.write("# Análisis de asociaciones entre variables categóricas y neurodesarrollo\n\n")
            
            f.write("## METODOLOGÍA\n")
            f.write("- Análisis chi-cuadrado para todas las combinaciones de variables categóricas\n")
            f.write("- Test exacto de Fisher para conteos pequeños\n")
            f.write("- Cálculo de odds ratios para resultados significativos\n")
            f.write("- Categorización de z-scores en tres niveles de riesgo\n\n")
            
            f.write("## INTERPRETACIÓN DE RESULTADOS\n")
            f.write("- Desarrollo adecuado: Z ≥ -1\n")
            f.write("- Riesgo moderado: -2 ≤ Z < -1\n")
            f.write("- Alto riesgo: Z < -2\n\n")
            
            f.write("Para análisis detallado, consultar: analisis_chi_cuadrado_completo.txt\n")
        
        print(f"Resumen ejecutivo generado en: {archivo_resumen}")
        return archivo_resumen


def main():
    """Función principal"""
    print("=== ANÁLISIS CHI-CUADRADO COMPLETO ===")
    print("Iniciando análisis automatizado...\n")
    
    # Verificar que existe el archivo de datos
    if not pd.io.common.file_exists("datos_optimizados.csv"):
        print("ERROR: No se encontró el archivo datos_optimizados.csv")
        print("Asegúrese de que el archivo esté en el directorio de trabajo")
        return
    
    # Crear instancia del análisis
    analisis = AnalisisChiCuadrado("datos_optimizados.csv")
    
    # Ejecutar análisis completo
    archivo_salida = analisis.realizar_analisis_completo()
    
    # Generar resumen ejecutivo
    analisis.generar_resumen_ejecutivo()
    
    print("\n=== ANÁLISIS COMPLETADO ===")
    print("Archivos generados:")
    print("- Análisis completo: analisis_chi_cuadrado_completo.txt")
    print("- Resumen ejecutivo: resumen_ejecutivo_chi_cuadrado.txt")


if __name__ == "__main__":
    main()