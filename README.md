# Comprehensive Chi-Square Analysis of Neurodevelopmental Risk Factors

This repository contains a comprehensive chi-square analysis of neurodevelopmental risk factors using the `datos_optimizados.csv` dataset. The analysis identifies associations between predictor variables and developmental domain scores to understand key risk factors for neurodevelopmental disorders.

## 📊 Analysis Overview

- **Dataset**: 1,725 observations with 57 variables
- **Developmental Domains**: 5 domains analyzed (Communication, Gross Motor, Fine Motor, Problem Solving, Socio-Individual)
- **Statistical Tests**: 29 chi-square tests performed
- **Significant Associations**: 9 associations found after Bonferroni correction
- **Risk Categorization**: Z-scores categorized into three risk levels

## 🎯 Key Findings

### Motor Development Most Affected
- **Gross Motor Development**: 6 significant associations
- **Fine Motor Development**: 3 significant associations  
- **Other Domains**: No significant associations found

### Primary Risk Factors Identified
1. **Nutrition Variables**: Vitamin A and mineral supplementation status
2. **Geographic Location**: Rural vs. urban residence (strongest effect size: 0.1092)
3. **Age-specific Supplementation**: Different effects across age groups

### Top Significant Associations
1. Vitamin A (6-12 months) → Gross Motor Development (χ² = 81.157, p = 2.872e-15)
2. Vitamins/Minerals (6-12 months) → Gross Motor Development (χ² = 80.873, p = 3.299e-15)
3. Vitamins/Minerals (12-18 months) → Gross Motor Development (χ² = 28.881, p = 2.396e-04)
4. Area of Residence → Gross Motor Development (χ² = 22.558, p = 3.664e-04)

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy scipy matplotlib seaborn
```

### Running the Analysis
```bash
python chi_square_analysis.py
```

### Viewing Summary
```bash
python summary_findings.py
```

## 📁 Generated Files

| File | Description |
|------|-------------|
| `chi_square_analysis.py` | Complete analysis script |
| `chi_square_analysis_report.txt` | Detailed written report |
| `chi_square_significant_results.csv` | Significant associations data |
| `chi_square_all_results.csv` | All test results |
| `contingency_tables.txt` | Detailed contingency tables |
| `chi_square_analysis_overview.png` | Overview visualization |
| `top_significant_associations.png` | Top associations visualization |
| `summary_findings.py` | Summary display script |

## 📈 Statistical Methods

### Risk Categorization
- **Z ≥ -1**: Adequate development
- **-2 ≤ Z < -1**: Risk of neurodevelopmental disorders  
- **Z < -2**: High risk of neurodevelopmental disorders

### Statistical Tests
- **Test**: Chi-square test of independence
- **Multiple Testing Correction**: Bonferroni method
- **Effect Size**: Cramér's V
- **Significance Level**: p < 0.05 (after correction)

### Data Quality Checks
- Expected frequencies ≥ 5 for valid chi-square tests
- Missing data handled appropriately
- Zero-frequency cells excluded

## 💡 Clinical Recommendations

1. **🎯 Focus on Motor Development**: Prioritize screening and intervention for motor skills
2. **💊 Nutrition Interventions**: Ensure adequate vitamin A and mineral supplementation
3. **🏘️ Geographic Targeting**: Implement specialized programs for rural populations
4. **👶 Early Intervention**: Screen for multiple risk factors in early childhood
5. **📋 Comprehensive Assessment**: Include nutrition and socioeconomic factors in evaluations

## 📊 Variables Analyzed

### Predictor Variables (48 total)
- **Demographics**: Age, ethnicity, residence area
- **Education**: Parental education levels
- **Housing**: Water source, sanitation, energy type
- **Household**: Family structure, employment status
- **Child Activities**: Screen time, play time with caregiver
- **Prenatal Care**: Controls, ultrasounds, timing
- **Birth/Early Care**: Delivery type, breastfeeding
- **Nutrition**: Vitamin A, minerals supplementation
- **Health Outcomes**: Growth, hospitalization, vaccination

### Developmental Domains
- Communication Development
- Gross Motor Development
- Fine Motor Development
- Problem Solving Development
- Socio-Individual Development

## 🔬 Technical Details

### Implementation Features
- Robust error handling for sparse contingency tables
- Automatic categorization of continuous variables
- Comprehensive visualization generation
- Detailed statistical reporting
- Export capabilities for further analysis

### Code Structure
```python
class ChiSquareAnalysis:
    - load_data()
    - categorize_developmental_scores()
    - prepare_categorical_variables()
    - perform_chi_square_tests()
    - create_visualizations()
    - generate_report()
```

## 📋 Usage Examples

### Basic Analysis
```python
from chi_square_analysis import ChiSquareAnalysis

# Create analysis instance
analysis = ChiSquareAnalysis('datos_optimizados.csv')

# Run complete analysis
results, significant_results = analysis.run_complete_analysis()
```

### Custom Analysis
```python
# Load and prepare data
analysis.load_data()
analysis.categorize_developmental_scores()
analysis.prepare_categorical_variables()

# Run specific tests
results = analysis.perform_chi_square_tests()

# Generate visualizations
analysis.create_visualizations()
```

## 🎨 Visualizations

The analysis generates two main visualizations:

1. **Overview Dashboard**: Heatmaps of p-values and effect sizes
2. **Top Associations**: Bar charts of significant relationships

## 📄 License

This analysis is part of a thesis project on neurodevelopmental risk factors.

## 🤝 Contributing

For questions or suggestions regarding the analysis methodology or findings, please open an issue in the repository.

---

*Analysis completed using Python 3.12 with pandas, numpy, scipy, matplotlib, and seaborn.*