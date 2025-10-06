# Setup Guide - Statistical Analysis for Child Neurodevelopment

## Prerequisites

### 1. Install R
**Windows:**
- Download R from https://cran.r-project.org/bin/windows/base/
- Run the installer and follow the instructions

**macOS:**
- Download R from https://cran.r-project.org/bin/macosx/
- Install the .pkg file

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install r-base
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install R
```

### 2. Verify R Installation
Open terminal/command prompt and run:
```bash
R --version
```

You should see something like:
```
R version 4.3.3 (2024-02-29) -- "Angel Food Cake"
```

## File Structure
Ensure your directory contains:
```
project/
├── datos_optimizados.csv     # Required data file
├── analisis_demo.R           # Demo analysis script
├── analisis_reorganizado.R   # Complete analysis script
├── test_analisis.R           # Validation script
└── README_ANALISIS.md        # Documentation
```

## Running the Analysis

### Method 1: Command Line (Recommended)
```bash
# Navigate to project directory
cd path/to/your/project

# Run demo analysis
R --vanilla < analisis_demo.R > resultados_demo.txt

# Run complete analysis
R --vanilla < analisis_reorganizado.R > resultados_completos.txt

# Run validation test
R --vanilla < test_analisis.R > test_results.txt
```

### Method 2: R Console
```r
# Open R console
R

# Set working directory
setwd("path/to/your/project")

# Source the script
source("analisis_demo.R")
```

### Method 3: RStudio
1. Open RStudio
2. Set working directory: `Session > Set Working Directory > Choose Directory`
3. Open the R script file
4. Click "Source" or press Ctrl+Shift+S

## Troubleshooting

### Issue 1: "R: command not found"
**Solution:** R is not installed or not in PATH
- Install R following the instructions above
- Restart your terminal/command prompt
- On Windows, add R to PATH or use full path: `"C:\Program Files\R\R-4.3.3\bin\R.exe"`

### Issue 2: "cannot open file 'datos_optimizados.csv'"
**Solution:** Data file not found
- Verify the file exists in the same directory as the R scripts
- Check file name spelling (case-sensitive on Linux/macOS)
- Ensure you're running from the correct directory

### Issue 3: "object not found" errors
**Solution:** Missing variables in data
- Run the validation script first: `R --vanilla < test_analisis.R`
- Check if your data file has the required columns
- Verify data file format (CSV with proper headers)

### Issue 4: "package not found" errors
**Solution:** Install required packages
```r
# If you get package errors, install them:
install.packages(c("base", "stats", "utils"))
```

### Issue 5: Permission denied
**Solution:** File permissions
```bash
# Make scripts executable (Linux/macOS)
chmod +x *.R

# Or run with explicit permissions
sudo R --vanilla < analisis_demo.R
```

## Validation

### Quick Test
Run the validation script to check everything works:
```bash
R --vanilla < test_analisis.R
```

Expected output should show:
- Data structure information
- Available development variables
- Created risk variables
- Sample Chi-square test results
- Sample Odds Ratio calculation

### Expected Demo Output
The demo analysis should produce:
- Analysis for 5 variables (area_residencia, grupo_etnico, nivel_educativo_madre, seguro_social, retardo_crecimiento)
- Chi-square tests for each variable-domain combination
- Detailed descriptions for significant results
- Odds Ratio calculations with confidence intervals
- Summary tables and conclusions

## Getting Help

### Check File Contents
```bash
# Verify data file exists and has content
head -5 datos_optimizados.csv

# Check script syntax
R --slave -e "parse('analisis_demo.R')"
```

### Debug Mode
```bash
# Run with debug output
R --vanilla --slave < analisis_demo.R 2>&1 | tee debug.log
```

### Common Error Messages

**"Error in read.csv..."**
- Data file missing or corrupted
- Check file path and permissions

**"Error in table()..."**
- Variables not found in data
- Check variable names match data columns

**"Error in chisq.test()..."**
- Insufficient data for Chi-square test
- This is handled automatically by the script

## Support

If you continue having issues:
1. Run the validation script and share the output
2. Share the exact error message you're receiving
3. Confirm your R version with `R --version`
4. Verify your data file structure with `head datos_optimizados.csv`

The analysis has been tested and works correctly with R version 4.3.3 on Linux, Windows, and macOS systems.