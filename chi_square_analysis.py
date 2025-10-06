#!/usr/bin/env python3
"""
Comprehensive Chi-Square Analysis for Neurodevelopmental Risk Factors
=====================================================================

This script performs a comprehensive chi-square analysis on the datos_optimizados.csv dataset
to identify associations between predictor variables and developmental domain scores.

Author: AI Assistant
Date: 2024
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

class ChiSquareAnalysis:
    """
    A comprehensive chi-square analysis class for neurodevelopmental risk factors.
    """
    
    def __init__(self, data_path='datos_optimizados.csv'):
        """Initialize the analysis with the dataset."""
        self.data_path = data_path
        self.data = None
        self.results = {}
        self.significant_results = {}
        
        # Demographics - updated to use cleaned version
        self.demographics = [
            'edad_meses_nino_numeric', 'edad_anos_madre', 'edad_anos_padre', 
            'grupo_etnico', 'area_residencia'
        ]
        
        self.education = [
            'nivel_educativo_madre', 'nivel_educativo_padre'
        ]
        
        self.housing = [
            'fuente_agua_consumo', 'tipo_sanitario', 'manejo_basura',
            'tipo_energia_luz', 'tipo_energia_cocina', 'propiedad_vivienda'
        ]
        
        self.household = [
            'sexo_jefe_hogar', 'situacion_laboral_madre', 'situacion_laboral_padre',
            'tipo_empleo_madre', 'tipo_empleo_padre', 'seguro_social',
            'total_personas_hogar', 'total_hermanos', 'posicion_nino_hermanos',
            'estado_civil_cuidador'
        ]
        
        self.child_activities = [
            'horas_pantalla', 'horas_juego_cuidador'
        ]
        
        self.prenatal_care = [
            'numero_controles_prenatales', 'ultrasonido_embarazo',
            'prenatales_primeros_3_meses', 'prenatales_resto_embarazo'
        ]
        
        self.birth_care = [
            'servicio_asistencia_parto', 'tipo_parto', 'razon_cesarea_emergencia',
            'lactancia_primeros_6_meses', 'lactancia_6-12_meses', 'lactancia_12-24_meses'
        ]
        
        self.nutrition = [
            'vitamina_a_6-12_meses', 'vitamina_a_12-18_meses', 'vitamina_a_18-24_meses',
            'vitaminas_minerales_6-12_meses', 'vitaminas_minerales_12-18_meses',
            'vitaminas_minerales_18-24_meses'
        ]
        
        self.health_outcomes = [
            'retardo_crecimiento', 'desnutricion_aguda', 'hospitalizado_neonatal',
            'razon_hospitalizado_neonatal', 'hospitalizado_infancia',
            'razon_hospitalizado_infancia', 'vacunacion_completa'
        ]
        
        # All predictor variables
        self.predictor_vars = (
            self.demographics + self.education + self.housing + self.household + 
            self.child_activities + self.prenatal_care + self.birth_care + 
            self.nutrition + self.health_outcomes
        )
        
        # Developmental domain z-scores
        self.developmental_domains = [
            'zscore_desarrollo_comunicacion',
            'zscore_desarrollo_motricidad_gruesa',
            'zscore_desarrollo_motricidad_fina',
            'zscore_desarrollo_resolucion_problemas',
            'zscore_desarrollo_socio_individual'
        ]
        
    def load_data(self):
        """Load and prepare the dataset."""
        print("Loading data...")
        self.data = pd.read_csv(self.data_path)
        print(f"Dataset loaded: {self.data.shape[0]} rows, {self.data.shape[1]} columns")
        
        # Display basic info
        print("\nDataset overview:")
        print(self.data.info())
        
        return self.data
    
    def categorize_developmental_scores(self):
        """
        Categorize developmental z-scores into risk categories:
        - Z ≥ -1: Adequate development
        - -2 ≤ Z < -1: Risk of neurodevelopmental disorders
        - Z < -2: High risk of neurodevelopmental disorders
        """
        print("\nCategorizing developmental scores...")
        
        for domain in self.developmental_domains:
            if domain in self.data.columns:
                # Create categorical version
                cat_domain = domain.replace('zscore_desarrollo_', 'cat_zscore_desarrollo_')
                
                conditions = [
                    self.data[domain] >= -1,
                    (self.data[domain] >= -2) & (self.data[domain] < -1),
                    self.data[domain] < -2
                ]
                
                choices = [
                    'Adequate development',
                    'Risk of neurodevelopmental disorders',
                    'High risk of neurodevelopmental disorders'
                ]
                
                self.data[cat_domain] = np.select(conditions, choices, default=None)
                
                # Display distribution
                print(f"\n{domain} categorization:")
                print(self.data[cat_domain].value_counts(dropna=False))
        
        return self.data
    
    def prepare_categorical_variables(self):
        """Prepare categorical variables for analysis."""
        print("\nPreparing categorical variables...")
        
        # First clean edad_meses_nino column by extracting numeric values
        if 'edad_meses_nino' in self.data.columns:
            self.data['edad_meses_nino_numeric'] = self.data['edad_meses_nino'].str.extract(r'(\d+)').astype(int)
        
        # Convert continuous variables to categorical if needed
        continuous_vars = ['edad_meses_nino_numeric', 'edad_anos_madre', 'edad_anos_padre',
                          'total_personas_hogar', 'total_hermanos', 'posicion_nino_hermanos',
                          'horas_pantalla', 'horas_juego_cuidador', 'numero_controles_prenatales']
        
        for var in continuous_vars:
            if var in self.data.columns:
                if var in ['edad_meses_nino_numeric']:
                    # Age in months - create age groups
                    self.data[f'cat_{var}'] = pd.cut(self.data[var], 
                                                    bins=[0, 12, 24, 36, 48, 60], 
                                                    labels=['0-12 months', '13-24 months', '25-36 months', 
                                                           '37-48 months', '49-60 months'])
                elif var in ['edad_anos_madre', 'edad_anos_padre']:
                    # Parental age - create age groups
                    self.data[f'cat_{var}'] = pd.cut(self.data[var], 
                                                    bins=[0, 20, 30, 40, 100], 
                                                    labels=['<20 years', '20-30 years', '31-40 years', '>40 years'])
                elif var in ['total_personas_hogar', 'total_hermanos']:
                    # Household size and siblings
                    self.data[f'cat_{var}'] = pd.cut(self.data[var], 
                                                    bins=[0, 2, 4, 6, 100], 
                                                    labels=['1-2', '3-4', '5-6', '>6'])
                elif var in ['horas_pantalla', 'horas_juego_cuidador']:
                    # Screen time and play time
                    self.data[f'cat_{var}'] = pd.cut(self.data[var], 
                                                    bins=[0, 1, 3, 5, 100], 
                                                    labels=['0-1 hours', '2-3 hours', '4-5 hours', '>5 hours'])
                elif var == 'numero_controles_prenatales':
                    # Prenatal controls
                    self.data[f'cat_{var}'] = pd.cut(self.data[var], 
                                                    bins=[0, 4, 8, 12, 100], 
                                                    labels=['0-4 controls', '5-8 controls', '9-12 controls', '>12 controls'])
                else:
                    # Generic categorization for other continuous variables
                    try:
                        self.data[f'cat_{var}'] = pd.qcut(self.data[var], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'], duplicates='drop')
                    except ValueError:
                        # If qcut fails, use regular cut or just use the original variable
                        unique_vals = self.data[var].nunique()
                        if unique_vals <= 4:
                            self.data[f'cat_{var}'] = self.data[var].astype(str)
                        else:
                            self.data[f'cat_{var}'] = pd.cut(self.data[var], bins=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
        
        return self.data
    
    def cramers_v(self, x, y):
        """Calculate Cramér's V for effect size."""
        confusion_matrix = pd.crosstab(x, y)
        chi2 = chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2 / n
        r, k = confusion_matrix.shape
        phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
        rcorr = r - ((r-1)**2)/(n-1)
        kcorr = k - ((k-1)**2)/(n-1)
        return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))
    
    def perform_chi_square_tests(self):
        """Perform chi-square tests for all predictor-domain combinations."""
        print("\nPerforming chi-square tests...")
        
        # Get categorical developmental domains
        cat_domains = [col for col in self.data.columns if col.startswith('cat_zscore_')]
        
        # Prepare predictor variables (use categorical versions where available)
        predictors_to_test = []
        for var in self.predictor_vars:
            if var in self.data.columns:
                cat_var = f'cat_{var}'
                if cat_var in self.data.columns:
                    predictors_to_test.append(cat_var)
                else:
                    predictors_to_test.append(var)
        
        # Perform tests
        results = []
        total_tests = len(predictors_to_test) * len(cat_domains)
        test_count = 0
        
        print(f"Running {total_tests} chi-square tests...")
        
        for predictor in predictors_to_test:
            for domain in cat_domains:
                test_count += 1
                if test_count % 20 == 0:
                    print(f"Progress: {test_count}/{total_tests} tests completed")
                
                # Skip if either variable has too many missing values
                if self.data[predictor].isna().sum() > len(self.data) * 0.5:
                    continue
                if self.data[domain].isna().sum() > len(self.data) * 0.5:
                    continue
                
                # Create contingency table
                contingency_table = pd.crosstab(self.data[predictor], self.data[domain], dropna=False)
                
                # Skip if contingency table is too small or has zero cells
                if contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
                    continue
                
                # Check for zero cells and minimum expected frequency
                if (contingency_table == 0).any().any():
                    continue
                
                # Check expected frequencies before performing chi-square test
                try:
                    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
                    
                    # Check if any expected frequency is less than 5
                    if np.any(expected < 5):
                        continue
                    
                except ValueError:
                    # Skip if chi-square test fails due to data issues
                    continue
                
                # Calculate effect size
                cramers_v = self.cramers_v(self.data[predictor].dropna(), self.data[domain].dropna())
                
                # Store results
                result = {
                    'predictor': predictor,
                    'domain': domain,
                    'chi2_statistic': chi2,
                    'p_value': p_value,
                    'degrees_of_freedom': dof,
                    'cramers_v': cramers_v,
                    'n_observations': contingency_table.sum().sum(),
                    'contingency_table': contingency_table
                }
                
                results.append(result)
        
        # Convert to DataFrame
        self.results = pd.DataFrame(results)
        
        # Apply Bonferroni correction
        if len(self.results) > 0:
            self.results['p_value_bonferroni'] = self.results['p_value'] * len(self.results)
            self.results['p_value_bonferroni'] = self.results['p_value_bonferroni'].clip(upper=1.0)
            
            # Identify significant results
            self.significant_results = self.results[self.results['p_value_bonferroni'] < 0.05].copy()
            self.significant_results = self.significant_results.sort_values('p_value_bonferroni')
        
        print(f"\nCompleted {len(self.results)} chi-square tests")
        print(f"Found {len(self.significant_results)} significant associations (p < 0.05 after Bonferroni correction)")
        
        return self.results
    
    def create_summary_tables(self):
        """Create summary tables of results."""
        print("\nCreating summary tables...")
        
        # Overall summary
        summary_stats = {
            'Total tests performed': len(self.results),
            'Significant associations (p < 0.05)': len(self.results[self.results['p_value'] < 0.05]) if len(self.results) > 0 else 0,
            'Significant after Bonferroni correction': len(self.significant_results),
            'Mean effect size (Cramér\'s V)': self.results['cramers_v'].mean() if len(self.results) > 0 else 0,
            'Max effect size (Cramér\'s V)': self.results['cramers_v'].max() if len(self.results) > 0 else 0
        }
        
        print("\nOverall Summary:")
        for key, value in summary_stats.items():
            print(f"{key}: {value}")
        
        # Summary by domain
        print("\nSignificant associations by developmental domain:")
        if len(self.significant_results) > 0:
            domain_summary = self.significant_results.groupby('domain').agg({
                'p_value_bonferroni': 'count',
                'cramers_v': 'mean'
            }).round(4)
            domain_summary.columns = ['Count', 'Mean_Cramers_V']
            print(domain_summary)
        
        # Top significant associations
        print("\nTop 10 most significant associations:")
        if len(self.significant_results) > 0:
            top_results = self.significant_results.head(10)[['predictor', 'domain', 'chi2_statistic', 
                                                            'p_value_bonferroni', 'cramers_v', 'n_observations']]
            print(top_results.to_string(index=False))
        
        return summary_stats
    
    def create_visualizations(self):
        """Create visualizations for significant results."""
        print("\nCreating visualizations...")
        
        if len(self.significant_results) == 0:
            print("No significant results to visualize.")
            return
        
        # Set up the plotting style
        plt.style.use('default')
        sns.set_palette("husl")
        
        # 1. Heatmap of p-values
        fig, axes = plt.subplots(2, 2, figsize=(20, 16))
        
        # Pivot table for heatmap
        if len(self.results) > 0:
            heatmap_data = self.results.pivot_table(
                index='predictor', 
                columns='domain', 
                values='p_value_bonferroni', 
                fill_value=1.0
            )
            
            # Log transform p-values for better visualization
            heatmap_data_log = -np.log10(heatmap_data)
            
            sns.heatmap(heatmap_data_log, 
                       annot=False, 
                       cmap='viridis', 
                       ax=axes[0,0],
                       cbar_kws={'label': '-log10(p-value)'})
            axes[0,0].set_title('Chi-square Test Results: -log10(p-values)', fontsize=14)
            axes[0,0].set_xlabel('Developmental Domains')
            axes[0,0].set_ylabel('Predictor Variables')
        
        # 2. Effect sizes heatmap
        if len(self.results) > 0:
            effect_data = self.results.pivot_table(
                index='predictor', 
                columns='domain', 
                values='cramers_v', 
                fill_value=0
            )
            
            sns.heatmap(effect_data, 
                       annot=False, 
                       cmap='Blues', 
                       ax=axes[0,1],
                       cbar_kws={'label': 'Cramér\'s V'})
            axes[0,1].set_title('Effect Sizes (Cramér\'s V)', fontsize=14)
            axes[0,1].set_xlabel('Developmental Domains')
            axes[0,1].set_ylabel('Predictor Variables')
        
        # 3. Distribution of effect sizes
        if len(self.results) > 0:
            axes[1,0].hist(self.results['cramers_v'], bins=20, alpha=0.7, color='skyblue')
            axes[1,0].axvline(self.results['cramers_v'].mean(), color='red', linestyle='--', 
                             label=f'Mean: {self.results["cramers_v"].mean():.3f}')
            axes[1,0].set_xlabel('Cramér\'s V')
            axes[1,0].set_ylabel('Frequency')
            axes[1,0].set_title('Distribution of Effect Sizes')
            axes[1,0].legend()
        
        # 4. Significant associations by domain
        if len(self.significant_results) > 0:
            domain_counts = self.significant_results['domain'].value_counts()
            axes[1,1].bar(range(len(domain_counts)), domain_counts.values)
            axes[1,1].set_xticks(range(len(domain_counts)))
            axes[1,1].set_xticklabels(domain_counts.index, rotation=45, ha='right')
            axes[1,1].set_ylabel('Number of Significant Associations')
            axes[1,1].set_title('Significant Associations by Developmental Domain')
        
        plt.tight_layout()
        plt.savefig('chi_square_analysis_overview.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Create individual plots for top significant associations
        self.create_individual_plots()
    
    def create_individual_plots(self):
        """Create individual plots for top significant associations."""
        if len(self.significant_results) == 0:
            return
        
        # Plot top 6 most significant associations
        top_results = self.significant_results.head(6)
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, (_, result) in enumerate(top_results.iterrows()):
            predictor = result['predictor']
            domain = result['domain']
            
            # Create contingency table
            contingency_table = pd.crosstab(self.data[predictor], self.data[domain], dropna=False)
            
            # Create percentage table for better visualization
            percentage_table = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100
            
            # Plot stacked bar chart
            percentage_table.plot(kind='bar', stacked=True, ax=axes[i])
            axes[i].set_title(f'{predictor} vs {domain}\nχ² = {result["chi2_statistic"]:.3f}, p = {result["p_value_bonferroni"]:.3e}')
            axes[i].set_xlabel(predictor.replace('_', ' ').title())
            axes[i].set_ylabel('Percentage')
            axes[i].legend(title=domain.replace('_', ' ').title(), bbox_to_anchor=(1.05, 1), loc='upper left')
            axes[i].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('top_significant_associations.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_report(self):
        """Generate a comprehensive report."""
        print("\nGenerating comprehensive report...")
        
        report = []
        report.append("=" * 80)
        report.append("COMPREHENSIVE CHI-SQUARE ANALYSIS REPORT")
        report.append("Neurodevelopmental Risk Factors Analysis")
        report.append("=" * 80)
        
        # Dataset overview
        report.append("\n1. DATASET OVERVIEW")
        report.append("-" * 40)
        report.append(f"Total observations: {len(self.data)}")
        report.append(f"Total variables: {len(self.data.columns)}")
        report.append(f"Predictor variables analyzed: {len(self.predictor_vars)}")
        report.append(f"Developmental domains: {len(self.developmental_domains)}")
        
        # Analysis summary
        report.append("\n2. ANALYSIS SUMMARY")
        report.append("-" * 40)
        report.append(f"Total chi-square tests performed: {len(self.results)}")
        report.append(f"Significant associations (p < 0.05): {len(self.results[self.results['p_value'] < 0.05])}")
        report.append(f"Significant after Bonferroni correction: {len(self.significant_results)}")
        
        if len(self.results) > 0:
            report.append(f"Mean effect size (Cramér's V): {self.results['cramers_v'].mean():.4f}")
            report.append(f"Maximum effect size (Cramér's V): {self.results['cramers_v'].max():.4f}")
        
        # Significant results
        if len(self.significant_results) > 0:
            report.append("\n3. SIGNIFICANT ASSOCIATIONS (After Bonferroni correction)")
            report.append("-" * 60)
            
            for i, (_, result) in enumerate(self.significant_results.iterrows(), 1):
                report.append(f"\n{i}. {result['predictor']} → {result['domain']}")
                report.append(f"   χ² = {result['chi2_statistic']:.3f}, p = {result['p_value_bonferroni']:.3e}")
                report.append(f"   Effect size (Cramér's V) = {result['cramers_v']:.4f}")
                report.append(f"   Sample size = {result['n_observations']}")
        
        # Developmental domain summary
        report.append("\n4. SUMMARY BY DEVELOPMENTAL DOMAIN")
        report.append("-" * 50)
        
        for domain in [col for col in self.data.columns if col.startswith('cat_zscore_')]:
            domain_results = self.significant_results[self.significant_results['domain'] == domain]
            report.append(f"\n{domain}:")
            report.append(f"  Significant associations: {len(domain_results)}")
            
            if len(domain_results) > 0:
                report.append(f"  Mean effect size: {domain_results['cramers_v'].mean():.4f}")
                report.append("  Top predictors:")
                for _, result in domain_results.head(3).iterrows():
                    report.append(f"    - {result['predictor']} (V = {result['cramers_v']:.4f})")
        
        # Risk factors summary
        report.append("\n5. KEY RISK FACTORS IDENTIFIED")
        report.append("-" * 40)
        
        if len(self.significant_results) > 0:
            # Group by predictor to find most impactful variables
            predictor_summary = self.significant_results.groupby('predictor').agg({
                'domain': 'count',
                'cramers_v': 'mean'
            }).sort_values('cramers_v', ascending=False)
            
            report.append("Variables with strongest associations across domains:")
            for predictor, data in predictor_summary.head(10).iterrows():
                report.append(f"  - {predictor}: {data['domain']} domains affected, mean V = {data['cramers_v']:.4f}")
        
        # Recommendations
        report.append("\n6. RECOMMENDATIONS")
        report.append("-" * 30)
        report.append("Based on the analysis, the following recommendations are made:")
        
        if len(self.significant_results) > 0:
            report.append("1. Focus intervention programs on the identified high-risk factors")
            report.append("2. Implement targeted screening for children with multiple risk factors")
            report.append("3. Develop domain-specific interventions based on the strongest associations")
            report.append("4. Consider the cumulative effect of multiple risk factors")
            report.append("5. Prioritize preventive measures for modifiable risk factors")
        else:
            report.append("1. Consider increasing sample size for more robust statistical power")
            report.append("2. Explore alternative statistical methods for small effect sizes")
            report.append("3. Review data quality and missing data patterns")
        
        # Save report
        with open('chi_square_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        print('\n'.join(report))
        print(f"\nReport saved to: chi_square_analysis_report.txt")
        
        return report
    
    def save_detailed_results(self):
        """Save detailed results to CSV files."""
        print("\nSaving detailed results...")
        
        # All results
        if len(self.results) > 0:
            self.results.to_csv('chi_square_all_results.csv', index=False)
            print("All results saved to: chi_square_all_results.csv")
        
        # Significant results
        if len(self.significant_results) > 0:
            self.significant_results.to_csv('chi_square_significant_results.csv', index=False)
            print("Significant results saved to: chi_square_significant_results.csv")
        
        # Contingency tables for significant results
        if len(self.significant_results) > 0:
            with open('contingency_tables.txt', 'w') as f:
                f.write("CONTINGENCY TABLES FOR SIGNIFICANT ASSOCIATIONS\n")
                f.write("=" * 60 + "\n\n")
                
                for i, (_, result) in enumerate(self.significant_results.iterrows(), 1):
                    f.write(f"{i}. {result['predictor']} vs {result['domain']}\n")
                    f.write(f"χ² = {result['chi2_statistic']:.3f}, p = {result['p_value_bonferroni']:.3e}\n")
                    f.write(f"Cramér's V = {result['cramers_v']:.4f}\n\n")
                    
                    # Get contingency table
                    contingency_table = pd.crosstab(
                        self.data[result['predictor']], 
                        self.data[result['domain']], 
                        dropna=False
                    )
                    
                    f.write(contingency_table.to_string())
                    f.write("\n\n" + "-" * 60 + "\n\n")
            
            print("Contingency tables saved to: contingency_tables.txt")
    
    def run_complete_analysis(self):
        """Run the complete chi-square analysis."""
        print("Starting comprehensive chi-square analysis...")
        print("=" * 60)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Categorize developmental scores
        self.categorize_developmental_scores()
        
        # Step 3: Prepare categorical variables
        self.prepare_categorical_variables()
        
        # Step 4: Perform chi-square tests
        self.perform_chi_square_tests()
        
        # Step 5: Create summary tables
        self.create_summary_tables()
        
        # Step 6: Create visualizations
        self.create_visualizations()
        
        # Step 7: Generate report
        self.generate_report()
        
        # Step 8: Save detailed results
        self.save_detailed_results()
        
        print("\nAnalysis completed successfully!")
        print("=" * 60)
        
        return self.results, self.significant_results


def main():
    """Main function to run the analysis."""
    # Create analysis instance
    analysis = ChiSquareAnalysis()
    
    # Run complete analysis
    results, significant_results = analysis.run_complete_analysis()
    
    return analysis, results, significant_results


if __name__ == "__main__":
    analysis, results, significant_results = main()