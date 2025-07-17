#!/usr/bin/env python3
"""
=============================================================================
ANOVA Analysis Script for Developmental Z-Scores (Python Version)
Author: Generated for data-tesis project
Purpose: Perform one-way ANOVA analysis for sociodemographic, environmental, 
         and clinical variables with five developmental z-score domains
=============================================================================
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway, levene, shapiro
import pingouin as pg
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# Configuration and Setup
# =============================================================================

# Z-score domains (dependent variables)
zscore_domains = [
    "zscore_desarrollo_comunicacion",
    "zscore_desarrollo_motricidad_gruesa", 
    "zscore_desarrollo_motricidad_fina",
    "zscore_desarrollo_resolucion_problemas",
    "zscore_desarrollo_socio_individual"
]

# Spanish names for domains (for LaTeX output)
domain_names_spanish = [
    "Comunicación",
    "Motricidad gruesa",
    "Motricidad fina", 
    "Resolución de problemas",
    "Socio-individual"
]

# Independent variables to test
independent_vars = [
    "edad_meses_nino", "edad_anos_madre", "edad_anos_padre",
    "grupo_etnico", "area_residencia", 
    "nivel_educativo_madre", "nivel_educativo_padre",
    "fuente_agua_consumo", "tipo_sanitario", "manejo_basura",
    "tipo_energia_luz", "tipo_energia_cocina", "propiedad_vivienda",
    "sexo_jefe_hogar", "situacion_laboral_madre", "situacion_laboral_padre",
    "tipo_empleo_madre", "tipo_empleo_padre", "seguro_social",
    "total_personas_hogar", "total_hermanos", "posicion_nino_hermanos",
    "estado_civil_cuidador", "horas_pantalla", "horas_juego_cuidador",
    "numero_controles_prenatales", "ultrasonido_embarazo",
    "prenatales_primeros_3_meses", "prenatales_resto_embarazo",
    "servicio_asistencia_parto", "tipo_parto", "razon_cesarea_emergencia",
    "lactancia_primeros_6_meses", "lactancia_6-12_meses", "lactancia_12-24_meses",
    "vitamina_a_6-12_meses", "vitamina_a_12-18_meses", "vitamina_a_18-24_meses",
    "vitaminas_minerales_6-12_meses", "vitaminas_minerales_12-18_meses", 
    "vitaminas_minerales_18-24_meses", "retardo_crecimiento", "desnutricion_aguda",
    "hospitalizado_neonatal", "razon_hospitalizado_neonatal",
    "hospitalizado_infancia", "razon_hospitalizado_infancia",
    "vacunacion_completa"
]

# =============================================================================
# Data Loading and Preparation Functions
# =============================================================================

def load_and_prepare_data():
    """Load and prepare the dataset for analysis"""
    print("Loading data...")
    
    # Load data
    df = pd.read_csv('datos_optimizados.csv')
    
    print(f"Data loaded: {df.shape[0]} observations, {df.shape[1]} variables")
    
    # Create categorical groups for continuous and ordinal variables
    df = create_categorical_groups(df)
    
    # Check for required columns
    missing_domains = [col for col in zscore_domains if col not in df.columns]
    if missing_domains:
        print(f"Warning: Missing z-score domains: {missing_domains}")
    
    print("Data preparation complete.")
    return df

def create_categorical_groups(df):
    """Create categorical groups for continuous and ordinal variables"""
    df = df.copy()
    
    # Convert edad_meses_nino to numeric (extract number from string)
    df['edad_meses_nino_num'] = df['edad_meses_nino'].str.extract('(\\d+)').astype(int)
    
    # Create age intervals for child age in months
    df['edad_meses_nino_original'] = df['edad_meses_nino']
    df['edad_meses_nino'] = pd.cut(df['edad_meses_nino_num'], 
                                  bins=[0, 6, 12, 18, 24, 36, 48, 60], 
                                  labels=['0-6 meses', '7-12 meses', '13-18 meses', 
                                         '19-24 meses', '25-36 meses', '37-48 meses', '49-60 meses'])
    
    # Create age intervals for mother's age
    df['edad_anos_madre_original'] = df['edad_anos_madre']
    df['edad_anos_madre'] = pd.cut(df['edad_anos_madre'], 
                                  bins=[0, 20, 25, 30, 35, 100], 
                                  labels=['≤20 años', '21-25 años', '26-30 años', 
                                         '31-35 años', '>35 años'])
    
    # Create age intervals for father's age
    df['edad_anos_padre_original'] = df['edad_anos_padre']
    df['edad_anos_padre'] = pd.cut(df['edad_anos_padre'], 
                                  bins=[0, 25, 30, 35, 40, 100], 
                                  labels=['≤25 años', '26-30 años', '31-35 años', 
                                         '36-40 años', '>40 años'])
    
    # Group prenatal care visits - standard medical cutoff
    df['numero_controles_prenatales_original'] = df['numero_controles_prenatales']
    df['numero_controles_prenatales'] = df['numero_controles_prenatales'].apply(
        lambda x: '< 4 controles' if pd.notna(x) and x < 4 else '≥ 4 controles' if pd.notna(x) else np.nan
    )
    
    # Group number of siblings
    df['total_hermanos_original'] = df['total_hermanos']
    df['total_hermanos'] = df['total_hermanos'].apply(
        lambda x: '0 hermanos' if pd.notna(x) and x == 0 else 
                  '1 hermano' if pd.notna(x) and x == 1 else 
                  '2 hermanos' if pd.notna(x) and x == 2 else 
                  '3+ hermanos' if pd.notna(x) and x >= 3 else np.nan
    )
    
    # Group household size
    df['total_personas_hogar_original'] = df['total_personas_hogar']
    df['total_personas_hogar'] = df['total_personas_hogar'].apply(
        lambda x: '3-4 personas' if pd.notna(x) and x <= 4 else 
                  '5-6 personas' if pd.notna(x) and x <= 6 else 
                  '7-8 personas' if pd.notna(x) and x <= 8 else 
                  '9+ personas' if pd.notna(x) and x >= 9 else np.nan
    )
    
    # Group hours of play with caregiver
    df['horas_juego_cuidador_original'] = df['horas_juego_cuidador']
    df['horas_juego_cuidador'] = df['horas_juego_cuidador'].apply(
        lambda x: '0-1 horas' if pd.notna(x) and x <= 1 else 
                  '2-3 horas' if pd.notna(x) and x <= 3 else 
                  '4-5 horas' if pd.notna(x) and x <= 5 else 
                  '6+ horas' if pd.notna(x) and x >= 6 else np.nan
    )
    
    # Group hours of screen time
    df['horas_pantalla_original'] = df['horas_pantalla']
    df['horas_pantalla'] = df['horas_pantalla'].apply(
        lambda x: '0-1 horas' if pd.notna(x) and x <= 1 else 
                  '2-3 horas' if pd.notna(x) and x <= 3 else 
                  '4-5 horas' if pd.notna(x) and x <= 5 else 
                  '6+ horas' if pd.notna(x) and x >= 6 else np.nan
    )
    
    return df

def calculate_risk_classification(z_scores):
    """Calculate risk classification based on z-scores"""
    risk_counts = {}
    total_valid = len(z_scores.dropna())
    
    if total_valid == 0:
        return {'normal': 0, 'riesgo': 0, 'pct_normal': 0, 'pct_riesgo': 0}
    
    # Z > -1: Normal development
    normal_count = len(z_scores[z_scores > -1])
    
    # Z ≤ -1: Risk for developmental disorders
    risk_count = len(z_scores[z_scores <= -1])
    
    return {
        'normal': normal_count,
        'riesgo': risk_count,
        'pct_normal': (normal_count / total_valid) * 100,
        'pct_riesgo': (risk_count / total_valid) * 100
    }

def check_anova_assumptions(groups):
    """Check ANOVA assumptions: normality and homogeneity of variance"""
    
    # Remove empty groups and convert to pandas Series for consistent handling
    groups = [pd.Series(group).dropna() for group in groups if len(pd.Series(group).dropna()) > 0]
    
    if len(groups) < 2:
        return False, False, "Insufficient groups for testing"
    
    # Check normality (Shapiro-Wilk test for each group)
    normality_ok = True
    for i, group in enumerate(groups):
        if len(group) >= 3:  # Need at least 3 observations for Shapiro-Wilk
            _, p_val = shapiro(group)
            if p_val < 0.05:
                normality_ok = False
                break
    
    # Check homogeneity of variance (Levene's test)
    homogeneity_ok = True
    if len(groups) >= 2:
        try:
            _, p_val = levene(*groups)
            if p_val < 0.05:
                homogeneity_ok = False
        except:
            homogeneity_ok = False
    
    return normality_ok, homogeneity_ok, "OK"

def perform_anova_analysis(df, independent_var, dependent_var):
    """Perform ANOVA analysis for a given independent and dependent variable"""
    
    # Remove missing values
    analysis_df = df[[independent_var, dependent_var]].dropna()
    
    if len(analysis_df) < 10:  # Need minimum sample size
        return None
    
    # Get groups
    groups = [group[dependent_var].values for name, group in analysis_df.groupby(independent_var)]
    group_names = [name for name, group in analysis_df.groupby(independent_var)]
    
    # Remove empty groups
    valid_groups = []
    valid_names = []
    for i, group in enumerate(groups):
        if len(group) >= 3:  # Need at least 3 observations per group
            valid_groups.append(group)
            valid_names.append(group_names[i])
    
    if len(valid_groups) < 2:
        return None
    
    # Check assumptions
    normality_ok, homogeneity_ok, assumption_note = check_anova_assumptions(valid_groups)
    
    # Perform appropriate ANOVA
    if homogeneity_ok:
        # Standard ANOVA
        f_stat, p_value = f_oneway(*valid_groups)
        test_type = "ANOVA"
    else:
        # Welch's ANOVA (unequal variances)
        try:
            # Use pingouin for Welch's ANOVA
            # Create DataFrame for pingouin
            data_list = []
            for i, (group, name) in enumerate(zip(valid_groups, valid_names)):
                for value in group:
                    data_list.append({'value': value, 'group': str(name)})
            
            df_welch = pd.DataFrame(data_list)
            result = pg.welch_anova(dv='value', between='group', data=df_welch)
            f_stat = result['F'].iloc[0]
            p_value = result['p-unc'].iloc[0]
            test_type = "Welch's ANOVA"
        except:
            # Fallback to standard ANOVA if Welch fails
            f_stat, p_value = f_oneway(*valid_groups)
            test_type = "ANOVA"
    
    # Calculate group statistics
    group_stats = {}
    for i, (name, group) in enumerate(zip(valid_names, valid_groups)):
        risk_class = calculate_risk_classification(pd.Series(group))
        group_stats[name] = {
            'n': len(group),
            'mean': np.mean(group),
            'std': np.std(group, ddof=1),
            'risk_classification': risk_class
        }
    
    # Post-hoc analysis for significant results
    post_hoc_info = ""
    if p_value < 0.05:
        post_hoc_info = perform_post_hoc_analysis(valid_groups, valid_names)
    
    return {
        'independent_var': independent_var,
        'dependent_var': dependent_var,
        'test_type': test_type,
        'f_statistic': f_stat,
        'p_value': p_value,
        'significant': p_value < 0.05,
        'group_stats': group_stats,
        'assumptions': {
            'normality': normality_ok,
            'homogeneity': homogeneity_ok,
            'note': assumption_note
        },
        'post_hoc_info': post_hoc_info,
        'sample_size': len(analysis_df)
    }

def perform_post_hoc_analysis(groups, group_names):
    """Perform post-hoc analysis to identify which groups differ significantly"""
    
    if len(groups) < 2:
        return ""
    
    # Simple pairwise comparisons using t-tests with Bonferroni correction
    n_comparisons = len(groups) * (len(groups) - 1) // 2
    alpha_corrected = 0.05 / n_comparisons
    
    significant_pairs = []
    group_means = [np.mean(group) for group in groups]
    
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            try:
                t_stat, p_val = stats.ttest_ind(groups[i], groups[j])
                if p_val < alpha_corrected:
                    # Identify which group has lower mean (more at risk)
                    if group_means[i] < group_means[j]:
                        affected_group = group_names[i]
                        comparison_group = group_names[j]
                    else:
                        affected_group = group_names[j]
                        comparison_group = group_names[i]
                    
                    significant_pairs.append({
                        'group1': group_names[i],
                        'group2': group_names[j],
                        'affected_group': affected_group,
                        'p_value': p_val,
                        'mean_diff': abs(group_means[i] - group_means[j])
                    })
            except:
                continue
    
    if not significant_pairs:
        return ""
    
    # Find the most affected group (lowest mean)
    most_affected = min(group_names, key=lambda x: group_means[group_names.index(x)])
    
    return f"Grupo más afectado: {most_affected}"

def calculate_group_risk_priority(df, independent_var, dependent_var):
    """Calculate risk priority for each group in a variable"""
    
    # Remove missing values
    analysis_df = df[[independent_var, dependent_var]].dropna()
    
    if len(analysis_df) < 10:
        return {}
    
    group_risks = {}
    for name, group in analysis_df.groupby(independent_var):
        if len(group) >= 3:
            z_scores = group[dependent_var]
            risk_info = calculate_risk_classification(z_scores)
            group_risks[name] = {
                'risk_percentage': risk_info['pct_riesgo'],
                'n': len(group),
                'mean_zscore': z_scores.mean()
            }
    
    return group_risks

def run_complete_analysis(df):
    """Run complete ANOVA analysis prioritizing high-risk groups"""
    
    results = []
    total_tests = len(independent_vars) * len(zscore_domains)
    current_test = 0
    
    print(f"Starting RISK-PRIORITIZED ANOVA analysis for {total_tests} combinations...")
    print("Prioritizing analysis based on developmental risk (Z ≤ -1)")
    
    # First, calculate risk priorities for all combinations
    print("\nCalculating risk priorities for all variable-domain combinations...")
    
    risk_priorities = []
    for independent_var in independent_vars:
        if independent_var not in df.columns:
            print(f"Warning: Variable {independent_var} not found in dataset")
            continue
            
        for dependent_var in zscore_domains:
            group_risks = calculate_group_risk_priority(df, independent_var, dependent_var)
            if group_risks:
                # Calculate overall risk priority for this combination
                max_risk = max([info['risk_percentage'] for info in group_risks.values()])
                avg_risk = sum([info['risk_percentage'] for info in group_risks.values()]) / len(group_risks)
                risk_variance = max_risk - min([info['risk_percentage'] for info in group_risks.values()])
                
                risk_priorities.append({
                    'independent_var': independent_var,
                    'dependent_var': dependent_var,
                    'max_risk': max_risk,
                    'avg_risk': avg_risk,
                    'risk_variance': risk_variance,
                    'priority_score': max_risk + (risk_variance * 0.5)  # Prioritize high max risk and high variance
                })
    
    # Sort by priority score (highest risk first)
    risk_priorities.sort(key=lambda x: x['priority_score'], reverse=True)
    
    print(f"Risk analysis complete. Top 10 priority combinations:")
    for i, combo in enumerate(risk_priorities[:10]):
        domain_idx = zscore_domains.index(combo['dependent_var'])
        domain_spanish = domain_names_spanish[domain_idx]
        print(f"{i+1}. {combo['independent_var']} vs {domain_spanish}: Max risk={combo['max_risk']:.1f}%, Priority={combo['priority_score']:.1f}")
    
    print(f"\nRunning ANOVA analysis in risk-prioritized order...")
    
    # Run analysis in prioritized order
    for combo in risk_priorities:
        current_test += 1
        independent_var = combo['independent_var']
        dependent_var = combo['dependent_var']
        
        domain_idx = zscore_domains.index(dependent_var)
        domain_spanish = domain_names_spanish[domain_idx]
        
        print(f"Progress: {current_test}/{total_tests} - PRIORITY ANALYSIS: {independent_var} vs {domain_spanish} (Risk priority: {combo['priority_score']:.1f})")
        
        result = perform_anova_analysis(df, independent_var, dependent_var)
        if result:
            # Add priority information to result
            result['risk_priority'] = combo['priority_score']
            result['max_group_risk'] = combo['max_risk']
            result['avg_group_risk'] = combo['avg_risk']
            result['risk_variance'] = combo['risk_variance']
            results.append(result)
    
    print(f"Analysis complete. {len(results)} successful tests out of {total_tests}")
    
    # Sort results by risk priority for output
    results.sort(key=lambda x: x.get('risk_priority', 0), reverse=True)
    
    return results

def generate_latex_tables(results):
    """Generate comprehensive LaTeX tables with explanatory content and risk prioritization"""
    
    latex_content = r"""\\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}
\usepackage{geometry}
\geometry{margin=2cm}

\title{Análisis ANOVA de Factores de Desarrollo en la Primera Infancia\\
\large{Análisis Priorizado por Riesgo de Trastornos del Desarrollo}}
\author{Análisis Estadístico Integral}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}

Este documento presenta los resultados del análisis estadístico integral mediante ANOVA de una vía para evaluar las asociaciones entre variables sociodemográficas, ambientales y clínicas con cinco dominios del desarrollo infantil. El análisis se realizó sobre una muestra de """ + str(len(results)) + r""" observaciones válidas, \textbf{priorizando las combinaciones con mayor riesgo de trastornos del desarrollo}.

\subsection{Enfoque de Priorización por Riesgo}

El análisis priorizó las combinaciones de variables basándose en:
\begin{itemize}
\item \textbf{Riesgo máximo}: Porcentaje más alto de niños con Z ≤ -1 en cualquier grupo
\item \textbf{Variabilidad del riesgo}: Diferencias entre grupos en términos de riesgo
\item \textbf{Puntuación de prioridad}: Combinación de riesgo máximo y variabilidad
\end{itemize}

\subsection{Dominios del Desarrollo Evaluados}

Los cinco dominios del desarrollo evaluados mediante puntajes Z son:

\begin{itemize}
\item \textbf{Comunicación}: Desarrollo del lenguaje receptivo y expresivo
\item \textbf{Motricidad gruesa}: Desarrollo de habilidades motoras de músculos grandes
\item \textbf{Motricidad fina}: Desarrollo de habilidades motoras precisas
\item \textbf{Resolución de problemas}: Desarrollo cognitivo y de razonamiento
\item \textbf{Socio-individual}: Desarrollo de habilidades sociales y emocionales
\end{itemize}

\subsection{Clasificación de Riesgo}

La clasificación de riesgo de desarrollo se basa en los puntajes Z:

\begin{itemize}
\item \textbf{Desarrollo normal}: Z > -1
\item \textbf{Riesgo de trastornos del desarrollo}: Z ≤ -1
\end{itemize}

\subsection{Metodología Estadística}

Para cada variable independiente se realizó:

\begin{enumerate}
\item \textbf{Análisis de priorización}: Cálculo de riesgo por grupo y priorización
\item Verificación de supuestos (normalidad y homocedasticidad)
\item ANOVA de una vía o ANOVA de Welch según corresponda
\item Análisis post-hoc para identificar grupos afectados cuando p < 0.05
\item Cálculo de estadísticas descriptivas y clasificación de riesgo por grupo
\end{enumerate}

\section{Resultados}

Los resultados se presentan ordenados por prioridad de riesgo, mostrando primero las combinaciones con mayor riesgo de trastornos del desarrollo.

"""
    
    # Group results by independent variable, maintaining risk priority order
    var_results = {}
    for result in results:
        var_name = result['independent_var']
        if var_name not in var_results:
            var_results[var_name] = []
        var_results[var_name].append(result)
    
    # Sort variables by their highest risk priority score
    sorted_vars = []
    for var_name, var_results_list in var_results.items():
        max_priority = max([r.get('risk_priority', 0) for r in var_results_list])
        sorted_vars.append((var_name, var_results_list, max_priority))
    
    sorted_vars.sort(key=lambda x: x[2], reverse=True)
    
    # Generate tables for each independent variable in priority order
    for var_name, var_results_list, max_priority in sorted_vars:
        latex_content += generate_variable_table(var_name, var_results_list)
    
    latex_content += r"""
\section{Conclusiones}

Este análisis priorizado por riesgo proporciona evidencia estadística sobre los factores más críticos asociados con el desarrollo infantil en múltiples dominios. Las combinaciones con mayor riesgo de trastornos del desarrollo han sido identificadas y analizadas prioritariamente, lo que permite una intervención más dirigida y efectiva.

Los resultados pueden informar políticas de salud pública y prácticas clínicas para la promoción del desarrollo integral en la primera infancia, con especial atención a los grupos de mayor riesgo identificados.

\end{document}
"""
    
    return latex_content

def generate_variable_table(var_name, var_results):
    """Generate LaTeX table for a specific independent variable"""
    
    # Get Spanish variable name
    spanish_var_names = {
        'edad_meses_nino': 'Edad del niño (meses)',
        'edad_anos_madre': 'Edad de la madre (años)',
        'edad_anos_padre': 'Edad del padre (años)',
        'grupo_etnico': 'Grupo étnico',
        'area_residencia': 'Área de residencia',
        'nivel_educativo_madre': 'Nivel educativo de la madre',
        'nivel_educativo_padre': 'Nivel educativo del padre',
        'fuente_agua_consumo': 'Fuente de agua para consumo',
        'tipo_sanitario': 'Tipo de sanitario',
        'manejo_basura': 'Manejo de basura',
        'tipo_energia_luz': 'Tipo de energía para luz',
        'tipo_energia_cocina': 'Tipo de energía para cocina',
        'propiedad_vivienda': 'Propiedad de vivienda',
        'sexo_jefe_hogar': 'Sexo del jefe de hogar',
        'situacion_laboral_madre': 'Situación laboral de la madre',
        'situacion_laboral_padre': 'Situación laboral del padre',
        'tipo_empleo_madre': 'Tipo de empleo de la madre',
        'tipo_empleo_padre': 'Tipo de empleo del padre',
        'seguro_social': 'Seguro social',
        'total_personas_hogar': 'Total de personas en el hogar',
        'total_hermanos': 'Total de hermanos',
        'posicion_nino_hermanos': 'Posición del niño entre hermanos',
        'estado_civil_cuidador': 'Estado civil del cuidador',
        'horas_pantalla': 'Horas de exposición a pantallas',
        'horas_juego_cuidador': 'Horas de juego con cuidador',
        'numero_controles_prenatales': 'Número de controles prenatales',
        'ultrasonido_embarazo': 'Ultrasonido durante el embarazo',
        'prenatales_primeros_3_meses': 'Controles prenatales primeros 3 meses',
        'prenatales_resto_embarazo': 'Controles prenatales resto del embarazo',
        'servicio_asistencia_parto': 'Servicio de asistencia al parto',
        'tipo_parto': 'Tipo de parto',
        'razon_cesarea_emergencia': 'Razón de cesárea de emergencia',
        'lactancia_primeros_6_meses': 'Lactancia primeros 6 meses',
        'lactancia_6-12_meses': 'Lactancia 6-12 meses',
        'lactancia_12-24_meses': 'Lactancia 12-24 meses',
        'vitamina_a_6-12_meses': 'Vitamina A 6-12 meses',
        'vitamina_a_12-18_meses': 'Vitamina A 12-18 meses',
        'vitamina_a_18-24_meses': 'Vitamina A 18-24 meses',
        'vitaminas_minerales_6-12_meses': 'Vitaminas y minerales 6-12 meses',
        'vitaminas_minerales_12-18_meses': 'Vitaminas y minerales 12-18 meses',
        'vitaminas_minerales_18-24_meses': 'Vitaminas y minerales 18-24 meses',
        'retardo_crecimiento': 'Retardo del crecimiento',
        'desnutricion_aguda': 'Desnutrición aguda',
        'hospitalizado_neonatal': 'Hospitalizado neonatal',
        'razon_hospitalizado_neonatal': 'Razón hospitalización neonatal',
        'hospitalizado_infancia': 'Hospitalizado en infancia',
        'razon_hospitalizado_infancia': 'Razón hospitalización en infancia',
        'vacunacion_completa': 'Vacunación completa'
    }
    
    spanish_name = spanish_var_names.get(var_name, var_name.replace('_', ' ').title())
    
    latex_content = f"""
\\subsection{{{spanish_name}}}

"""
    
    # Create table header with risk priority information
    latex_content += r"""
\begin{longtable}{|l|c|c|c|c|c|c|}
\hline
\textbf{Dominio} & \textbf{F/W} & \textbf{p-valor} & \textbf{Significativo} & \textbf{Método} & \textbf{N} & \textbf{Riesgo Máx \%} \\
\hline
\endfirsthead

\hline
\textbf{Dominio} & \textbf{F/W} & \textbf{p-valor} & \textbf{Significativo} & \textbf{Método} & \textbf{N} & \textbf{Riesgo Máx \%} \\
\hline
\endhead

\hline
\endfoot

\hline
\endlastfoot

"""
    
    # Sort results by risk priority for this variable
    var_results_sorted = sorted(var_results, key=lambda x: x.get('risk_priority', 0), reverse=True)
    
    # Add results for each domain
    significant_results = []
    for result in var_results_sorted:
        domain_idx = zscore_domains.index(result['dependent_var'])
        domain_name = domain_names_spanish[domain_idx]
        
        f_stat = f"{result['f_statistic']:.2f}"
        p_val = f"{result['p_value']:.3f}" if result['p_value'] >= 0.001 else "< 0.001"
        significant = "Sí" if result['significant'] else "No"
        method = result['test_type']
        n = result['sample_size']
        max_risk = f"{result.get('max_group_risk', 0):.1f}"
        
        latex_content += f"{domain_name} & {f_stat} & {p_val} & {significant} & {method} & {n} & {max_risk} \\\\\n"
        
        if result['significant']:
            significant_results.append(result)
    
    latex_content += r"""
\end{longtable}

"""
    
    # Add risk priority information for this variable
    if var_results_sorted:
        max_priority = max([r.get('risk_priority', 0) for r in var_results_sorted])
        avg_priority = sum([r.get('risk_priority', 0) for r in var_results_sorted]) / len(var_results_sorted)
        
        latex_content += f"""
\\textbf{{Información de Prioridad de Riesgo:}}
\\begin{{itemize}}
\\item Puntuación de prioridad máxima: {max_priority:.1f}
\\item Puntuación de prioridad promedio: {avg_priority:.1f}
\\item Dominios analizados: {len(var_results_sorted)}
\\item Resultados significativos: {len(significant_results)}
\\end{{itemize}}

"""
    
    # Add detailed explanation for significant results
    if significant_results:
        latex_content += f"""
\\textbf{{Análisis detallado de resultados significativos para {spanish_name}:}}

"""
        
        for result in significant_results:
            domain_idx = zscore_domains.index(result['dependent_var'])
            domain_name = domain_names_spanish[domain_idx]
            
            latex_content += f"""
\\textbf{{Dominio: {domain_name}}}

"""
            
            # Add group statistics
            latex_content += r"""
\begin{center}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Grupo} & \textbf{N} & \textbf{Media} & \textbf{DE} & \textbf{Normal \%} & \textbf{Riesgo \%} \\
\hline
"""
            
            for group_name, stats in result['group_stats'].items():
                n = stats['n']
                mean = f"{stats['mean']:.2f}"
                std = f"{stats['std']:.2f}"
                normal_pct = f"{stats['risk_classification']['pct_normal']:.1f}"
                risk_pct = f"{stats['risk_classification']['pct_riesgo']:.1f}"
                
                latex_content += f"{group_name} & {n} & {mean} & {std} & {normal_pct} & {risk_pct} \\\\\n"
            
            latex_content += r"""
\hline
\end{tabular}
\end{center}

"""
            
            # Add interpretation with risk priority information
            if result['post_hoc_info']:
                latex_content += f"""
\\textbf{{Interpretación:}} {result['post_hoc_info']}. Este grupo presenta puntuaciones Z significativamente menores, indicando mayor riesgo de alteraciones en el desarrollo del dominio {domain_name.lower()}.

\\textbf{{Prioridad de Riesgo:}} {result.get('risk_priority', 0):.1f} (Riesgo máximo: {result.get('max_group_risk', 0):.1f}\\%, Riesgo promedio: {result.get('avg_group_risk', 0):.1f}\\%)

"""
            
            latex_content += r"""
\vspace{0.5cm}

"""
    
    return latex_content

def generate_summary_report(results):
    """Generate executive summary report with risk prioritization"""
    
    total_tests = len(results)
    significant_results = [r for r in results if r['significant']]
    significant_count = len(significant_results)
    
    summary = f"""
RESUMEN EJECUTIVO - ANÁLISIS ANOVA DE DESARROLLO INFANTIL (PRIORIZADO POR RIESGO)
================================================================================

ESTADÍSTICAS GENERALES:
- Total de pruebas ANOVA realizadas: {total_tests}
- Resultados significativos (p < 0.05): {significant_count}
- Porcentaje de significancia: {(significant_count/total_tests)*100:.1f}%

ANÁLISIS PRIORIZADO POR RIESGO:
Este análisis prioriza las combinaciones de variables con mayor riesgo de trastornos del desarrollo (Z ≤ -1).

COMBINACIONES CON MAYOR RIESGO DE DESARROLLO:
"""
    
    # Show top 15 highest risk combinations
    top_risk_results = sorted(results, key=lambda x: x.get('max_group_risk', 0), reverse=True)[:15]
    
    for i, result in enumerate(top_risk_results):
        domain_idx = zscore_domains.index(result['dependent_var'])
        domain_spanish = domain_names_spanish[domain_idx]
        significance_mark = "***" if result['significant'] else ""
        
        summary += f"{i+1}. {result['independent_var']} vs {domain_spanish}: "
        summary += f"Riesgo máximo={result.get('max_group_risk', 0):.1f}% "
        summary += f"(p={result['p_value']:.3f}){significance_mark}\n"
    
    summary += f"""

VARIABLES CON MAYOR NÚMERO DE ASOCIACIONES SIGNIFICATIVAS:
"""
    
    # Count significant results by independent variable
    var_significance_count = {}
    for result in significant_results:
        var_name = result['independent_var']
        var_significance_count[var_name] = var_significance_count.get(var_name, 0) + 1
    
    # Sort by significance count
    sorted_vars = sorted(var_significance_count.items(), key=lambda x: x[1], reverse=True)
    
    for var_name, count in sorted_vars[:10]:  # Top 10
        summary += f"- {var_name}: {count} dominios significativos\n"
    
    summary += f"""

DOMINIOS DEL DESARROLLO MÁS AFECTADOS:
"""
    
    # Count significant results by domain
    domain_significance_count = {}
    for result in significant_results:
        domain_name = result['dependent_var']
        domain_significance_count[domain_name] = domain_significance_count.get(domain_name, 0) + 1
    
    # Sort by significance count
    sorted_domains = sorted(domain_significance_count.items(), key=lambda x: x[1], reverse=True)
    
    for domain_name, count in sorted_domains:
        domain_idx = zscore_domains.index(domain_name)
        spanish_name = domain_names_spanish[domain_idx]
        summary += f"- {spanish_name}: {count} variables significativas\n"
    
    summary += f"""

RESULTADOS SIGNIFICATIVOS PRIORIZADOS POR RIESGO:
===============================================
"""
    
    # Show significant results ordered by risk priority
    significant_by_risk = sorted(significant_results, key=lambda x: x.get('risk_priority', 0), reverse=True)
    
    for result in significant_by_risk:
        domain_idx = zscore_domains.index(result['dependent_var'])
        domain_spanish = domain_names_spanish[domain_idx]
        
        summary += f"""
Variable: {result['independent_var']}
Dominio: {domain_spanish}
Prioridad de riesgo: {result.get('risk_priority', 0):.1f}
Riesgo máximo por grupo: {result.get('max_group_risk', 0):.1f}%
Riesgo promedio: {result.get('avg_group_risk', 0):.1f}%
Estadístico F/W: {result['f_statistic']:.3f}
P-valor: {result['p_value']:.3f}
Método: {result['test_type']}
Tamaño de muestra: {result['sample_size']}
Grupos afectados: {result['post_hoc_info']}
---
"""
    
    return summary

def save_results(results, df):
    """Save all results to files"""
    
    # Save LaTeX tables
    latex_content = generate_latex_tables(results)
    with open('resultados_anova.tex', 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    # Save summary report
    summary_content = generate_summary_report(results)
    with open('anova_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    # Save raw results as CSV for further analysis
    results_df = pd.DataFrame(results)
    results_df.to_csv('anova_results.csv', index=False)
    
    print("Results saved:")
    print("- resultados_anova.tex: LaTeX tables")
    print("- anova_summary.txt: Executive summary")
    print("- anova_results.csv: Raw results")

# =============================================================================
# Main Execution
# =============================================================================

def main():
    """Main execution function with risk-prioritized analysis"""
    
    print("=== ANÁLISIS ANOVA DE DESARROLLO INFANTIL (PRIORIZADO POR RIESGO) ===")
    print("Iniciando análisis estadístico integral con priorización por riesgo...")
    
    # Load and prepare data
    df = load_and_prepare_data()
    
    # Run risk-prioritized analysis
    results = run_complete_analysis(df)
    
    # Save results
    save_results(results, df)
    
    print("\n=== ANÁLISIS COMPLETADO ===")
    print(f"Total de pruebas realizadas: {len(results)}")
    significant_count = len([r for r in results if r['significant']])
    print(f"Resultados significativos: {significant_count}")
    print(f"Porcentaje de significancia: {(significant_count/len(results))*100:.1f}%")
    
    # Show top risk combinations
    print("\n=== TOP 5 COMBINACIONES DE MAYOR RIESGO ===")
    top_risk = sorted(results, key=lambda x: x.get('max_group_risk', 0), reverse=True)[:5]
    for i, result in enumerate(top_risk):
        domain_idx = zscore_domains.index(result['dependent_var'])
        domain_spanish = domain_names_spanish[domain_idx]
        significance = "***" if result['significant'] else ""
        print(f"{i+1}. {result['independent_var']} vs {domain_spanish}: {result.get('max_group_risk', 0):.1f}% riesgo máximo {significance}")
    
    print("\n=== ANÁLISIS PRIORIZADO POR RIESGO COMPLETADO ===")
    print("Los resultados se han organizado según prioridad de riesgo de trastornos del desarrollo.")
    print("Consulte resultados_anova.tex para el análisis detallado.")

if __name__ == "__main__":
    main()