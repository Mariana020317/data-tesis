# ANÁLISIS EXHAUSTIVO DE CHI-CUADRADO
## Asociaciones entre Variables Categóricas y Dominios del Neurodesarrollo
================================================================================

**Dataset:** 1725 observaciones, 62 variables
**Variables categóricas analizadas:** 50
**Dominios del neurodesarrollo:** 5

**Criterios de categorización de riesgo:**
- Desarrollo adecuado: Z ≥ -1
- Riesgo de trastornos: -2 ≤ Z < -1
- Alto riesgo: Z < -2

**Nota:** Se ignoran completamente los valores faltantes en todos los análisis.



## 1. ANÁLISIS DE LA VARIABLE: CENTRO_ATENCION_SALUD

### Variable: centro_atencion_salud
==================================================

**Distribución de la variable centro_atencion_salud:**
- Puesto de salud de Pacajá: 832 (48.2%)
- Centro de salud de Quetzaltenango: 719 (41.7%)
- Puesto de salud de San José Chiquilajá: 174 (10.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
centro_atencion_salud                                                                                 
Centro de salud de Quetzaltenango                   5                  678                    36   719
Puesto de salud de Pacajá                           7                  791                    34   832
Puesto de salud de San José Chiquilajá              2                  159                    13   174
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
centro_atencion_salud                                                                           
Centro de salud de Quetzaltenango                 0.7                 94.3                   5.0
Puesto de salud de Pacajá                         0.8                 95.1                   4.1
Puesto de salud de San José Chiquilajá            1.1                 91.4                   7.5

**Estadísticos:**
- Chi-cuadrado: 4.106
- Valor p: 0.392
- Grados de libertad: 4

**Interpretación:**
La asociación entre centro_atencion_salud y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.106, p = 0.392).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
centro_atencion_salud                                                                                      
Centro de salud de Quetzaltenango                       19                  622                    78   719
Puesto de salud de Pacajá                               27                  669                   136   832
Puesto de salud de San José Chiquilajá                   8                  146                    20   174
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
centro_atencion_salud                                                                                
Centro de salud de Quetzaltenango                      2.6                 86.5                  10.8
Puesto de salud de Pacajá                              3.2                 80.4                  16.3
Puesto de salud de San José Chiquilajá                 4.6                 83.9                  11.5

**Estadísticos:**
- Chi-cuadrado: 12.715
- Valor p: 0.013
- Grados de libertad: 4

**Interpretación:**
La asociación entre centro_atencion_salud y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.715, p = 0.013).

**Análisis por categorías:**
- **Puesto de salud de San José Chiquilajá** muestra la mayor proporción de alto riesgo (4.6%)
- **Centro de salud de Quetzaltenango** muestra la mayor proporción de desarrollo adecuado (86.5%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
centro_atencion_salud                                                                                    
Centro de salud de Quetzaltenango                     10                  645                    64   719
Puesto de salud de Pacajá                             11                  778                    43   832
Puesto de salud de San José Chiquilajá                 3                  154                    17   174
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
centro_atencion_salud                                                                              
Centro de salud de Quetzaltenango                    1.4                 89.7                   8.9
Puesto de salud de Pacajá                            1.3                 93.5                   5.2
Puesto de salud de San José Chiquilajá               1.7                 88.5                   9.8

**Estadísticos:**
- Chi-cuadrado: 10.228
- Valor p: 0.037
- Grados de libertad: 4

**Interpretación:**
La asociación entre centro_atencion_salud y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.228, p = 0.037).

**Análisis por categorías:**
- **Puesto de salud de San José Chiquilajá** muestra la mayor proporción de alto riesgo (1.7%)
- **Puesto de salud de Pacajá** muestra la mayor proporción de desarrollo adecuado (93.5%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
centro_atencion_salud                                                                                         
Centro de salud de Quetzaltenango                           4                  672                    43   719
Puesto de salud de Pacajá                                   4                  777                    51   832
Puesto de salud de San José Chiquilajá                      4                  148                    22   174
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
centro_atencion_salud                                                                                   
Centro de salud de Quetzaltenango                         0.6                 93.5                   6.0
Puesto de salud de Pacajá                                 0.5                 93.4                   6.1
Puesto de salud de San José Chiquilajá                    2.3                 85.1                  12.6

**Estadísticos:**
- Chi-cuadrado: 18.460
- Valor p: 0.001
- Grados de libertad: 4

**Interpretación:**
La asociación entre centro_atencion_salud y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 18.460, p = 0.001).

**Análisis por categorías:**
- **Puesto de salud de San José Chiquilajá** muestra la mayor proporción de alto riesgo (2.3%)
- **Centro de salud de Quetzaltenango** muestra la mayor proporción de desarrollo adecuado (93.5%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
centro_atencion_salud                                                                                     
Centro de salud de Quetzaltenango                       8                  675                    36   719
Puesto de salud de Pacajá                               7                  765                    60   832
Puesto de salud de San José Chiquilajá                  2                  160                    12   174
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
centro_atencion_salud                                                                               
Centro de salud de Quetzaltenango                     1.1                 93.9                   5.0
Puesto de salud de Pacajá                             0.8                 91.9                   7.2
Puesto de salud de San José Chiquilajá                1.1                 92.0                   6.9

**Estadísticos:**
- Chi-cuadrado: 3.629
- Valor p: 0.459
- Grados de libertad: 4

**Interpretación:**
La asociación entre centro_atencion_salud y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.629, p = 0.459).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 2. ANÁLISIS DE LA VARIABLE: SEXO_NINO

### Variable: sexo_nino
==================================================

**Distribución de la variable sexo_nino:**
- Masculino: 922 (53.4%)
- Femenino: 803 (46.6%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_nino                                                                                             
Femenino                                            4                  765                    34   803
Masculino                                          10                  863                    49   922
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_nino                                                                                       
Femenino                                          0.5                 95.3                   4.2
Masculino                                         1.1                 93.6                   5.3

**Estadísticos:**
- Chi-cuadrado: 2.986
- Valor p: 0.225
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_nino y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.986, p = 0.225).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_nino                                                                                                  
Femenino                                                29                  669                   105   803
Masculino                                               25                  768                   129   922
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_nino                                                                                            
Femenino                                               3.6                 83.3                  13.1
Masculino                                              2.7                 83.3                  14.0

**Estadísticos:**
- Chi-cuadrado: 1.376
- Valor p: 0.503
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_nino y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.376, p = 0.503).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_nino                                                                                                
Femenino                                              11                  741                    51   803
Masculino                                             13                  836                    73   922
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_nino                                                                                          
Femenino                                             1.4                 92.3                   6.4
Masculino                                            1.4                 90.7                   7.9

**Estadísticos:**
- Chi-cuadrado: 1.591
- Valor p: 0.451
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_nino y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.591, p = 0.451).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_nino                                                                                                     
Femenino                                                    5                  751                    47   803
Masculino                                                   7                  846                    69   922
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_nino                                                                                               
Femenino                                                  0.6                 93.5                   5.9
Masculino                                                 0.8                 91.8                   7.5

**Estadísticos:**
- Chi-cuadrado: 1.957
- Valor p: 0.376
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_nino y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.957, p = 0.376).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_nino                                                                                                 
Femenino                                                9                  745                    49   803
Masculino                                               8                  855                    59   922
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_nino                                                                                           
Femenino                                              1.1                 92.8                   6.1
Masculino                                             0.9                 92.7                   6.4

**Estadísticos:**
- Chi-cuadrado: 0.340
- Valor p: 0.844
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_nino y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.340, p = 0.844).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 3. ANÁLISIS DE LA VARIABLE: NACIMIENTO_PREMATURO

### Variable: nacimiento_prematuro
==================================================

**Distribución de la variable nacimiento_prematuro:**
- No: 1310 (75.9%)
- Sí: 415 (24.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nacimiento_prematuro                                                                                  
No                                                 11                 1239                    60  1310
Sí                                                  3                  389                    23   415
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nacimiento_prematuro                                                                            
No                                                0.8                 94.6                   4.6
Sí                                                0.7                 93.7                   5.5

**Estadísticos:**
- Chi-cuadrado: 0.683
- Valor p: 0.711
- Grados de libertad: 2

**Interpretación:**
La asociación entre nacimiento_prematuro y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.683, p = 0.711).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nacimiento_prematuro                                                                                       
No                                                      40                 1087                   183  1310
Sí                                                      14                  350                    51   415
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nacimiento_prematuro                                                                                 
No                                                     3.1                 83.0                  14.0
Sí                                                     3.4                 84.3                  12.3

**Estadísticos:**
- Chi-cuadrado: 0.829
- Valor p: 0.661
- Grados de libertad: 2

**Interpretación:**
La asociación entre nacimiento_prematuro y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.829, p = 0.661).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nacimiento_prematuro                                                                                     
No                                                    19                 1206                    85  1310
Sí                                                     5                  371                    39   415
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nacimiento_prematuro                                                                               
No                                                   1.5                 92.1                   6.5
Sí                                                   1.2                 89.4                   9.4

**Estadísticos:**
- Chi-cuadrado: 4.091
- Valor p: 0.129
- Grados de libertad: 2

**Interpretación:**
La asociación entre nacimiento_prematuro y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.091, p = 0.129).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nacimiento_prematuro                                                                                          
No                                                         11                 1224                    75  1310
Sí                                                          1                  373                    41   415
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nacimiento_prematuro                                                                                    
No                                                        0.8                 93.4                   5.7
Sí                                                        0.2                 89.9                   9.9

**Estadísticos:**
- Chi-cuadrado: 10.143
- Valor p: 0.006
- Grados de libertad: 2

**Interpretación:**
La asociación entre nacimiento_prematuro y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.143, p = 0.006).

**Análisis por categorías:**
- **No** muestra la mayor proporción de alto riesgo (0.8%)
- **No** muestra la mayor proporción de desarrollo adecuado (93.4%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nacimiento_prematuro                                                                                      
No                                                     12                 1217                    81  1310
Sí                                                      5                  383                    27   415
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nacimiento_prematuro                                                                                
No                                                    0.9                 92.9                   6.2
Sí                                                    1.2                 92.3                   6.5

**Estadísticos:**
- Chi-cuadrado: 0.332
- Valor p: 0.847
- Grados de libertad: 2

**Interpretación:**
La asociación entre nacimiento_prematuro y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.332, p = 0.847).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 4. ANÁLISIS DE LA VARIABLE: SEMANAS_PREMATUREZ

### Variable: semanas_prematurez
==================================================

**Distribución de la variable semanas_prematurez:**
- 2 semanas: 115 (6.7%)
- 4 semanas: 93 (5.4%)
- 3 semanas: 59 (3.4%)
- 1 semana: 37 (2.1%)
- 6 semanas: 37 (2.1%)
- 1 semanas: 24 (1.4%)
- 5 semanas: 21 (1.2%)
- 7 semanas: 20 (1.2%)
- 8 semanas: 7 (0.4%)
- 9 semanas: 2 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
semanas_prematurez                                                                                   
1 semana                                            1                   34                     2   37
1 semanas                                           0                   23                     1   24
2 semanas                                           1                  108                     6  115
3 semanas                                           0                   51                     8   59
4 semanas                                           1                   91                     1   93
5 semanas                                           0                   19                     2   21
6 semanas                                           0                   34                     3   37
7 semanas                                           0                   20                     0   20
8 semanas                                           0                    7                     0    7
9 semanas                                           0                    2                     0    2
All                                                 3                  389                    23  415

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
semanas_prematurez                                                                              
1 semana                                          2.7                 91.9                   5.4
1 semanas                                         0.0                 95.8                   4.2
2 semanas                                         0.9                 93.9                   5.2
3 semanas                                         0.0                 86.4                  13.6
4 semanas                                         1.1                 97.8                   1.1
5 semanas                                         0.0                 90.5                   9.5
6 semanas                                         0.0                 91.9                   8.1
7 semanas                                         0.0                100.0                   0.0
8 semanas                                         0.0                100.0                   0.0
9 semanas                                         0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 17.059
- Valor p: 0.519
- Grados de libertad: 18

**Interpretación:**
La asociación entre semanas_prematurez y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 17.059, p = 0.519).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
semanas_prematurez                                                                                        
1 semana                                                 0                   33                     4   37
1 semanas                                                1                   21                     2   24
2 semanas                                                3                  103                     9  115
3 semanas                                                1                   47                    11   59
4 semanas                                                5                   79                     9   93
5 semanas                                                0                   18                     3   21
6 semanas                                                2                   27                     8   37
7 semanas                                                2                   13                     5   20
8 semanas                                                0                    7                     0    7
9 semanas                                                0                    2                     0    2
All                                                     14                  350                    51  415

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
semanas_prematurez                                                                                   
1 semana                                               0.0                 89.2                  10.8
1 semanas                                              4.2                 87.5                   8.3
2 semanas                                              2.6                 89.6                   7.8
3 semanas                                              1.7                 79.7                  18.6
4 semanas                                              5.4                 84.9                   9.7
5 semanas                                              0.0                 85.7                  14.3
6 semanas                                              5.4                 73.0                  21.6
7 semanas                                             10.0                 65.0                  25.0
8 semanas                                              0.0                100.0                   0.0
9 semanas                                              0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 20.657
- Valor p: 0.297
- Grados de libertad: 18

**Interpretación:**
La asociación entre semanas_prematurez y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 20.657, p = 0.297).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
semanas_prematurez                                                                                      
1 semana                                               0                   34                     3   37
1 semanas                                              0                   23                     1   24
2 semanas                                              1                  105                     9  115
3 semanas                                              0                   51                     8   59
4 semanas                                              2                   84                     7   93
5 semanas                                              1                   15                     5   21
6 semanas                                              1                   33                     3   37
7 semanas                                              0                   18                     2   20
8 semanas                                              0                    7                     0    7
9 semanas                                              0                    1                     1    2
All                                                    5                  371                    39  415

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
semanas_prematurez                                                                                 
1 semana                                             0.0                 91.9                   8.1
1 semanas                                            0.0                 95.8                   4.2
2 semanas                                            0.9                 91.3                   7.8
3 semanas                                            0.0                 86.4                  13.6
4 semanas                                            2.2                 90.3                   7.5
5 semanas                                            4.8                 71.4                  23.8
6 semanas                                            2.7                 89.2                   8.1
7 semanas                                            0.0                 90.0                  10.0
8 semanas                                            0.0                100.0                   0.0
9 semanas                                            0.0                 50.0                  50.0

**Estadísticos:**
- Chi-cuadrado: 18.313
- Valor p: 0.435
- Grados de libertad: 18

**Interpretación:**
La asociación entre semanas_prematurez y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 18.313, p = 0.435).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
semanas_prematurez                                                                                           
1 semana                                                    0                   34                     3   37
1 semanas                                                   0                   22                     2   24
2 semanas                                                   0                  108                     7  115
3 semanas                                                   0                   51                     8   59
4 semanas                                                   1                   81                    11   93
5 semanas                                                   0                   19                     2   21
6 semanas                                                   0                   32                     5   37
7 semanas                                                   0                   17                     3   20
8 semanas                                                   0                    7                     0    7
9 semanas                                                   0                    2                     0    2
All                                                         1                  373                    41  415

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
semanas_prematurez                                                                                      
1 semana                                                  0.0                 91.9                   8.1
1 semanas                                                 0.0                 91.7                   8.3
2 semanas                                                 0.0                 93.9                   6.1
3 semanas                                                 0.0                 86.4                  13.6
4 semanas                                                 1.1                 87.1                  11.8
5 semanas                                                 0.0                 90.5                   9.5
6 semanas                                                 0.0                 86.5                  13.5
7 semanas                                                 0.0                 85.0                  15.0
8 semanas                                                 0.0                100.0                   0.0
9 semanas                                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 8.990
- Valor p: 0.960
- Grados de libertad: 18

**Interpretación:**
La asociación entre semanas_prematurez y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.990, p = 0.960).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
semanas_prematurez                                                                                       
1 semana                                                0                   36                     1   37
1 semanas                                               0                   21                     3   24
2 semanas                                               2                  105                     8  115
3 semanas                                               0                   54                     5   59
4 semanas                                               3                   84                     6   93
5 semanas                                               0                   19                     2   21
6 semanas                                               0                   36                     1   37
7 semanas                                               0                   20                     0   20
8 semanas                                               0                    6                     1    7
9 semanas                                               0                    2                     0    2
All                                                     5                  383                    27  415

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
semanas_prematurez                                                                                  
1 semana                                              0.0                 97.3                   2.7
1 semanas                                             0.0                 87.5                  12.5
2 semanas                                             1.7                 91.3                   7.0
3 semanas                                             0.0                 91.5                   8.5
4 semanas                                             3.2                 90.3                   6.5
5 semanas                                             0.0                 90.5                   9.5
6 semanas                                             0.0                 97.3                   2.7
7 semanas                                             0.0                100.0                   0.0
8 semanas                                             0.0                 85.7                  14.3
9 semanas                                             0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 12.152
- Valor p: 0.839
- Grados de libertad: 18

**Interpretación:**
La asociación entre semanas_prematurez y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.152, p = 0.839).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 5. ANÁLISIS DE LA VARIABLE: EDAD_MESES_NINO

### Variable: edad_meses_nino
==================================================

**Distribución de la variable edad_meses_nino:**
- 12 meses: 145 (8.4%)
- 36 meses: 102 (5.9%)
- 6 meses: 99 (5.7%)
- 48 meses: 89 (5.2%)
- 24 meses: 89 (5.2%)
- 42 meses: 89 (5.2%)
- 27 meses: 89 (5.2%)
- 18 meses: 86 (5.0%)
- 22 meses: 83 (4.8%)
- 4 meses: 82 (4.8%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
edad_meses_nino                                                                                       
10 meses                                            0                   64                     1    65
12 meses                                            0                  145                     0   145
14 meses                                            1                   73                     0    74
16 meses                                            0                   61                     1    62
18 meses                                            1                   85                     0    86
2 meses                                             3                   77                     2    82
20 meses                                            0                   62                     5    67
22 meses                                            1                   79                     3    83
24 meses                                            0                   84                     5    89
27 meses                                            0                   84                     5    89
30 meses                                            0                   66                     7    73
33 meses                                            0                   75                     6    81
36 meses                                            2                   92                     8   102
4 meses                                             1                   70                    11    82
42 meses                                            1                   88                     0    89
48 meses                                            1                   75                    13    89
54 meses                                            1                   69                     9    79
6 meses                                             0                   98                     1    99
60 meses                                            2                   53                     4    59
8 meses                                             0                   67                     2    69
9 meses                                             0                   61                     0    61
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
edad_meses_nino                                                                                 
10 meses                                          0.0                 98.5                   1.5
12 meses                                          0.0                100.0                   0.0
14 meses                                          1.4                 98.6                   0.0
16 meses                                          0.0                 98.4                   1.6
18 meses                                          1.2                 98.8                   0.0
2 meses                                           3.7                 93.9                   2.4
20 meses                                          0.0                 92.5                   7.5
22 meses                                          1.2                 95.2                   3.6
24 meses                                          0.0                 94.4                   5.6
27 meses                                          0.0                 94.4                   5.6
30 meses                                          0.0                 90.4                   9.6
33 meses                                          0.0                 92.6                   7.4
36 meses                                          2.0                 90.2                   7.8
4 meses                                           1.2                 85.4                  13.4
42 meses                                          1.1                 98.9                   0.0
48 meses                                          1.1                 84.3                  14.6
54 meses                                          1.3                 87.3                  11.4
6 meses                                           0.0                 99.0                   1.0
60 meses                                          3.4                 89.8                   6.8
8 meses                                           0.0                 97.1                   2.9
9 meses                                           0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 102.481
- Valor p: 0.000
- Grados de libertad: 40

**Interpretación:**
La asociación entre edad_meses_nino y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 102.481, p = 0.000).

**Análisis por categorías:**
- **2 meses** muestra la mayor proporción de alto riesgo (3.7%)
- **12 meses** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
edad_meses_nino                                                                                            
10 meses                                                 0                   61                     4    65
12 meses                                                 3                  132                    10   145
14 meses                                                 2                   69                     3    74
16 meses                                                 2                   40                    20    62
18 meses                                                 5                   60                    21    86
2 meses                                                 18                   60                     4    82
20 meses                                                 2                   46                    19    67
22 meses                                                 3                   77                     3    83
24 meses                                                 6                   62                    21    89
27 meses                                                 0                   86                     3    89
30 meses                                                 0                   69                     4    73
33 meses                                                 0                   68                    13    81
36 meses                                                 1                   74                    27   102
4 meses                                                  6                   55                    21    82
42 meses                                                 3                   58                    28    89
48 meses                                                 0                   83                     6    89
54 meses                                                 0                   73                     6    79
6 meses                                                  0                   96                     3    99
60 meses                                                 1                   54                     4    59
8 meses                                                  2                   55                    12    69
9 meses                                                  0                   59                     2    61
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
edad_meses_nino                                                                                      
10 meses                                               0.0                 93.8                   6.2
12 meses                                               2.1                 91.0                   6.9
14 meses                                               2.7                 93.2                   4.1
16 meses                                               3.2                 64.5                  32.3
18 meses                                               5.8                 69.8                  24.4
2 meses                                               22.0                 73.2                   4.9
20 meses                                               3.0                 68.7                  28.4
22 meses                                               3.6                 92.8                   3.6
24 meses                                               6.7                 69.7                  23.6
27 meses                                               0.0                 96.6                   3.4
30 meses                                               0.0                 94.5                   5.5
33 meses                                               0.0                 84.0                  16.0
36 meses                                               1.0                 72.5                  26.5
4 meses                                                7.3                 67.1                  25.6
42 meses                                               3.4                 65.2                  31.5
48 meses                                               0.0                 93.3                   6.7
54 meses                                               0.0                 92.4                   7.6
6 meses                                                0.0                 97.0                   3.0
60 meses                                               1.7                 91.5                   6.8
8 meses                                                2.9                 79.7                  17.4
9 meses                                                0.0                 96.7                   3.3

**Estadísticos:**
- Chi-cuadrado: 292.478
- Valor p: 0.000
- Grados de libertad: 40

**Interpretación:**
La asociación entre edad_meses_nino y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 292.478, p = 0.000).

**Análisis por categorías:**
- **2 meses** muestra la mayor proporción de alto riesgo (22.0%)
- **6 meses** muestra la mayor proporción de desarrollo adecuado (97.0%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
edad_meses_nino                                                                                          
10 meses                                               1                   49                    15    65
12 meses                                               1                  137                     7   145
14 meses                                               2                   69                     3    74
16 meses                                               0                   54                     8    62
18 meses                                               1                   66                    19    86
2 meses                                                2                   77                     3    82
20 meses                                               3                   59                     5    67
22 meses                                               2                   79                     2    83
24 meses                                               5                   75                     9    89
27 meses                                               0                   87                     2    89
30 meses                                               0                   70                     3    73
33 meses                                               0                   78                     3    81
36 meses                                               0                   99                     3   102
4 meses                                                2                   73                     7    82
42 meses                                               0                   85                     4    89
48 meses                                               1                   86                     2    89
54 meses                                               0                   78                     1    79
6 meses                                                0                   97                     2    99
60 meses                                               0                   58                     1    59
8 meses                                                4                   44                    21    69
9 meses                                                0                   57                     4    61
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
edad_meses_nino                                                                                    
10 meses                                             1.5                 75.4                  23.1
12 meses                                             0.7                 94.5                   4.8
14 meses                                             2.7                 93.2                   4.1
16 meses                                             0.0                 87.1                  12.9
18 meses                                             1.2                 76.7                  22.1
2 meses                                              2.4                 93.9                   3.7
20 meses                                             4.5                 88.1                   7.5
22 meses                                             2.4                 95.2                   2.4
24 meses                                             5.6                 84.3                  10.1
27 meses                                             0.0                 97.8                   2.2
30 meses                                             0.0                 95.9                   4.1
33 meses                                             0.0                 96.3                   3.7
36 meses                                             0.0                 97.1                   2.9
4 meses                                              2.4                 89.0                   8.5
42 meses                                             0.0                 95.5                   4.5
48 meses                                             1.1                 96.6                   2.2
54 meses                                             0.0                 98.7                   1.3
6 meses                                              0.0                 98.0                   2.0
60 meses                                             0.0                 98.3                   1.7
8 meses                                              5.8                 63.8                  30.4
9 meses                                              0.0                 93.4                   6.6

**Estadísticos:**
- Chi-cuadrado: 187.102
- Valor p: 0.000
- Grados de libertad: 40

**Interpretación:**
La asociación entre edad_meses_nino y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 187.102, p = 0.000).

**Análisis por categorías:**
- **8 meses** muestra la mayor proporción de alto riesgo (5.8%)
- **54 meses** muestra la mayor proporción de desarrollo adecuado (98.7%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
edad_meses_nino                                                                                               
10 meses                                                    0                   59                     6    65
12 meses                                                    1                  137                     7   145
14 meses                                                    2                   72                     0    74
16 meses                                                    0                   56                     6    62
18 meses                                                    1                   80                     5    86
2 meses                                                     1                   73                     8    82
20 meses                                                    0                   62                     5    67
22 meses                                                    1                   80                     2    83
24 meses                                                    0                   87                     2    89
27 meses                                                    0                   86                     3    89
30 meses                                                    0                   72                     1    73
33 meses                                                    0                   79                     2    81
36 meses                                                    1                   88                    13   102
4 meses                                                     2                   74                     6    82
42 meses                                                    0                   88                     1    89
48 meses                                                    2                   72                    15    89
54 meses                                                    0                   72                     7    79
6 meses                                                     0                   97                     2    99
60 meses                                                    1                   51                     7    59
8 meses                                                     0                   53                    16    69
9 meses                                                     0                   59                     2    61
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
edad_meses_nino                                                                                         
10 meses                                                  0.0                 90.8                   9.2
12 meses                                                  0.7                 94.5                   4.8
14 meses                                                  2.7                 97.3                   0.0
16 meses                                                  0.0                 90.3                   9.7
18 meses                                                  1.2                 93.0                   5.8
2 meses                                                   1.2                 89.0                   9.8
20 meses                                                  0.0                 92.5                   7.5
22 meses                                                  1.2                 96.4                   2.4
24 meses                                                  0.0                 97.8                   2.2
27 meses                                                  0.0                 96.6                   3.4
30 meses                                                  0.0                 98.6                   1.4
33 meses                                                  0.0                 97.5                   2.5
36 meses                                                  1.0                 86.3                  12.7
4 meses                                                   2.4                 90.2                   7.3
42 meses                                                  0.0                 98.9                   1.1
48 meses                                                  2.2                 80.9                  16.9
54 meses                                                  0.0                 91.1                   8.9
6 meses                                                   0.0                 98.0                   2.0
60 meses                                                  1.7                 86.4                  11.9
8 meses                                                   0.0                 76.8                  23.2
9 meses                                                   0.0                 96.7                   3.3

**Estadísticos:**
- Chi-cuadrado: 103.857
- Valor p: 0.000
- Grados de libertad: 40

**Interpretación:**
La asociación entre edad_meses_nino y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 103.857, p = 0.000).

**Análisis por categorías:**
- **14 meses** muestra la mayor proporción de alto riesgo (2.7%)
- **42 meses** muestra la mayor proporción de desarrollo adecuado (98.9%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
edad_meses_nino                                                                                           
10 meses                                                0                   64                     1    65
12 meses                                                0                  144                     1   145
14 meses                                                0                   69                     5    74
16 meses                                                0                   62                     0    62
18 meses                                                0                   86                     0    86
2 meses                                                 4                   70                     8    82
20 meses                                                1                   59                     7    67
22 meses                                                2                   72                     9    83
24 meses                                                0                   79                    10    89
27 meses                                                0                   86                     3    89
30 meses                                                0                   69                     4    73
33 meses                                                1                   79                     1    81
36 meses                                                4                   88                    10   102
4 meses                                                 0                   77                     5    82
42 meses                                                0                   84                     5    89
48 meses                                                0                   88                     1    89
54 meses                                                3                   71                     5    79
6 meses                                                 0                   93                     6    99
60 meses                                                1                   41                    17    59
8 meses                                                 1                   60                     8    69
9 meses                                                 0                   59                     2    61
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
edad_meses_nino                                                                                     
10 meses                                              0.0                 98.5                   1.5
12 meses                                              0.0                 99.3                   0.7
14 meses                                              0.0                 93.2                   6.8
16 meses                                              0.0                100.0                   0.0
18 meses                                              0.0                100.0                   0.0
2 meses                                               4.9                 85.4                   9.8
20 meses                                              1.5                 88.1                  10.4
22 meses                                              2.4                 86.7                  10.8
24 meses                                              0.0                 88.8                  11.2
27 meses                                              0.0                 96.6                   3.4
30 meses                                              0.0                 94.5                   5.5
33 meses                                              1.2                 97.5                   1.2
36 meses                                              3.9                 86.3                   9.8
4 meses                                               0.0                 93.9                   6.1
42 meses                                              0.0                 94.4                   5.6
48 meses                                              0.0                 98.9                   1.1
54 meses                                              3.8                 89.9                   6.3
6 meses                                               0.0                 93.9                   6.1
60 meses                                              1.7                 69.5                  28.8
8 meses                                               1.4                 87.0                  11.6
9 meses                                               0.0                 96.7                   3.3

**Estadísticos:**
- Chi-cuadrado: 139.991
- Valor p: 0.000
- Grados de libertad: 40

**Interpretación:**
La asociación entre edad_meses_nino y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 139.991, p = 0.000).

**Análisis por categorías:**
- **2 meses** muestra la mayor proporción de alto riesgo (4.9%)
- **16 meses** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------


## 6. ANÁLISIS DE LA VARIABLE: GRUPO_ETNICO

### Variable: grupo_etnico
==================================================

**Distribución de la variable grupo_etnico:**
- No indígena: 984 (57.0%)
- Indígena: 741 (43.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                          
Indígena                                            6                  691                    44   741
No indígena                                         8                  937                    39   984
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                    
Indígena                                          0.8                 93.3                   5.9
No indígena                                       0.8                 95.2                   4.0

**Estadísticos:**
- Chi-cuadrado: 3.599
- Valor p: 0.165
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.599, p = 0.165).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                               
Indígena                                                33                  612                    96   741
No indígena                                             21                  825                   138   984
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                         
Indígena                                               4.5                 82.6                  13.0
No indígena                                            2.1                 83.8                  14.0

**Estadísticos:**
- Chi-cuadrado: 7.699
- Valor p: 0.021
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.699, p = 0.021).

**Análisis por categorías:**
- **Indígena** muestra la mayor proporción de alto riesgo (4.5%)
- **No indígena** muestra la mayor proporción de desarrollo adecuado (83.8%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                             
Indígena                                              14                  669                    58   741
No indígena                                           10                  908                    66   984
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                       
Indígena                                             1.9                 90.3                   7.8
No indígena                                          1.0                 92.3                   6.7

**Estadísticos:**
- Chi-cuadrado: 3.237
- Valor p: 0.198
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.237, p = 0.198).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                                  
Indígena                                                    7                  674                    60   741
No indígena                                                 5                  923                    56   984
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                            
Indígena                                                  0.9                 91.0                   8.1
No indígena                                               0.5                 93.8                   5.7

**Estadísticos:**
- Chi-cuadrado: 5.166
- Valor p: 0.076
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.166, p = 0.076).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
grupo_etnico                                                                                              
Indígena                                                7                  675                    59   741
No indígena                                            10                  925                    49   984
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
grupo_etnico                                                                                        
Indígena                                              0.9                 91.1                   8.0
No indígena                                           1.0                 94.0                   5.0

**Estadísticos:**
- Chi-cuadrado: 6.414
- Valor p: 0.040
- Grados de libertad: 2

**Interpretación:**
La asociación entre grupo_etnico y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 6.414, p = 0.040).

**Análisis por categorías:**
- **No indígena** muestra la mayor proporción de alto riesgo (1.0%)
- **No indígena** muestra la mayor proporción de desarrollo adecuado (94.0%)

--------------------------------------------------------------------------------


## 7. ANÁLISIS DE LA VARIABLE: AREA_RESIDENCIA

### Variable: area_residencia
==================================================

**Distribución de la variable area_residencia:**
- Urbano: 1468 (85.1%)
- Rural: 257 (14.9%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
area_residencia                                                                                       
Rural                                               2                  232                    23   257
Urbano                                             12                 1396                    60  1468
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
area_residencia                                                                                 
Rural                                             0.8                 90.3                   8.9
Urbano                                            0.8                 95.1                   4.1

**Estadísticos:**
- Chi-cuadrado: 11.289
- Valor p: 0.004
- Grados de libertad: 2

**Interpretación:**
La asociación entre area_residencia y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.289, p = 0.004).

**Análisis por categorías:**
- **Urbano** muestra la mayor proporción de alto riesgo (0.8%)
- **Urbano** muestra la mayor proporción de desarrollo adecuado (95.1%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
area_residencia                                                                                            
Rural                                                   19                  194                    44   257
Urbano                                                  35                 1243                   190  1468
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
area_residencia                                                                                      
Rural                                                  7.4                 75.5                  17.1
Urbano                                                 2.4                 84.7                  12.9

**Estadísticos:**
- Chi-cuadrado: 22.558
- Valor p: 0.000
- Grados de libertad: 2

**Interpretación:**
La asociación entre area_residencia y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 22.558, p = 0.000).

**Análisis por categorías:**
- **Rural** muestra la mayor proporción de alto riesgo (7.4%)
- **Urbano** muestra la mayor proporción de desarrollo adecuado (84.7%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
area_residencia                                                                                          
Rural                                                  4                  229                    24   257
Urbano                                                20                 1348                   100  1468
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
area_residencia                                                                                    
Rural                                                1.6                 89.1                   9.3
Urbano                                               1.4                 91.8                   6.8

**Estadísticos:**
- Chi-cuadrado: 2.178
- Valor p: 0.336
- Grados de libertad: 2

**Interpretación:**
La asociación entre area_residencia y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.178, p = 0.336).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
area_residencia                                                                                               
Rural                                                       3                  218                    36   257
Urbano                                                      9                 1379                    80  1468
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
area_residencia                                                                                         
Rural                                                     1.2                 84.8                  14.0
Urbano                                                    0.6                 93.9                   5.4

**Estadísticos:**
- Chi-cuadrado: 26.749
- Valor p: 0.000
- Grados de libertad: 2

**Interpretación:**
La asociación entre area_residencia y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 26.749, p = 0.000).

**Análisis por categorías:**
- **Rural** muestra la mayor proporción de alto riesgo (1.2%)
- **Urbano** muestra la mayor proporción de desarrollo adecuado (93.9%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
area_residencia                                                                                           
Rural                                                   6                  223                    28   257
Urbano                                                 11                 1377                    80  1468
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
area_residencia                                                                                     
Rural                                                 2.3                 86.8                  10.9
Urbano                                                0.7                 93.8                   5.4

**Estadísticos:**
- Chi-cuadrado: 17.101
- Valor p: 0.000
- Grados de libertad: 2

**Interpretación:**
La asociación entre area_residencia y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 17.101, p = 0.000).

**Análisis por categorías:**
- **Rural** muestra la mayor proporción de alto riesgo (2.3%)
- **Urbano** muestra la mayor proporción de desarrollo adecuado (93.8%)

--------------------------------------------------------------------------------


## 8. ANÁLISIS DE LA VARIABLE: NIVEL_EDUCATIVO_MADRE

### Variable: nivel_educativo_madre
==================================================

**Distribución de la variable nivel_educativo_madre:**
- Diversificado: 700 (40.6%)
- Básico: 506 (29.3%)
- Primaria: 314 (18.2%)
- Universitario: 128 (7.4%)
- Ninguna: 63 (3.7%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_madre                                                                                 
Básico                                              3                  485                    18   506
Diversificado                                       6                  660                    34   700
Ninguna                                             2                   54                     7    63
Primaria                                            1                  293                    20   314
Universitario                                       2                  124                     2   128
All                                                14                 1616                    81  1711

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_madre                                                                           
Básico                                            0.6                 95.8                   3.6
Diversificado                                     0.9                 94.3                   4.9
Ninguna                                           3.2                 85.7                  11.1
Primaria                                          0.3                 93.3                   6.4
Universitario                                     1.6                 96.9                   1.6

**Estadísticos:**
- Chi-cuadrado: 18.574
- Valor p: 0.017
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_madre y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 18.574, p = 0.017).

**Análisis por categorías:**
- **Ninguna** muestra la mayor proporción de alto riesgo (3.2%)
- **Universitario** muestra la mayor proporción de desarrollo adecuado (96.9%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_madre                                                                                      
Básico                                                  15                  417                    74   506
Diversificado                                           19                  583                    98   700
Ninguna                                                  5                   46                    12    63
Primaria                                                12                  262                    40   314
Universitario                                            3                  118                     7   128
All                                                     54                 1426                   231  1711

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_madre                                                                                
Básico                                                 3.0                 82.4                  14.6
Diversificado                                          2.7                 83.3                  14.0
Ninguna                                                7.9                 73.0                  19.0
Primaria                                               3.8                 83.4                  12.7
Universitario                                          2.3                 92.2                   5.5

**Estadísticos:**
- Chi-cuadrado: 16.112
- Valor p: 0.041
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_madre y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 16.112, p = 0.041).

**Análisis por categorías:**
- **Ninguna** muestra la mayor proporción de alto riesgo (7.9%)
- **Universitario** muestra la mayor proporción de desarrollo adecuado (92.2%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_madre                                                                                    
Básico                                                 7                  459                    40   506
Diversificado                                          6                  655                    39   700
Ninguna                                                4                   51                     8    63
Primaria                                               5                  279                    30   314
Universitario                                          1                  121                     6   128
All                                                   23                 1565                   123  1711

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_madre                                                                              
Básico                                               1.4                 90.7                   7.9
Diversificado                                        0.9                 93.6                   5.6
Ninguna                                              6.3                 81.0                  12.7
Primaria                                             1.6                 88.9                   9.6
Universitario                                        0.8                 94.5                   4.7

**Estadísticos:**
- Chi-cuadrado: 24.051
- Valor p: 0.002
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_madre y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 24.051, p = 0.002).

**Análisis por categorías:**
- **Ninguna** muestra la mayor proporción de alto riesgo (6.3%)
- **Universitario** muestra la mayor proporción de desarrollo adecuado (94.5%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_madre                                                                                         
Básico                                                      3                  478                    25   506
Diversificado                                               6                  640                    54   700
Ninguna                                                     1                   55                     7    63
Primaria                                                    1                  290                    23   314
Universitario                                               1                  124                     3   128
All                                                        12                 1587                   112  1711

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_madre                                                                                   
Básico                                                    0.6                 94.5                   4.9
Diversificado                                             0.9                 91.4                   7.7
Ninguna                                                   1.6                 87.3                  11.1
Primaria                                                  0.3                 92.4                   7.3
Universitario                                             0.8                 96.9                   2.3

**Estadísticos:**
- Chi-cuadrado: 11.636
- Valor p: 0.168
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_madre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.636, p = 0.168).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_madre                                                                                     
Básico                                                  1                  481                    24   506
Diversificado                                           8                  649                    43   700
Ninguna                                                 2                   52                     9    63
Primaria                                                4                  285                    25   314
Universitario                                           2                  121                     5   128
All                                                    17                 1588                   106  1711

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_madre                                                                               
Básico                                                0.2                 95.1                   4.7
Diversificado                                         1.1                 92.7                   6.1
Ninguna                                               3.2                 82.5                  14.3
Primaria                                              1.3                 90.8                   8.0
Universitario                                         1.6                 94.5                   3.9

**Estadísticos:**
- Chi-cuadrado: 19.286
- Valor p: 0.013
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_madre y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 19.286, p = 0.013).

**Análisis por categorías:**
- **Ninguna** muestra la mayor proporción de alto riesgo (3.2%)
- **Básico** muestra la mayor proporción de desarrollo adecuado (95.1%)

--------------------------------------------------------------------------------


## 9. ANÁLISIS DE LA VARIABLE: NIVEL_EDUCATIVO_PADRE

### Variable: nivel_educativo_padre
==================================================

**Distribución de la variable nivel_educativo_padre:**
- Diversificado: 811 (47.0%)
- Básico: 380 (22.0%)
- Primaria: 260 (15.1%)
- Universitario: 172 (10.0%)
- Ninguna: 50 (2.9%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_padre                                                                                 
Básico                                              0                  366                    14   380
Diversificado                                       6                  767                    38   811
Ninguna                                             2                   46                     2    50
Primaria                                            2                  243                    15   260
Universitario                                       3                  162                     7   172
All                                                13                 1584                    76  1673

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_padre                                                                           
Básico                                            0.0                 96.3                   3.7
Diversificado                                     0.7                 94.6                   4.7
Ninguna                                           4.0                 92.0                   4.0
Primaria                                          0.8                 93.5                   5.8
Universitario                                     1.7                 94.2                   4.1

**Estadísticos:**
- Chi-cuadrado: 13.544
- Valor p: 0.094
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_padre y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 13.544, p = 0.094).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_padre                                                                                      
Básico                                                   6                  320                    54   380
Diversificado                                           22                  675                   114   811
Ninguna                                                  3                   34                    13    50
Primaria                                                11                  223                    26   260
Universitario                                           10                  144                    18   172
All                                                     52                 1396                   225  1673

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_padre                                                                                
Básico                                                 1.6                 84.2                  14.2
Diversificado                                          2.7                 83.2                  14.1
Ninguna                                                6.0                 68.0                  26.0
Primaria                                               4.2                 85.8                  10.0
Universitario                                          5.8                 83.7                  10.5

**Estadísticos:**
- Chi-cuadrado: 21.030
- Valor p: 0.007
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_padre y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 21.030, p = 0.007).

**Análisis por categorías:**
- **Ninguna** muestra la mayor proporción de alto riesgo (6.0%)
- **Primaria** muestra la mayor proporción de desarrollo adecuado (85.8%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_padre                                                                                    
Básico                                                 2                  350                    28   380
Diversificado                                         11                  754                    46   811
Ninguna                                                1                   45                     4    50
Primaria                                               4                  229                    27   260
Universitario                                          2                  158                    12   172
All                                                   20                 1536                   117  1673

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_padre                                                                              
Básico                                               0.5                 92.1                   7.4
Diversificado                                        1.4                 93.0                   5.7
Ninguna                                              2.0                 90.0                   8.0
Primaria                                             1.5                 88.1                  10.4
Universitario                                        1.2                 91.9                   7.0

**Estadísticos:**
- Chi-cuadrado: 9.112
- Valor p: 0.333
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_padre y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 9.112, p = 0.333).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_padre                                                                                         
Básico                                                      2                  359                    19   380
Diversificado                                               4                  754                    53   811
Ninguna                                                     1                   44                     5    50
Primaria                                                    3                  242                    15   260
Universitario                                               1                  161                    10   172
All                                                        11                 1560                   102  1673

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_padre                                                                                   
Básico                                                    0.5                 94.5                   5.0
Diversificado                                             0.5                 93.0                   6.5
Ninguna                                                   2.0                 88.0                  10.0
Primaria                                                  1.2                 93.1                   5.8
Universitario                                             0.6                 93.6                   5.8

**Estadísticos:**
- Chi-cuadrado: 5.334
- Valor p: 0.721
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_padre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.334, p = 0.721).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
nivel_educativo_padre                                                                                     
Básico                                                  2                  358                    20   380
Diversificado                                           7                  757                    47   811
Ninguna                                                 1                   44                     5    50
Primaria                                                4                  235                    21   260
Universitario                                           2                  158                    12   172
All                                                    16                 1552                   105  1673

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
nivel_educativo_padre                                                                               
Básico                                                0.5                 94.2                   5.3
Diversificado                                         0.9                 93.3                   5.8
Ninguna                                               2.0                 88.0                  10.0
Primaria                                              1.5                 90.4                   8.1
Universitario                                         1.2                 91.9                   7.0

**Estadísticos:**
- Chi-cuadrado: 6.289
- Valor p: 0.615
- Grados de libertad: 8

**Interpretación:**
La asociación entre nivel_educativo_padre y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 6.289, p = 0.615).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 10. ANÁLISIS DE LA VARIABLE: FUENTE_AGUA_CONSUMO

### Variable: fuente_agua_consumo
==================================================

**Distribución de la variable fuente_agua_consumo:**
- Red de tubería: 1562 (90.6%)
- Chorro público: 142 (8.2%)
- Pozo público o privado: 18 (1.0%)
- Río, lago, tonel, camión y otro: 3 (0.2%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
fuente_agua_consumo                                                                                   
Chorro público                                      0                  136                     6   142
Pozo público o privado                              1                   15                     2    18
Red de tubería                                     13                 1474                    75  1562
Río, lago, tonel, camión y otro                     0                    3                     0     3
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
fuente_agua_consumo                                                                             
Chorro público                                    0.0                 95.8                   4.2
Pozo público o privado                            5.6                 83.3                  11.1
Red de tubería                                    0.8                 94.4                   4.8
Río, lago, tonel, camión y otro                   0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 8.179
- Valor p: 0.225
- Grados de libertad: 6

**Interpretación:**
La asociación entre fuente_agua_consumo y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.179, p = 0.225).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
fuente_agua_consumo                                                                                        
Chorro público                                           5                  119                    18   142
Pozo público o privado                                   4                   12                     2    18
Red de tubería                                          45                 1303                   214  1562
Río, lago, tonel, camión y otro                          0                    3                     0     3
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
fuente_agua_consumo                                                                                  
Chorro público                                         3.5                 83.8                  12.7
Pozo público o privado                                22.2                 66.7                  11.1
Red de tubería                                         2.9                 83.4                  13.7
Río, lago, tonel, camión y otro                        0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 22.728
- Valor p: 0.001
- Grados de libertad: 6

**Interpretación:**
La asociación entre fuente_agua_consumo y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 22.728, p = 0.001).

**Análisis por categorías:**
- **Pozo público o privado** muestra la mayor proporción de alto riesgo (22.2%)
- **Río, lago, tonel, camión y otro** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
fuente_agua_consumo                                                                                      
Chorro público                                         3                  126                    13   142
Pozo público o privado                                 2                   13                     3    18
Red de tubería                                        19                 1435                   108  1562
Río, lago, tonel, camión y otro                        0                    3                     0     3
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
fuente_agua_consumo                                                                                
Chorro público                                       2.1                 88.7                   9.2
Pozo público o privado                              11.1                 72.2                  16.7
Red de tubería                                       1.2                 91.9                   6.9
Río, lago, tonel, camión y otro                      0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 17.428
- Valor p: 0.008
- Grados de libertad: 6

**Interpretación:**
La asociación entre fuente_agua_consumo y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 17.428, p = 0.008).

**Análisis por categorías:**
- **Pozo público o privado** muestra la mayor proporción de alto riesgo (11.1%)
- **Río, lago, tonel, camión y otro** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
fuente_agua_consumo                                                                                           
Chorro público                                              1                  126                    15   142
Pozo público o privado                                      0                   15                     3    18
Red de tubería                                             11                 1453                    98  1562
Río, lago, tonel, camión y otro                             0                    3                     0     3
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
fuente_agua_consumo                                                                                     
Chorro público                                            0.7                 88.7                  10.6
Pozo público o privado                                    0.0                 83.3                  16.7
Red de tubería                                            0.7                 93.0                   6.3
Río, lago, tonel, camión y otro                           0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 7.023
- Valor p: 0.319
- Grados de libertad: 6

**Interpretación:**
La asociación entre fuente_agua_consumo y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.023, p = 0.319).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
fuente_agua_consumo                                                                                       
Chorro público                                          2                  133                     7   142
Pozo público o privado                                  1                   16                     1    18
Red de tubería                                         14                 1449                    99  1562
Río, lago, tonel, camión y otro                         0                    2                     1     3
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
fuente_agua_consumo                                                                                 
Chorro público                                        1.4                 93.7                   4.9
Pozo público o privado                                5.6                 88.9                   5.6
Red de tubería                                        0.9                 92.8                   6.3
Río, lago, tonel, camión y otro                       0.0                 66.7                  33.3

**Estadísticos:**
- Chi-cuadrado: 8.433
- Valor p: 0.208
- Grados de libertad: 6

**Interpretación:**
La asociación entre fuente_agua_consumo y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.433, p = 0.208).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 11. ANÁLISIS DE LA VARIABLE: TIPO_SANITARIO

### Variable: tipo_sanitario
==================================================

**Distribución de la variable tipo_sanitario:**
- Inodoro: 1615 (93.6%)
- Letrina/Pozo ciego: 109 (6.3%)
- Excusado lavable: 1 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_sanitario                                                                                        
Excusado lavable                                    0                    1                     0     1
Inodoro                                            14                 1523                    78  1615
Letrina/Pozo ciego                                  0                  104                     5   109
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_sanitario                                                                                  
Excusado lavable                                  0.0                100.0                   0.0
Inodoro                                           0.9                 94.3                   4.8
Letrina/Pozo ciego                                0.0                 95.4                   4.6

**Estadísticos:**
- Chi-cuadrado: 1.031
- Valor p: 0.905
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_sanitario y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.031, p = 0.905).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_sanitario                                                                                             
Excusado lavable                                         0                    1                     0     1
Inodoro                                                 47                 1345                   223  1615
Letrina/Pozo ciego                                       7                   91                    11   109
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_sanitario                                                                                       
Excusado lavable                                       0.0                100.0                   0.0
Inodoro                                                2.9                 83.3                  13.8
Letrina/Pozo ciego                                     6.4                 83.5                  10.1

**Estadísticos:**
- Chi-cuadrado: 5.263
- Valor p: 0.261
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_sanitario y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.263, p = 0.261).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_sanitario                                                                                           
Excusado lavable                                       0                    1                     0     1
Inodoro                                               21                 1476                   118  1615
Letrina/Pozo ciego                                     3                  100                     6   109
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_sanitario                                                                                     
Excusado lavable                                     0.0                100.0                   0.0
Inodoro                                              1.3                 91.4                   7.3
Letrina/Pozo ciego                                   2.8                 91.7                   5.5

**Estadísticos:**
- Chi-cuadrado: 2.104
- Valor p: 0.717
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_sanitario y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.104, p = 0.717).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_sanitario                                                                                                
Excusado lavable                                            0                    1                     0     1
Inodoro                                                    12                 1500                   103  1615
Letrina/Pozo ciego                                          0                   96                    13   109
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_sanitario                                                                                          
Excusado lavable                                          0.0                100.0                   0.0
Inodoro                                                   0.7                 92.9                   6.4
Letrina/Pozo ciego                                        0.0                 88.1                  11.9

**Estadísticos:**
- Chi-cuadrado: 5.821
- Valor p: 0.213
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_sanitario y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.821, p = 0.213).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_sanitario                                                                                            
Excusado lavable                                        0                    0                     1     1
Inodoro                                                17                 1500                    98  1615
Letrina/Pozo ciego                                      0                  100                     9   109
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_sanitario                                                                                      
Excusado lavable                                      0.0                  0.0                 100.0
Inodoro                                               1.1                 92.9                   6.1
Letrina/Pozo ciego                                    0.0                 91.7                   8.3

**Estadísticos:**
- Chi-cuadrado: 16.924
- Valor p: 0.002
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_sanitario y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 16.924, p = 0.002).

**Análisis por categorías:**
- **Inodoro** muestra la mayor proporción de alto riesgo (1.1%)
- **Inodoro** muestra la mayor proporción de desarrollo adecuado (92.9%)

--------------------------------------------------------------------------------


## 12. ANÁLISIS DE LA VARIABLE: MANEJO_BASURA

### Variable: manejo_basura
==================================================

**Distribución de la variable manejo_basura:**
- Servicio municipal o privado: 1482 (85.9%)
- La quema: 223 (12.9%)
- La tira en cualquier lugar: 9 (0.5%)
- La entierra: 8 (0.5%)
- Otra: 3 (0.2%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
manejo_basura                                                                                         
La entierra                                         1                    6                     1     8
La quema                                            2                  203                    18   223
La tira en cualquier lugar                          0                    9                     0     9
Otra                                                0                    3                     0     3
Servicio municipal o privado                       11                 1407                    64  1482
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
manejo_basura                                                                                   
La entierra                                      12.5                 75.0                  12.5
La quema                                          0.9                 91.0                   8.1
La tira en cualquier lugar                        0.0                100.0                   0.0
Otra                                              0.0                100.0                   0.0
Servicio municipal o privado                      0.7                 94.9                   4.3

**Estadísticos:**
- Chi-cuadrado: 21.580
- Valor p: 0.006
- Grados de libertad: 8

**Interpretación:**
La asociación entre manejo_basura y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 21.580, p = 0.006).

**Análisis por categorías:**
- **La entierra** muestra la mayor proporción de alto riesgo (12.5%)
- **La tira en cualquier lugar** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
manejo_basura                                                                                              
La entierra                                              1                    7                     0     8
La quema                                                12                  187                    24   223
La tira en cualquier lugar                               0                    6                     3     9
Otra                                                     0                    3                     0     3
Servicio municipal o privado                            41                 1234                   207  1482
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
manejo_basura                                                                                        
La entierra                                           12.5                 87.5                   0.0
La quema                                               5.4                 83.9                  10.8
La tira en cualquier lugar                             0.0                 66.7                  33.3
Otra                                                   0.0                100.0                   0.0
Servicio municipal o privado                           2.8                 83.3                  14.0

**Estadísticos:**
- Chi-cuadrado: 12.833
- Valor p: 0.118
- Grados de libertad: 8

**Interpretación:**
La asociación entre manejo_basura y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.833, p = 0.118).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
manejo_basura                                                                                            
La entierra                                            1                    6                     1     8
La quema                                               4                  203                    16   223
La tira en cualquier lugar                             0                    8                     1     9
Otra                                                   0                    3                     0     3
Servicio municipal o privado                          19                 1357                   106  1482
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
manejo_basura                                                                                      
La entierra                                         12.5                 75.0                  12.5
La quema                                             1.8                 91.0                   7.2
La tira en cualquier lugar                           0.0                 88.9                  11.1
Otra                                                 0.0                100.0                   0.0
Servicio municipal o privado                         1.3                 91.6                   7.2

**Estadísticos:**
- Chi-cuadrado: 8.648
- Valor p: 0.373
- Grados de libertad: 8

**Interpretación:**
La asociación entre manejo_basura y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.648, p = 0.373).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
manejo_basura                                                                                                 
La entierra                                                 1                    7                     0     8
La quema                                                    3                  195                    25   223
La tira en cualquier lugar                                  0                    9                     0     9
Otra                                                        0                    3                     0     3
Servicio municipal o privado                                8                 1383                    91  1482
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
manejo_basura                                                                                           
La entierra                                              12.5                 87.5                   0.0
La quema                                                  1.3                 87.4                  11.2
La tira en cualquier lugar                                0.0                100.0                   0.0
Otra                                                      0.0                100.0                   0.0
Servicio municipal o privado                              0.5                 93.3                   6.1

**Estadísticos:**
- Chi-cuadrado: 27.566
- Valor p: 0.001
- Grados de libertad: 8

**Interpretación:**
La asociación entre manejo_basura y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 27.566, p = 0.001).

**Análisis por categorías:**
- **La entierra** muestra la mayor proporción de alto riesgo (12.5%)
- **La tira en cualquier lugar** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
manejo_basura                                                                                             
La entierra                                             0                    7                     1     8
La quema                                                4                  198                    21   223
La tira en cualquier lugar                              0                    9                     0     9
Otra                                                    0                    3                     0     3
Servicio municipal o privado                           13                 1383                    86  1482
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
manejo_basura                                                                                       
La entierra                                           0.0                 87.5                  12.5
La quema                                              1.8                 88.8                   9.4
La tira en cualquier lugar                            0.0                100.0                   0.0
Otra                                                  0.0                100.0                   0.0
Servicio municipal o privado                          0.9                 93.3                   5.8

**Estadísticos:**
- Chi-cuadrado: 7.666
- Valor p: 0.467
- Grados de libertad: 8

**Interpretación:**
La asociación entre manejo_basura y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.666, p = 0.467).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 13. ANÁLISIS DE LA VARIABLE: TIPO_ENERGIA_LUZ

### Variable: tipo_energia_luz
==================================================

**Distribución de la variable tipo_energia_luz:**
- Eléctrico: 1725 (100.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_luz                                                                                      
Eléctrico                                          14                 1628                    83  1725
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_luz                                                                                
Eléctrico                                         0.8                 94.4                   4.8
**Interpretación:**
No se pudo calcular el estadístico chi-cuadrado para la asociación entre tipo_energia_luz y Comunicación.
--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_luz                                                                                           
Eléctrico                                               54                 1437                   234  1725
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_luz                                                                                     
Eléctrico                                              3.1                 83.3                  13.6
**Interpretación:**
No se pudo calcular el estadístico chi-cuadrado para la asociación entre tipo_energia_luz y Motricidad Gruesa.
--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_luz                                                                                         
Eléctrico                                             24                 1577                   124  1725
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_luz                                                                                   
Eléctrico                                            1.4                 91.4                   7.2
**Interpretación:**
No se pudo calcular el estadístico chi-cuadrado para la asociación entre tipo_energia_luz y Motricidad Fina.
--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_luz                                                                                              
Eléctrico                                                  12                 1597                   116  1725
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_luz                                                                                        
Eléctrico                                                 0.7                 92.6                   6.7
**Interpretación:**
No se pudo calcular el estadístico chi-cuadrado para la asociación entre tipo_energia_luz y Resolución de Problemas.
--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_luz                                                                                          
Eléctrico                                              17                 1600                   108  1725
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_luz                                                                                    
Eléctrico                                             1.0                 92.8                   6.3
**Interpretación:**
No se pudo calcular el estadístico chi-cuadrado para la asociación entre tipo_energia_luz y Desarrollo Socio-Individual.
--------------------------------------------------------------------------------


## 14. ANÁLISIS DE LA VARIABLE: TIPO_ENERGIA_COCINA

### Variable: tipo_energia_cocina
==================================================

**Distribución de la variable tipo_energia_cocina:**
- Gas propano: 1503 (87.1%)
- Leña: 216 (12.5%)
- Gas corriente, carbón y otros: 4 (0.2%)
- Electricidad: 2 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_cocina                                                                                   
Electricidad                                        0                    2                     0     2
Gas corriente, carbón y otros                       0                    4                     0     4
Gas propano                                        13                 1422                    68  1503
Leña                                                1                  200                    15   216
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_cocina                                                                             
Electricidad                                      0.0                100.0                   0.0
Gas corriente, carbón y otros                     0.0                100.0                   0.0
Gas propano                                       0.9                 94.6                   4.5
Leña                                              0.5                 92.6                   6.9

**Estadísticos:**
- Chi-cuadrado: 3.115
- Valor p: 0.794
- Grados de libertad: 6

**Interpretación:**
La asociación entre tipo_energia_cocina y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.115, p = 0.794).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_cocina                                                                                        
Electricidad                                             0                    2                     0     2
Gas corriente, carbón y otros                            0                    3                     1     4
Gas propano                                             44                 1256                   203  1503
Leña                                                    10                  176                    30   216
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_cocina                                                                                  
Electricidad                                           0.0                100.0                   0.0
Gas corriente, carbón y otros                          0.0                 75.0                  25.0
Gas propano                                            2.9                 83.6                  13.5
Leña                                                   4.6                 81.5                  13.9

**Estadísticos:**
- Chi-cuadrado: 2.812
- Valor p: 0.832
- Grados de libertad: 6

**Interpretación:**
La asociación entre tipo_energia_cocina y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.812, p = 0.832).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_cocina                                                                                      
Electricidad                                           0                    2                     0     2
Gas corriente, carbón y otros                          1                    3                     0     4
Gas propano                                           21                 1378                   104  1503
Leña                                                   2                  194                    20   216
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_cocina                                                                                
Electricidad                                         0.0                100.0                   0.0
Gas corriente, carbón y otros                       25.0                 75.0                   0.0
Gas propano                                          1.4                 91.7                   6.9
Leña                                                 0.9                 89.8                   9.3

**Estadísticos:**
- Chi-cuadrado: 18.466
- Valor p: 0.005
- Grados de libertad: 6

**Interpretación:**
La asociación entre tipo_energia_cocina y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 18.466, p = 0.005).

**Análisis por categorías:**
- **Gas corriente, carbón y otros** muestra la mayor proporción de alto riesgo (25.0%)
- **Electricidad** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_cocina                                                                                           
Electricidad                                                0                    2                     0     2
Gas corriente, carbón y otros                               0                    4                     0     4
Gas propano                                                11                 1399                    93  1503
Leña                                                        1                  192                    23   216
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_cocina                                                                                     
Electricidad                                              0.0                100.0                   0.0
Gas corriente, carbón y otros                             0.0                100.0                   0.0
Gas propano                                               0.7                 93.1                   6.2
Leña                                                      0.5                 88.9                  10.6

**Estadísticos:**
- Chi-cuadrado: 6.625
- Valor p: 0.357
- Grados de libertad: 6

**Interpretación:**
La asociación entre tipo_energia_cocina y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 6.625, p = 0.357).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_energia_cocina                                                                                       
Electricidad                                            0                    2                     0     2
Gas corriente, carbón y otros                           0                    4                     0     4
Gas propano                                            15                 1400                    88  1503
Leña                                                    2                  194                    20   216
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_energia_cocina                                                                                 
Electricidad                                          0.0                100.0                   0.0
Gas corriente, carbón y otros                         0.0                100.0                   0.0
Gas propano                                           1.0                 93.1                   5.9
Leña                                                  0.9                 89.8                   9.3

**Estadísticos:**
- Chi-cuadrado: 4.202
- Valor p: 0.649
- Grados de libertad: 6

**Interpretación:**
La asociación entre tipo_energia_cocina y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.202, p = 0.649).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 15. ANÁLISIS DE LA VARIABLE: PROPIEDAD_VIVIENDA

### Variable: propiedad_vivienda
==================================================

**Distribución de la variable propiedad_vivienda:**
- Propia: 1254 (72.7%)
- Alquilada: 471 (27.3%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
propiedad_vivienda                                                                                    
Alquilada                                           6                  438                    27   471
Propia                                              8                 1190                    56  1254
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
propiedad_vivienda                                                                              
Alquilada                                         1.3                 93.0                   5.7
Propia                                            0.6                 94.9                   4.5

**Estadísticos:**
- Chi-cuadrado: 2.979
- Valor p: 0.225
- Grados de libertad: 2

**Interpretación:**
La asociación entre propiedad_vivienda y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.979, p = 0.225).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
propiedad_vivienda                                                                                         
Alquilada                                               21                  403                    47   471
Propia                                                  33                 1034                   187  1254
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
propiedad_vivienda                                                                                   
Alquilada                                              4.5                 85.6                  10.0
Propia                                                 2.6                 82.5                  14.9

**Estadísticos:**
- Chi-cuadrado: 10.191
- Valor p: 0.006
- Grados de libertad: 2

**Interpretación:**
La asociación entre propiedad_vivienda y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.191, p = 0.006).

**Análisis por categorías:**
- **Alquilada** muestra la mayor proporción de alto riesgo (4.5%)
- **Alquilada** muestra la mayor proporción de desarrollo adecuado (85.6%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
propiedad_vivienda                                                                                       
Alquilada                                              9                  426                    36   471
Propia                                                15                 1151                    88  1254
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
propiedad_vivienda                                                                                 
Alquilada                                            1.9                 90.4                   7.6
Propia                                               1.2                 91.8                   7.0

**Estadísticos:**
- Chi-cuadrado: 1.511
- Valor p: 0.470
- Grados de libertad: 2

**Interpretación:**
La asociación entre propiedad_vivienda y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.511, p = 0.470).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
propiedad_vivienda                                                                                            
Alquilada                                                   3                  437                    31   471
Propia                                                      9                 1160                    85  1254
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
propiedad_vivienda                                                                                      
Alquilada                                                 0.6                 92.8                   6.6
Propia                                                    0.7                 92.5                   6.8

**Estadísticos:**
- Chi-cuadrado: 0.055
- Valor p: 0.973
- Grados de libertad: 2

**Interpretación:**
La asociación entre propiedad_vivienda y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.055, p = 0.973).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
propiedad_vivienda                                                                                        
Alquilada                                               6                  437                    28   471
Propia                                                 11                 1163                    80  1254
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
propiedad_vivienda                                                                                  
Alquilada                                             1.3                 92.8                   5.9
Propia                                                0.9                 92.7                   6.4

**Estadísticos:**
- Chi-cuadrado: 0.650
- Valor p: 0.722
- Grados de libertad: 2

**Interpretación:**
La asociación entre propiedad_vivienda y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.650, p = 0.722).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 16. ANÁLISIS DE LA VARIABLE: SEXO_JEFE_HOGAR

### Variable: sexo_jefe_hogar
==================================================

**Distribución de la variable sexo_jefe_hogar:**
- Hombre: 1331 (77.2%)
- Mujer: 394 (22.8%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_jefe_hogar                                                                                       
Hombre                                             12                 1252                    67  1331
Mujer                                               2                  376                    16   394
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_jefe_hogar                                                                                 
Hombre                                            0.9                 94.1                   5.0
Mujer                                             0.5                 95.4                   4.1

**Estadísticos:**
- Chi-cuadrado: 1.240
- Valor p: 0.538
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_jefe_hogar y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.240, p = 0.538).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_jefe_hogar                                                                                            
Hombre                                                  42                 1116                   173  1331
Mujer                                                   12                  321                    61   394
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_jefe_hogar                                                                                      
Hombre                                                 3.2                 83.8                  13.0
Mujer                                                  3.0                 81.5                  15.5

**Estadísticos:**
- Chi-cuadrado: 1.601
- Valor p: 0.449
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_jefe_hogar y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.601, p = 0.449).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_jefe_hogar                                                                                          
Hombre                                                18                 1224                    89  1331
Mujer                                                  6                  353                    35   394
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_jefe_hogar                                                                                    
Hombre                                               1.4                 92.0                   6.7
Mujer                                                1.5                 89.6                   8.9

**Estadísticos:**
- Chi-cuadrado: 2.290
- Valor p: 0.318
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_jefe_hogar y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.290, p = 0.318).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_jefe_hogar                                                                                               
Hombre                                                     10                 1234                    87  1331
Mujer                                                       2                  363                    29   394
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_jefe_hogar                                                                                         
Hombre                                                    0.8                 92.7                   6.5
Mujer                                                     0.5                 92.1                   7.4

**Estadísticos:**
- Chi-cuadrado: 0.578
- Valor p: 0.749
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_jefe_hogar y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.578, p = 0.749).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
sexo_jefe_hogar                                                                                           
Hombre                                                 11                 1233                    87  1331
Mujer                                                   6                  367                    21   394
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
sexo_jefe_hogar                                                                                     
Hombre                                                0.8                 92.6                   6.5
Mujer                                                 1.5                 93.1                   5.3

**Estadísticos:**
- Chi-cuadrado: 2.211
- Valor p: 0.331
- Grados de libertad: 2

**Interpretación:**
La asociación entre sexo_jefe_hogar y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.211, p = 0.331).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 17. ANÁLISIS DE LA VARIABLE: SITUACION_LABORAL_MADRE

### Variable: situacion_laboral_madre
==================================================

**Distribución de la variable situacion_laboral_madre:**
- No trabaja: 868 (50.3%)
- Trabaja: 850 (49.3%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_madre                                                                               
No trabaja                                          9                  825                    34   868
Trabaja                                             5                  797                    48   850
All                                                14                 1622                    82  1718

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_madre                                                                         
No trabaja                                        1.0                 95.0                   3.9
Trabaja                                           0.6                 93.8                   5.6

**Estadísticos:**
- Chi-cuadrado: 3.828
- Valor p: 0.147
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_madre y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.828, p = 0.147).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_madre                                                                                    
No trabaja                                              30                  730                   108   868
Trabaja                                                 24                  700                   126   850
All                                                     54                 1430                   234  1718

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_madre                                                                              
No trabaja                                             3.5                 84.1                  12.4
Trabaja                                                2.8                 82.4                  14.8

**Estadísticos:**
- Chi-cuadrado: 2.492
- Valor p: 0.288
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_madre y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.492, p = 0.288).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_madre                                                                                  
No trabaja                                            10                  799                    59   868
Trabaja                                               14                  772                    64   850
All                                                   24                 1571                   123  1718

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_madre                                                                            
No trabaja                                           1.2                 92.1                   6.8
Trabaja                                              1.6                 90.8                   7.5

**Estadísticos:**
- Chi-cuadrado: 1.145
- Valor p: 0.564
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_madre y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.145, p = 0.564).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_madre                                                                                       
No trabaja                                                  7                  807                    54   868
Trabaja                                                     5                  785                    60   850
All                                                        12                 1592                   114  1718

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_madre                                                                                 
No trabaja                                                0.8                 93.0                   6.2
Trabaja                                                   0.6                 92.4                   7.1

**Estadísticos:**
- Chi-cuadrado: 0.765
- Valor p: 0.682
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_madre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.765, p = 0.682).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_madre                                                                                   
No trabaja                                              9                  811                    48   868
Trabaja                                                 8                  783                    59   850
All                                                    17                 1594                   107  1718

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_madre                                                                             
No trabaja                                            1.0                 93.4                   5.5
Trabaja                                               0.9                 92.1                   6.9

**Estadísticos:**
- Chi-cuadrado: 1.493
- Valor p: 0.474
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_madre y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.493, p = 0.474).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 18. ANÁLISIS DE LA VARIABLE: SITUACION_LABORAL_PADRE

### Variable: situacion_laboral_padre
==================================================

**Distribución de la variable situacion_laboral_padre:**
- Trabaja: 1520 (88.1%)
- No trabaja: 156 (9.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_padre                                                                               
No trabaja                                          0                  145                    11   156
Trabaja                                            13                 1440                    67  1520
All                                                13                 1585                    78  1676

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_padre                                                                         
No trabaja                                        0.0                 92.9                   7.1
Trabaja                                           0.9                 94.7                   4.4

**Estadísticos:**
- Chi-cuadrado: 3.506
- Valor p: 0.173
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_padre y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.506, p = 0.173).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_padre                                                                                    
No trabaja                                               5                  117                    34   156
Trabaja                                                 48                 1280                   192  1520
All                                                     53                 1397                   226  1676

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_padre                                                                              
No trabaja                                             3.2                 75.0                  21.8
Trabaja                                                3.2                 84.2                  12.6

**Estadísticos:**
- Chi-cuadrado: 10.251
- Valor p: 0.006
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_padre y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.251, p = 0.006).

**Análisis por categorías:**
- **No trabaja** muestra la mayor proporción de alto riesgo (3.2%)
- **Trabaja** muestra la mayor proporción de desarrollo adecuado (84.2%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_padre                                                                                  
No trabaja                                             0                  146                    10   156
Trabaja                                               21                 1392                   107  1520
All                                                   21                 1538                   117  1676

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_padre                                                                            
No trabaja                                           0.0                 93.6                   6.4
Trabaja                                              1.4                 91.6                   7.0

**Estadísticos:**
- Chi-cuadrado: 2.298
- Valor p: 0.317
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_padre y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.298, p = 0.317).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_padre                                                                                       
No trabaja                                                  0                  144                    12   156
Trabaja                                                    11                 1418                    91  1520
All                                                        11                 1562                   103  1676

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_padre                                                                                 
No trabaja                                                0.0                 92.3                   7.7
Trabaja                                                   0.7                 93.3                   6.0

**Estadísticos:**
- Chi-cuadrado: 1.813
- Valor p: 0.404
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_padre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.813, p = 0.404).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
situacion_laboral_padre                                                                                   
No trabaja                                              3                  140                    13   156
Trabaja                                                14                 1414                    92  1520
All                                                    17                 1554                   105  1676

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
situacion_laboral_padre                                                                             
No trabaja                                            1.9                 89.7                   8.3
Trabaja                                               0.9                 93.0                   6.1

**Estadísticos:**
- Chi-cuadrado: 2.740
- Valor p: 0.254
- Grados de libertad: 2

**Interpretación:**
La asociación entre situacion_laboral_padre y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.740, p = 0.254).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 19. ANÁLISIS DE LA VARIABLE: TIPO_EMPLEO_MADRE

### Variable: tipo_empleo_madre
==================================================

**Distribución de la variable tipo_empleo_madre:**
- Formal: 504 (29.2%)
- Informal: 346 (20.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
tipo_empleo_madre                                                                                    
Formal                                              4                  479                    21  504
Informal                                            1                  318                    27  346
All                                                 5                  797                    48  850

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_madre                                                                               
Formal                                            0.8                 95.0                   4.2
Informal                                          0.3                 91.9                   7.8

**Estadísticos:**
- Chi-cuadrado: 5.908
- Valor p: 0.052
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_madre y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.908, p = 0.052).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
tipo_empleo_madre                                                                                         
Formal                                                  18                  407                    79  504
Informal                                                 6                  293                    47  346
All                                                     24                  700                   126  850

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_madre                                                                                    
Formal                                                 3.6                 80.8                  15.7
Informal                                               1.7                 84.7                  13.6

**Estadísticos:**
- Chi-cuadrado: 3.442
- Valor p: 0.179
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_madre y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.442, p = 0.179).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
tipo_empleo_madre                                                                                       
Formal                                                 6                  457                    41  504
Informal                                               8                  315                    23  346
All                                                   14                  772                    64  850

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_madre                                                                                  
Formal                                               1.2                 90.7                   8.1
Informal                                             2.3                 91.0                   6.6

**Estadísticos:**
- Chi-cuadrado: 2.173
- Valor p: 0.337
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_madre y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.173, p = 0.337).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
tipo_empleo_madre                                                                                            
Formal                                                      3                  464                    37  504
Informal                                                    2                  321                    23  346
All                                                         5                  785                    60  850

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_madre                                                                                       
Formal                                                    0.6                 92.1                   7.3
Informal                                                  0.6                 92.8                   6.6

**Estadísticos:**
- Chi-cuadrado: 0.152
- Valor p: 0.927
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_madre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.152, p = 0.927).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
tipo_empleo_madre                                                                                        
Formal                                                  7                  459                    38  504
Informal                                                1                  324                    21  346
All                                                     8                  783                    59  850

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_madre                                                                                   
Formal                                                1.4                 91.1                   7.5
Informal                                              0.3                 93.6                   6.1

**Estadísticos:**
- Chi-cuadrado: 3.423
- Valor p: 0.181
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_madre y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.423, p = 0.181).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 20. ANÁLISIS DE LA VARIABLE: TIPO_EMPLEO_PADRE

### Variable: tipo_empleo_padre
==================================================

**Distribución de la variable tipo_empleo_padre:**
- Formal: 1056 (61.2%)
- Informal: 464 (26.9%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_empleo_padre                                                                                     
Formal                                              9                  998                    49  1056
Informal                                            4                  442                    18   464
All                                                13                 1440                    67  1520

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_padre                                                                               
Formal                                            0.9                 94.5                   4.6
Informal                                          0.9                 95.3                   3.9

**Estadísticos:**
- Chi-cuadrado: 0.443
- Valor p: 0.801
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_padre y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.443, p = 0.801).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_empleo_padre                                                                                          
Formal                                                  34                  891                   131  1056
Informal                                                14                  389                    61   464
All                                                     48                 1280                   192  1520

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_padre                                                                                    
Formal                                                 3.2                 84.4                  12.4
Informal                                               3.0                 83.8                  13.1

**Estadísticos:**
- Chi-cuadrado: 0.193
- Valor p: 0.908
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_padre y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.193, p = 0.908).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_empleo_padre                                                                                        
Formal                                                14                  967                    75  1056
Informal                                               7                  425                    32   464
All                                                   21                 1392                   107  1520

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_padre                                                                                  
Formal                                               1.3                 91.6                   7.1
Informal                                             1.5                 91.6                   6.9

**Estadísticos:**
- Chi-cuadrado: 0.097
- Valor p: 0.952
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_padre y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.097, p = 0.952).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_empleo_padre                                                                                             
Formal                                                      6                  987                    63  1056
Informal                                                    5                  431                    28   464
All                                                        11                 1418                    91  1520

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_padre                                                                                       
Formal                                                    0.6                 93.5                   6.0
Informal                                                  1.1                 92.9                   6.0

**Estadísticos:**
- Chi-cuadrado: 1.170
- Valor p: 0.557
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_padre y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.170, p = 0.557).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_empleo_padre                                                                                         
Formal                                                 11                  986                    59  1056
Informal                                                3                  428                    33   464
All                                                    14                 1414                    92  1520

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_empleo_padre                                                                                   
Formal                                                1.0                 93.4                   5.6
Informal                                              0.6                 92.2                   7.1

**Estadísticos:**
- Chi-cuadrado: 1.829
- Valor p: 0.401
- Grados de libertad: 2

**Interpretación:**
La asociación entre tipo_empleo_padre y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.829, p = 0.401).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 21. ANÁLISIS DE LA VARIABLE: SEGURO_SOCIAL

### Variable: seguro_social
==================================================

**Distribución de la variable seguro_social:**
- No: 1311 (76.0%)
- Sí: 414 (24.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
seguro_social                                                                                         
No                                                  8                 1234                    69  1311
Sí                                                  6                  394                    14   414
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
seguro_social                                                                                   
No                                                0.6                 94.1                   5.3
Sí                                                1.4                 95.2                   3.4

**Estadísticos:**
- Chi-cuadrado: 5.080
- Valor p: 0.079
- Grados de libertad: 2

**Interpretación:**
La asociación entre seguro_social y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.080, p = 0.079).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
seguro_social                                                                                              
No                                                      36                 1090                   185  1311
Sí                                                      18                  347                    49   414
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
seguro_social                                                                                        
No                                                     2.7                 83.1                  14.1
Sí                                                     4.3                 83.8                  11.8

**Estadísticos:**
- Chi-cuadrado: 3.797
- Valor p: 0.150
- Grados de libertad: 2

**Interpretación:**
La asociación entre seguro_social y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.797, p = 0.150).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
seguro_social                                                                                            
No                                                    17                 1191                   103  1311
Sí                                                     7                  386                    21   414
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
seguro_social                                                                                      
No                                                   1.3                 90.8                   7.9
Sí                                                   1.7                 93.2                   5.1

**Estadísticos:**
- Chi-cuadrado: 3.941
- Valor p: 0.139
- Grados de libertad: 2

**Interpretación:**
La asociación entre seguro_social y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.941, p = 0.139).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
seguro_social                                                                                                 
No                                                          8                 1213                    90  1311
Sí                                                          4                  384                    26   414
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
seguro_social                                                                                           
No                                                        0.6                 92.5                   6.9
Sí                                                        1.0                 92.8                   6.3

**Estadísticos:**
- Chi-cuadrado: 0.735
- Valor p: 0.693
- Grados de libertad: 2

**Interpretación:**
La asociación entre seguro_social y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.735, p = 0.693).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
seguro_social                                                                                             
No                                                     11                 1216                    84  1311
Sí                                                      6                  384                    24   414
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
seguro_social                                                                                       
No                                                    0.8                 92.8                   6.4
Sí                                                    1.4                 92.8                   5.8

**Estadísticos:**
- Chi-cuadrado: 1.376
- Valor p: 0.503
- Grados de libertad: 2

**Interpretación:**
La asociación entre seguro_social y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.376, p = 0.503).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 22. ANÁLISIS DE LA VARIABLE: TOTAL_PERSONAS_HOGAR

### Variable: total_personas_hogar
==================================================

**Distribución de la variable total_personas_hogar:**
- 3: 390 (22.6%)
- 4: 361 (20.9%)
- 5: 327 (19.0%)
- 6: 246 (14.3%)
- 7: 168 (9.7%)
- 8: 101 (5.9%)
- 9: 46 (2.7%)
- 11: 31 (1.8%)
- 10: 22 (1.3%)
- 13: 11 (0.6%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_personas_hogar                                                                                  
3                                                   3                  372                    15   390
4                                                   4                  341                    16   361
5                                                   1                  300                    26   327
6                                                   1                  234                    11   246
7                                                   2                  162                     4   168
8                                                   1                   91                     9   101
9                                                   0                   45                     1    46
10                                                  0                   22                     0    22
11                                                  0                   31                     0    31
12                                                  0                    7                     0     7
13                                                  2                    9                     0    11
15                                                  0                    5                     0     5
16                                                  0                    3                     1     4
17                                                  0                    1                     0     1
20                                                  0                    4                     0     4
25                                                  0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_personas_hogar                                                                            
3                                                 0.8                 95.4                   3.8
4                                                 1.1                 94.5                   4.4
5                                                 0.3                 91.7                   8.0
6                                                 0.4                 95.1                   4.5
7                                                 1.2                 96.4                   2.4
8                                                 1.0                 90.1                   8.9
9                                                 0.0                 97.8                   2.2
10                                                0.0                100.0                   0.0
11                                                0.0                100.0                   0.0
12                                                0.0                100.0                   0.0
13                                               18.2                 81.8                   0.0
15                                                0.0                100.0                   0.0
16                                                0.0                 75.0                  25.0
17                                                0.0                100.0                   0.0
20                                                0.0                100.0                   0.0
25                                                0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 66.558
- Valor p: 0.000
- Grados de libertad: 30

**Interpretación:**
La asociación entre total_personas_hogar y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 66.558, p = 0.000).

**Análisis por categorías:**
- **13** muestra la mayor proporción de alto riesgo (18.2%)
- **10** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_personas_hogar                                                                                       
3                                                       13                  315                    62   390
4                                                       14                  303                    44   361
5                                                        8                  278                    41   327
6                                                        5                  212                    29   246
7                                                        3                  137                    28   168
8                                                        4                   84                    13   101
9                                                        1                   39                     6    46
10                                                       2                   19                     1    22
11                                                       3                   26                     2    31
12                                                       0                    4                     3     7
13                                                       1                    9                     1    11
15                                                       0                    4                     1     5
16                                                       0                    2                     2     4
17                                                       0                    1                     0     1
20                                                       0                    3                     1     4
25                                                       0                    1                     0     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_personas_hogar                                                                                 
3                                                      3.3                 80.8                  15.9
4                                                      3.9                 83.9                  12.2
5                                                      2.4                 85.0                  12.5
6                                                      2.0                 86.2                  11.8
7                                                      1.8                 81.5                  16.7
8                                                      4.0                 83.2                  12.9
9                                                      2.2                 84.8                  13.0
10                                                     9.1                 86.4                   4.5
11                                                     9.7                 83.9                   6.5
12                                                     0.0                 57.1                  42.9
13                                                     9.1                 81.8                   9.1
15                                                     0.0                 80.0                  20.0
16                                                     0.0                 50.0                  50.0
17                                                     0.0                100.0                   0.0
20                                                     0.0                 75.0                  25.0
25                                                     0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 30.053
- Valor p: 0.463
- Grados de libertad: 30

**Interpretación:**
La asociación entre total_personas_hogar y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 30.053, p = 0.463).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_personas_hogar                                                                                     
3                                                      2                  350                    38   390
4                                                      4                  329                    28   361
5                                                      4                  304                    19   327
6                                                      2                  234                    10   246
7                                                      5                  155                     8   168
8                                                      4                   89                     8   101
9                                                      0                   42                     4    46
10                                                     1                   19                     2    22
11                                                     0                   27                     4    31
12                                                     0                    5                     2     7
13                                                     2                    9                     0    11
15                                                     0                    5                     0     5
16                                                     0                    4                     0     4
17                                                     0                    1                     0     1
20                                                     0                    3                     1     4
25                                                     0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_personas_hogar                                                                               
3                                                    0.5                 89.7                   9.7
4                                                    1.1                 91.1                   7.8
5                                                    1.2                 93.0                   5.8
6                                                    0.8                 95.1                   4.1
7                                                    3.0                 92.3                   4.8
8                                                    4.0                 88.1                   7.9
9                                                    0.0                 91.3                   8.7
10                                                   4.5                 86.4                   9.1
11                                                   0.0                 87.1                  12.9
12                                                   0.0                 71.4                  28.6
13                                                  18.2                 81.8                   0.0
15                                                   0.0                100.0                   0.0
16                                                   0.0                100.0                   0.0
17                                                   0.0                100.0                   0.0
20                                                   0.0                 75.0                  25.0
25                                                   0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 56.375
- Valor p: 0.002
- Grados de libertad: 30

**Interpretación:**
La asociación entre total_personas_hogar y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 56.375, p = 0.002).

**Análisis por categorías:**
- **13** muestra la mayor proporción de alto riesgo (18.2%)
- **15** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_personas_hogar                                                                                          
3                                                           2                  364                    24   390
4                                                           1                  339                    21   361
5                                                           1                  306                    20   327
6                                                           0                  223                    23   246
7                                                           2                  150                    16   168
8                                                           3                   94                     4   101
9                                                           0                   43                     3    46
10                                                          1                   21                     0    22
11                                                          0                   30                     1    31
12                                                          0                    7                     0     7
13                                                          2                    7                     2    11
15                                                          0                    5                     0     5
16                                                          0                    3                     1     4
17                                                          0                    1                     0     1
20                                                          0                    4                     0     4
25                                                          0                    0                     1     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_personas_hogar                                                                                    
3                                                         0.5                 93.3                   6.2
4                                                         0.3                 93.9                   5.8
5                                                         0.3                 93.6                   6.1
6                                                         0.0                 90.7                   9.3
7                                                         1.2                 89.3                   9.5
8                                                         3.0                 93.1                   4.0
9                                                         0.0                 93.5                   6.5
10                                                        4.5                 95.5                   0.0
11                                                        0.0                 96.8                   3.2
12                                                        0.0                100.0                   0.0
13                                                       18.2                 63.6                  18.2
15                                                        0.0                100.0                   0.0
16                                                        0.0                 75.0                  25.0
17                                                        0.0                100.0                   0.0
20                                                        0.0                100.0                   0.0
25                                                        0.0                  0.0                 100.0

**Estadísticos:**
- Chi-cuadrado: 94.714
- Valor p: 0.000
- Grados de libertad: 30

**Interpretación:**
La asociación entre total_personas_hogar y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 94.714, p = 0.000).

**Análisis por categorías:**
- **13** muestra la mayor proporción de alto riesgo (18.2%)
- **12** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_personas_hogar                                                                                      
3                                                       5                  366                    19   390
4                                                       4                  334                    23   361
5                                                       3                  302                    22   327
6                                                       3                  223                    20   246
7                                                       1                  158                     9   168
8                                                       0                   93                     8   101
9                                                       0                   45                     1    46
10                                                      0                   18                     4    22
11                                                      0                   30                     1    31
12                                                      0                    7                     0     7
13                                                      1                   10                     0    11
15                                                      0                    5                     0     5
16                                                      0                    3                     1     4
17                                                      0                    1                     0     1
20                                                      0                    4                     0     4
25                                                      0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_personas_hogar                                                                                
3                                                     1.3                 93.8                   4.9
4                                                     1.1                 92.5                   6.4
5                                                     0.9                 92.4                   6.7
6                                                     1.2                 90.7                   8.1
7                                                     0.6                 94.0                   5.4
8                                                     0.0                 92.1                   7.9
9                                                     0.0                 97.8                   2.2
10                                                    0.0                 81.8                  18.2
11                                                    0.0                 96.8                   3.2
12                                                    0.0                100.0                   0.0
13                                                    9.1                 90.9                   0.0
15                                                    0.0                100.0                   0.0
16                                                    0.0                 75.0                  25.0
17                                                    0.0                100.0                   0.0
20                                                    0.0                100.0                   0.0
25                                                    0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 25.349
- Valor p: 0.708
- Grados de libertad: 30

**Interpretación:**
La asociación entre total_personas_hogar y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 25.349, p = 0.708).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 23. ANÁLISIS DE LA VARIABLE: TOTAL_HERMANOS

### Variable: total_hermanos
==================================================

**Distribución de la variable total_hermanos:**
- 1: 591 (34.3%)
- 0: 540 (31.3%)
- 2: 381 (22.1%)
- 3: 144 (8.3%)
- 4: 47 (2.7%)
- 5: 17 (1.0%)
- 6: 3 (0.2%)
- 8: 1 (0.1%)
- 7: 1 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_hermanos                                                                                        
0                                                   4                  517                    19   540
1                                                   5                  560                    26   591
2                                                   4                  351                    26   381
3                                                   1                  138                     5   144
4                                                   0                   41                     6    47
5                                                   0                   16                     1    17
6                                                   0                    3                     0     3
7                                                   0                    1                     0     1
8                                                   0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_hermanos                                                                                  
0                                                 0.7                 95.7                   3.5
1                                                 0.8                 94.8                   4.4
2                                                 1.0                 92.1                   6.8
3                                                 0.7                 95.8                   3.5
4                                                 0.0                 87.2                  12.8
5                                                 0.0                 94.1                   5.9
6                                                 0.0                100.0                   0.0
7                                                 0.0                100.0                   0.0
8                                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 13.807
- Valor p: 0.613
- Grados de libertad: 16

**Interpretación:**
La asociación entre total_hermanos y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 13.807, p = 0.613).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_hermanos                                                                                             
0                                                       17                  448                    75   540
1                                                       17                  503                    71   591
2                                                       14                  311                    56   381
3                                                        6                  119                    19   144
4                                                        0                   38                     9    47
5                                                        0                   13                     4    17
6                                                        0                    3                     0     3
7                                                        0                    1                     0     1
8                                                        0                    1                     0     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_hermanos                                                                                       
0                                                      3.1                 83.0                  13.9
1                                                      2.9                 85.1                  12.0
2                                                      3.7                 81.6                  14.7
3                                                      4.2                 82.6                  13.2
4                                                      0.0                 80.9                  19.1
5                                                      0.0                 76.5                  23.5
6                                                      0.0                100.0                   0.0
7                                                      0.0                100.0                   0.0
8                                                      0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 8.277
- Valor p: 0.940
- Grados de libertad: 16

**Interpretación:**
La asociación entre total_hermanos y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.277, p = 0.940).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_hermanos                                                                                           
0                                                      7                  483                    50   540
1                                                     11                  541                    39   591
2                                                      4                  356                    21   381
3                                                      2                  133                     9   144
4                                                      0                   46                     1    47
5                                                      0                   13                     4    17
6                                                      0                    3                     0     3
7                                                      0                    1                     0     1
8                                                      0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_hermanos                                                                                     
0                                                    1.3                 89.4                   9.3
1                                                    1.9                 91.5                   6.6
2                                                    1.0                 93.4                   5.5
3                                                    1.4                 92.4                   6.2
4                                                    0.0                 97.9                   2.1
5                                                    0.0                 76.5                  23.5
6                                                    0.0                100.0                   0.0
7                                                    0.0                100.0                   0.0
8                                                    0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 16.860
- Valor p: 0.395
- Grados de libertad: 16

**Interpretación:**
La asociación entre total_hermanos y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 16.860, p = 0.395).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_hermanos                                                                                                
0                                                           4                  498                    38   540
1                                                           5                  550                    36   591
2                                                           3                  351                    27   381
3                                                           0                  132                    12   144
4                                                           0                   47                     0    47
5                                                           0                   14                     3    17
6                                                           0                    3                     0     3
7                                                           0                    1                     0     1
8                                                           0                    1                     0     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_hermanos                                                                                          
0                                                         0.7                 92.2                   7.0
1                                                         0.8                 93.1                   6.1
2                                                         0.8                 92.1                   7.1
3                                                         0.0                 91.7                   8.3
4                                                         0.0                100.0                   0.0
5                                                         0.0                 82.4                  17.6
6                                                         0.0                100.0                   0.0
7                                                         0.0                100.0                   0.0
8                                                         0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 9.853
- Valor p: 0.874
- Grados de libertad: 16

**Interpretación:**
La asociación entre total_hermanos y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 9.853, p = 0.874).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
total_hermanos                                                                                            
0                                                       4                  499                    37   540
1                                                       6                  555                    30   591
2                                                       4                  353                    24   381
3                                                       3                  129                    12   144
4                                                       0                   46                     1    47
5                                                       0                   13                     4    17
6                                                       0                    3                     0     3
7                                                       0                    1                     0     1
8                                                       0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
total_hermanos                                                                                      
0                                                     0.7                 92.4                   6.9
1                                                     1.0                 93.9                   5.1
2                                                     1.0                 92.7                   6.3
3                                                     2.1                 89.6                   8.3
4                                                     0.0                 97.9                   2.1
5                                                     0.0                 76.5                  23.5
6                                                     0.0                100.0                   0.0
7                                                     0.0                100.0                   0.0
8                                                     0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 15.994
- Valor p: 0.453
- Grados de libertad: 16

**Interpretación:**
La asociación entre total_hermanos y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 15.994, p = 0.453).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 24. ANÁLISIS DE LA VARIABLE: POSICION_NINO_HERMANOS

### Variable: posicion_nino_hermanos
==================================================

**Distribución de la variable posicion_nino_hermanos:**
- 1: 694 (40.2%)
- 2: 616 (35.7%)
- 3: 372 (21.6%)
- 4: 37 (2.1%)
- 5: 3 (0.2%)
- 6: 2 (0.1%)
- 7: 1 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
posicion_nino_hermanos                                                                                
1                                                   9                  655                    30   694
2                                                   1                  588                    27   616
3                                                   3                  348                    21   372
4                                                   1                   31                     5    37
5                                                   0                    3                     0     3
6                                                   0                    2                     0     2
7                                                   0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
posicion_nino_hermanos                                                                          
1                                                 1.3                 94.4                   4.3
2                                                 0.2                 95.5                   4.4
3                                                 0.8                 93.5                   5.6
4                                                 2.7                 83.8                  13.5
5                                                 0.0                100.0                   0.0
6                                                 0.0                100.0                   0.0
7                                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 14.683
- Valor p: 0.259
- Grados de libertad: 12

**Interpretación:**
La asociación entre posicion_nino_hermanos y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 14.683, p = 0.259).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
posicion_nino_hermanos                                                                                     
1                                                       18                  580                    96   694
2                                                       18                  513                    85   616
3                                                       14                  307                    51   372
4                                                        4                   31                     2    37
5                                                        0                    3                     0     3
6                                                        0                    2                     0     2
7                                                        0                    1                     0     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
posicion_nino_hermanos                                                                               
1                                                      2.6                 83.6                  13.8
2                                                      2.9                 83.3                  13.8
3                                                      3.8                 82.5                  13.7
4                                                     10.8                 83.8                   5.4
5                                                      0.0                100.0                   0.0
6                                                      0.0                100.0                   0.0
7                                                      0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 11.292
- Valor p: 0.504
- Grados de libertad: 12

**Interpretación:**
La asociación entre posicion_nino_hermanos y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.292, p = 0.504).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
posicion_nino_hermanos                                                                                   
1                                                      8                  617                    69   694
2                                                      9                  571                    36   616
3                                                      6                  348                    18   372
4                                                      1                   35                     1    37
5                                                      0                    3                     0     3
6                                                      0                    2                     0     2
7                                                      0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
posicion_nino_hermanos                                                                             
1                                                    1.2                 88.9                   9.9
2                                                    1.5                 92.7                   5.8
3                                                    1.6                 93.5                   4.8
4                                                    2.7                 94.6                   2.7
5                                                    0.0                100.0                   0.0
6                                                    0.0                100.0                   0.0
7                                                    0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 15.036
- Valor p: 0.239
- Grados de libertad: 12

**Interpretación:**
La asociación entre posicion_nino_hermanos y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 15.036, p = 0.239).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
posicion_nino_hermanos                                                                                        
1                                                           5                  638                    51   694
2                                                           4                  575                    37   616
3                                                           3                  346                    23   372
4                                                           0                   32                     5    37
5                                                           0                    3                     0     3
6                                                           0                    2                     0     2
7                                                           0                    1                     0     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
posicion_nino_hermanos                                                                                  
1                                                         0.7                 91.9                   7.3
2                                                         0.6                 93.3                   6.0
3                                                         0.8                 93.0                   6.2
4                                                         0.0                 86.5                  13.5
5                                                         0.0                100.0                   0.0
6                                                         0.0                100.0                   0.0
7                                                         0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 4.628
- Valor p: 0.969
- Grados de libertad: 12

**Interpretación:**
La asociación entre posicion_nino_hermanos y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.628, p = 0.969).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
posicion_nino_hermanos                                                                                    
1                                                       6                  644                    44   694
2                                                       6                  572                    38   616
3                                                       3                  345                    24   372
4                                                       2                   33                     2    37
5                                                       0                    3                     0     3
6                                                       0                    2                     0     2
7                                                       0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
posicion_nino_hermanos                                                                              
1                                                     0.9                 92.8                   6.3
2                                                     1.0                 92.9                   6.2
3                                                     0.8                 92.7                   6.5
4                                                     5.4                 89.2                   5.4
5                                                     0.0                100.0                   0.0
6                                                     0.0                100.0                   0.0
7                                                     0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 8.160
- Valor p: 0.773
- Grados de libertad: 12

**Interpretación:**
La asociación entre posicion_nino_hermanos y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.160, p = 0.773).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 25. ANÁLISIS DE LA VARIABLE: ESTADO_CIVIL_CUIDADOR

### Variable: estado_civil_cuidador
==================================================

**Distribución de la variable estado_civil_cuidador:**
- Casado: 975 (56.5%)
- Unido: 437 (25.3%)
- Soltero: 313 (18.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
estado_civil_cuidador                                                                                 
Casado                                             11                  912                    52   975
Soltero                                             2                  288                    23   313
Unido                                               1                  428                     8   437
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
estado_civil_cuidador                                                                           
Casado                                            1.1                 93.5                   5.3
Soltero                                           0.6                 92.0                   7.3
Unido                                             0.2                 97.9                   1.8

**Estadísticos:**
- Chi-cuadrado: 16.802
- Valor p: 0.002
- Grados de libertad: 4

**Interpretación:**
La asociación entre estado_civil_cuidador y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 16.802, p = 0.002).

**Análisis por categorías:**
- **Casado** muestra la mayor proporción de alto riesgo (1.1%)
- **Unido** muestra la mayor proporción de desarrollo adecuado (97.9%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
estado_civil_cuidador                                                                                      
Casado                                                  37                  806                   132   975
Soltero                                                  6                  254                    53   313
Unido                                                   11                  377                    49   437
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
estado_civil_cuidador                                                                                
Casado                                                 3.8                 82.7                  13.5
Soltero                                                1.9                 81.2                  16.9
Unido                                                  2.5                 86.3                  11.2

**Estadísticos:**
- Chi-cuadrado: 8.456
- Valor p: 0.076
- Grados de libertad: 4

**Interpretación:**
La asociación entre estado_civil_cuidador y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.456, p = 0.076).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
estado_civil_cuidador                                                                                    
Casado                                                13                  894                    68   975
Soltero                                                5                  283                    25   313
Unido                                                  6                  400                    31   437
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
estado_civil_cuidador                                                                              
Casado                                               1.3                 91.7                   7.0
Soltero                                              1.6                 90.4                   8.0
Unido                                                1.4                 91.5                   7.1

**Estadísticos:**
- Chi-cuadrado: 0.509
- Valor p: 0.973
- Grados de libertad: 4

**Interpretación:**
La asociación entre estado_civil_cuidador y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.509, p = 0.973).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
estado_civil_cuidador                                                                                         
Casado                                                     10                  903                    62   975
Soltero                                                     2                  278                    33   313
Unido                                                       0                  416                    21   437
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
estado_civil_cuidador                                                                                   
Casado                                                    1.0                 92.6                   6.4
Soltero                                                   0.6                 88.8                  10.5
Unido                                                     0.0                 95.2                   4.8

**Estadísticos:**
- Chi-cuadrado: 14.756
- Valor p: 0.005
- Grados de libertad: 4

**Interpretación:**
La asociación entre estado_civil_cuidador y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 14.756, p = 0.005).

**Análisis por categorías:**
- **Casado** muestra la mayor proporción de alto riesgo (1.0%)
- **Unido** muestra la mayor proporción de desarrollo adecuado (95.2%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
estado_civil_cuidador                                                                                     
Casado                                                 12                  902                    61   975
Soltero                                                 0                  286                    27   313
Unido                                                   5                  412                    20   437
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
estado_civil_cuidador                                                                               
Casado                                                1.2                 92.5                   6.3
Soltero                                               0.0                 91.4                   8.6
Unido                                                 1.1                 94.3                   4.6

**Estadísticos:**
- Chi-cuadrado: 8.748
- Valor p: 0.068
- Grados de libertad: 4

**Interpretación:**
La asociación entre estado_civil_cuidador y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 8.748, p = 0.068).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 26. ANÁLISIS DE LA VARIABLE: HORAS_PANTALLA

### Variable: horas_pantalla
==================================================

**Distribución de la variable horas_pantalla:**
- 0.0: 661 (38.3%)
- 1.0: 578 (33.5%)
- 2.0: 266 (15.4%)
- 3.0: 106 (6.1%)
- 4.0: 45 (2.6%)
- 0.5: 26 (1.5%)
- 5.0: 24 (1.4%)
- 6.0: 9 (0.5%)
- 7.0: 6 (0.3%)
- 9.0: 2 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_pantalla                                                                                        
0.0                                                 4                  629                    28   661
0.5                                                 0                   22                     4    26
1.0                                                 6                  541                    31   578
2.0                                                 2                  252                    12   266
3.0                                                 1                  100                     5   106
4.0                                                 1                   42                     2    45
5.0                                                 0                   24                     0    24
6.0                                                 0                    8                     1     9
7.0                                                 0                    6                     0     6
8.0                                                 0                    1                     0     1
9.0                                                 0                    2                     0     2
12.0                                                0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_pantalla                                                                                  
0.0                                               0.6                 95.2                   4.2
0.5                                               0.0                 84.6                  15.4
1.0                                               1.0                 93.6                   5.4
2.0                                               0.8                 94.7                   4.5
3.0                                               0.9                 94.3                   4.7
4.0                                               2.2                 93.3                   4.4
5.0                                               0.0                100.0                   0.0
6.0                                               0.0                 88.9                  11.1
7.0                                               0.0                100.0                   0.0
8.0                                               0.0                100.0                   0.0
9.0                                               0.0                100.0                   0.0
12.0                                              0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 12.208
- Valor p: 0.953
- Grados de libertad: 22

**Interpretación:**
La asociación entre horas_pantalla y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.208, p = 0.953).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_pantalla                                                                                             
0.0                                                     24                  542                    95   661
0.5                                                      0                   24                     2    26
1.0                                                     19                  487                    72   578
2.0                                                      6                  229                    31   266
3.0                                                      2                   90                    14   106
4.0                                                      0                   31                    14    45
5.0                                                      2                   21                     1    24
6.0                                                      0                    4                     5     9
7.0                                                      0                    6                     0     6
8.0                                                      0                    1                     0     1
9.0                                                      1                    1                     0     2
12.0                                                     0                    1                     0     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_pantalla                                                                                       
0.0                                                    3.6                 82.0                  14.4
0.5                                                    0.0                 92.3                   7.7
1.0                                                    3.3                 84.3                  12.5
2.0                                                    2.3                 86.1                  11.7
3.0                                                    1.9                 84.9                  13.2
4.0                                                    0.0                 68.9                  31.1
5.0                                                    8.3                 87.5                   4.2
6.0                                                    0.0                 44.4                  55.6
7.0                                                    0.0                100.0                   0.0
8.0                                                    0.0                100.0                   0.0
9.0                                                   50.0                 50.0                   0.0
12.0                                                   0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 51.742
- Valor p: 0.000
- Grados de libertad: 22

**Interpretación:**
La asociación entre horas_pantalla y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 51.742, p = 0.000).

**Análisis por categorías:**
- **9.0** muestra la mayor proporción de alto riesgo (50.0%)
- **7.0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_pantalla                                                                                           
0.0                                                    7                  600                    54   661
0.5                                                    1                   23                     2    26
1.0                                                    8                  532                    38   578
2.0                                                    5                  244                    17   266
3.0                                                    1                   98                     7   106
4.0                                                    0                   41                     4    45
5.0                                                    0                   24                     0    24
6.0                                                    2                    6                     1     9
7.0                                                    0                    5                     1     6
8.0                                                    0                    1                     0     1
9.0                                                    0                    2                     0     2
12.0                                                   0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_pantalla                                                                                     
0.0                                                  1.1                 90.8                   8.2
0.5                                                  3.8                 88.5                   7.7
1.0                                                  1.4                 92.0                   6.6
2.0                                                  1.9                 91.7                   6.4
3.0                                                  0.9                 92.5                   6.6
4.0                                                  0.0                 91.1                   8.9
5.0                                                  0.0                100.0                   0.0
6.0                                                 22.2                 66.7                  11.1
7.0                                                  0.0                 83.3                  16.7
8.0                                                  0.0                100.0                   0.0
9.0                                                  0.0                100.0                   0.0
12.0                                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 37.015
- Valor p: 0.024
- Grados de libertad: 22

**Interpretación:**
La asociación entre horas_pantalla y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 37.015, p = 0.024).

**Análisis por categorías:**
- **6.0** muestra la mayor proporción de alto riesgo (22.2%)
- **5.0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_pantalla                                                                                                
0.0                                                         4                  612                    45   661
0.5                                                         1                   24                     1    26
1.0                                                         4                  539                    35   578
2.0                                                         2                  246                    18   266
3.0                                                         1                   93                    12   106
4.0                                                         0                   41                     4    45
5.0                                                         0                   24                     0    24
6.0                                                         0                    9                     0     9
7.0                                                         0                    5                     1     6
8.0                                                         0                    1                     0     1
9.0                                                         0                    2                     0     2
12.0                                                        0                    1                     0     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_pantalla                                                                                          
0.0                                                       0.6                 92.6                   6.8
0.5                                                       3.8                 92.3                   3.8
1.0                                                       0.7                 93.3                   6.1
2.0                                                       0.8                 92.5                   6.8
3.0                                                       0.9                 87.7                  11.3
4.0                                                       0.0                 91.1                   8.9
5.0                                                       0.0                100.0                   0.0
6.0                                                       0.0                100.0                   0.0
7.0                                                       0.0                 83.3                  16.7
8.0                                                       0.0                100.0                   0.0
9.0                                                       0.0                100.0                   0.0
12.0                                                      0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 12.815
- Valor p: 0.938
- Grados de libertad: 22

**Interpretación:**
La asociación entre horas_pantalla y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.815, p = 0.938).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_pantalla                                                                                            
0.0                                                     6                  614                    41   661
0.5                                                     0                   23                     3    26
1.0                                                     7                  538                    33   578
2.0                                                     4                  246                    16   266
3.0                                                     0                   99                     7   106
4.0                                                     0                   43                     2    45
5.0                                                     0                   20                     4    24
6.0                                                     0                    7                     2     9
7.0                                                     0                    6                     0     6
8.0                                                     0                    1                     0     1
9.0                                                     0                    2                     0     2
12.0                                                    0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_pantalla                                                                                      
0.0                                                   0.9                 92.9                   6.2
0.5                                                   0.0                 88.5                  11.5
1.0                                                   1.2                 93.1                   5.7
2.0                                                   1.5                 92.5                   6.0
3.0                                                   0.0                 93.4                   6.6
4.0                                                   0.0                 95.6                   4.4
5.0                                                   0.0                 83.3                  16.7
6.0                                                   0.0                 77.8                  22.2
7.0                                                   0.0                100.0                   0.0
8.0                                                   0.0                100.0                   0.0
9.0                                                   0.0                100.0                   0.0
12.0                                                  0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 14.003
- Valor p: 0.901
- Grados de libertad: 22

**Interpretación:**
La asociación entre horas_pantalla y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 14.003, p = 0.901).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 27. ANÁLISIS DE LA VARIABLE: HORAS_JUEGO_CUIDADOR

### Variable: horas_juego_cuidador
==================================================

**Distribución de la variable horas_juego_cuidador:**
- 2.0: 487 (28.2%)
- 3.0: 466 (27.0%)
- 1.0: 322 (18.7%)
- 4.0: 286 (16.6%)
- 5.0: 88 (5.1%)
- 0.0: 38 (2.2%)
- 6.0: 22 (1.3%)
- 8.0: 7 (0.4%)
- 0.5: 4 (0.2%)
- 7.0: 4 (0.2%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_juego_cuidador                                                                                  
0.0                                                 1                   36                     1    38
0.5                                                 0                    4                     0     4
1.0                                                 5                  298                    19   322
2.0                                                 1                  459                    27   487
3.0                                                 4                  441                    21   466
4.0                                                 2                  270                    14   286
5.0                                                 1                   86                     1    88
6.0                                                 0                   22                     0    22
7.0                                                 0                    4                     0     4
8.0                                                 0                    7                     0     7
10.0                                                0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_juego_cuidador                                                                            
0.0                                               2.6                 94.7                   2.6
0.5                                               0.0                100.0                   0.0
1.0                                               1.6                 92.5                   5.9
2.0                                               0.2                 94.3                   5.5
3.0                                               0.9                 94.6                   4.5
4.0                                               0.7                 94.4                   4.9
5.0                                               1.1                 97.7                   1.1
6.0                                               0.0                100.0                   0.0
7.0                                               0.0                100.0                   0.0
8.0                                               0.0                100.0                   0.0
10.0                                              0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 12.872
- Valor p: 0.883
- Grados de libertad: 20

**Interpretación:**
La asociación entre horas_juego_cuidador y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.872, p = 0.883).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_juego_cuidador                                                                                       
0.0                                                      1                   32                     5    38
0.5                                                      0                    4                     0     4
1.0                                                     13                  275                    34   322
2.0                                                     16                  401                    70   487
3.0                                                     14                  384                    68   466
4.0                                                      7                  234                    45   286
5.0                                                      3                   76                     9    88
6.0                                                      0                   20                     2    22
7.0                                                      0                    3                     1     4
8.0                                                      0                    7                     0     7
10.0                                                     0                    1                     0     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_juego_cuidador                                                                                 
0.0                                                    2.6                 84.2                  13.2
0.5                                                    0.0                100.0                   0.0
1.0                                                    4.0                 85.4                  10.6
2.0                                                    3.3                 82.3                  14.4
3.0                                                    3.0                 82.4                  14.6
4.0                                                    2.4                 81.8                  15.7
5.0                                                    3.4                 86.4                  10.2
6.0                                                    0.0                 90.9                   9.1
7.0                                                    0.0                 75.0                  25.0
8.0                                                    0.0                100.0                   0.0
10.0                                                   0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 10.410
- Valor p: 0.960
- Grados de libertad: 20

**Interpretación:**
La asociación entre horas_juego_cuidador y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.410, p = 0.960).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_juego_cuidador                                                                                     
0.0                                                    0                   36                     2    38
0.5                                                    1                    2                     1     4
1.0                                                    7                  290                    25   322
2.0                                                    6                  443                    38   487
3.0                                                    5                  439                    22   466
4.0                                                    5                  259                    22   286
5.0                                                    0                   77                    11    88
6.0                                                    0                   20                     2    22
7.0                                                    0                    4                     0     4
8.0                                                    0                    6                     1     7
10.0                                                   0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_juego_cuidador                                                                               
0.0                                                  0.0                 94.7                   5.3
0.5                                                 25.0                 50.0                  25.0
1.0                                                  2.2                 90.1                   7.8
2.0                                                  1.2                 91.0                   7.8
3.0                                                  1.1                 94.2                   4.7
4.0                                                  1.7                 90.6                   7.7
5.0                                                  0.0                 87.5                  12.5
6.0                                                  0.0                 90.9                   9.1
7.0                                                  0.0                100.0                   0.0
8.0                                                  0.0                 85.7                  14.3
10.0                                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 32.691
- Valor p: 0.036
- Grados de libertad: 20

**Interpretación:**
La asociación entre horas_juego_cuidador y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 32.691, p = 0.036).

**Análisis por categorías:**
- **0.5** muestra la mayor proporción de alto riesgo (25.0%)
- **7.0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_juego_cuidador                                                                                          
0.0                                                         0                   34                     4    38
0.5                                                         1                    2                     1     4
1.0                                                         5                  291                    26   322
2.0                                                         1                  460                    26   487
3.0                                                         1                  440                    25   466
4.0                                                         2                  254                    30   286
5.0                                                         2                   83                     3    88
6.0                                                         0                   21                     1    22
7.0                                                         0                    4                     0     4
8.0                                                         0                    7                     0     7
10.0                                                        0                    1                     0     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_juego_cuidador                                                                                    
0.0                                                       0.0                 89.5                  10.5
0.5                                                      25.0                 50.0                  25.0
1.0                                                       1.6                 90.4                   8.1
2.0                                                       0.2                 94.5                   5.3
3.0                                                       0.2                 94.4                   5.4
4.0                                                       0.7                 88.8                  10.5
5.0                                                       2.3                 94.3                   3.4
6.0                                                       0.0                 95.5                   4.5
7.0                                                       0.0                100.0                   0.0
8.0                                                       0.0                100.0                   0.0
10.0                                                      0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 60.930
- Valor p: 0.000
- Grados de libertad: 20

**Interpretación:**
La asociación entre horas_juego_cuidador y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 60.930, p = 0.000).

**Análisis por categorías:**
- **0.5** muestra la mayor proporción de alto riesgo (25.0%)
- **7.0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
horas_juego_cuidador                                                                                      
0.0                                                     1                   37                     0    38
0.5                                                     0                    1                     3     4
1.0                                                     1                  294                    27   322
2.0                                                     3                  454                    30   487
3.0                                                     8                  437                    21   466
4.0                                                     3                  262                    21   286
5.0                                                     1                   83                     4    88
6.0                                                     0                   21                     1    22
7.0                                                     0                    4                     0     4
8.0                                                     0                    6                     1     7
10.0                                                    0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
horas_juego_cuidador                                                                                
0.0                                                   2.6                 97.4                   0.0
0.5                                                   0.0                 25.0                  75.0
1.0                                                   0.3                 91.3                   8.4
2.0                                                   0.6                 93.2                   6.2
3.0                                                   1.7                 93.8                   4.5
4.0                                                   1.0                 91.6                   7.3
5.0                                                   1.1                 94.3                   4.5
6.0                                                   0.0                 95.5                   4.5
7.0                                                   0.0                100.0                   0.0
8.0                                                   0.0                 85.7                  14.3
10.0                                                  0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 47.765
- Valor p: 0.000
- Grados de libertad: 20

**Interpretación:**
La asociación entre horas_juego_cuidador y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 47.765, p = 0.000).

**Análisis por categorías:**
- **0.0** muestra la mayor proporción de alto riesgo (2.6%)
- **7.0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------


## 28. ANÁLISIS DE LA VARIABLE: NUMERO_CONTROLES_PRENATALES

### Variable: numero_controles_prenatales
==================================================

**Distribución de la variable numero_controles_prenatales:**
- 9: 351 (20.3%)
- 6: 315 (18.3%)
- 7: 288 (16.7%)
- 5: 248 (14.4%)
- 8: 225 (13.0%)
- 4: 140 (8.1%)
- 3: 59 (3.4%)
- 10: 53 (3.1%)
- 2: 18 (1.0%)
- 0: 8 (0.5%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
numero_controles_prenatales                                                                           
0                                                   0                    6                     2     8
1                                                   0                    8                     0     8
2                                                   0                   17                     1    18
3                                                   0                   54                     5    59
4                                                   1                  134                     5   140
5                                                   0                  236                    12   248
6                                                   3                  295                    17   315
7                                                   5                  276                     7   288
8                                                   1                  209                    15   225
9                                                   3                  334                    14   351
10                                                  1                   49                     3    53
11                                                  0                    7                     1     8
12                                                  0                    2                     1     3
14                                                  0                    1                     0     1
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
numero_controles_prenatales                                                                     
0                                                 0.0                 75.0                  25.0
1                                                 0.0                100.0                   0.0
2                                                 0.0                 94.4                   5.6
3                                                 0.0                 91.5                   8.5
4                                                 0.7                 95.7                   3.6
5                                                 0.0                 95.2                   4.8
6                                                 1.0                 93.7                   5.4
7                                                 1.7                 95.8                   2.4
8                                                 0.4                 92.9                   6.7
9                                                 0.9                 95.2                   4.0
10                                                1.9                 92.5                   5.7
11                                                0.0                 87.5                  12.5
12                                                0.0                 66.7                  33.3
14                                                0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 29.211
- Valor p: 0.302
- Grados de libertad: 26

**Interpretación:**
La asociación entre numero_controles_prenatales y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 29.211, p = 0.302).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
numero_controles_prenatales                                                                                
0                                                        0                    7                     1     8
1                                                        0                    6                     2     8
2                                                        1                   15                     2    18
3                                                        0                   50                     9    59
4                                                        2                  112                    26   140
5                                                        5                  213                    30   248
6                                                        8                  265                    42   315
7                                                        8                  242                    38   288
8                                                       12                  189                    24   225
9                                                       15                  286                    50   351
10                                                       2                   43                     8    53
11                                                       1                    6                     1     8
12                                                       0                    3                     0     3
14                                                       0                    0                     1     1
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
numero_controles_prenatales                                                                          
0                                                      0.0                 87.5                  12.5
1                                                      0.0                 75.0                  25.0
2                                                      5.6                 83.3                  11.1
3                                                      0.0                 84.7                  15.3
4                                                      1.4                 80.0                  18.6
5                                                      2.0                 85.9                  12.1
6                                                      2.5                 84.1                  13.3
7                                                      2.8                 84.0                  13.2
8                                                      5.3                 84.0                  10.7
9                                                      4.3                 81.5                  14.2
10                                                     3.8                 81.1                  15.1
11                                                    12.5                 75.0                  12.5
12                                                     0.0                100.0                   0.0
14                                                     0.0                  0.0                 100.0

**Estadísticos:**
- Chi-cuadrado: 26.058
- Valor p: 0.460
- Grados de libertad: 26

**Interpretación:**
La asociación entre numero_controles_prenatales y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 26.058, p = 0.460).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
numero_controles_prenatales                                                                              
0                                                      0                    8                     0     8
1                                                      0                    8                     0     8
2                                                      2                   13                     3    18
3                                                      0                   54                     5    59
4                                                      5                  127                     8   140
5                                                      3                  229                    16   248
6                                                      3                  283                    29   315
7                                                      3                  260                    25   288
8                                                      4                  201                    20   225
9                                                      3                  333                    15   351
10                                                     0                   50                     3    53
11                                                     1                    7                     0     8
12                                                     0                    3                     0     3
14                                                     0                    1                     0     1
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
numero_controles_prenatales                                                                        
0                                                    0.0                100.0                   0.0
1                                                    0.0                100.0                   0.0
2                                                   11.1                 72.2                  16.7
3                                                    0.0                 91.5                   8.5
4                                                    3.6                 90.7                   5.7
5                                                    1.2                 92.3                   6.5
6                                                    1.0                 89.8                   9.2
7                                                    1.0                 90.3                   8.7
8                                                    1.8                 89.3                   8.9
9                                                    0.9                 94.9                   4.3
10                                                   0.0                 94.3                   5.7
11                                                  12.5                 87.5                   0.0
12                                                   0.0                100.0                   0.0
14                                                   0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 42.236
- Valor p: 0.023
- Grados de libertad: 26

**Interpretación:**
La asociación entre numero_controles_prenatales y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 42.236, p = 0.023).

**Análisis por categorías:**
- **11** muestra la mayor proporción de alto riesgo (12.5%)
- **0** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
numero_controles_prenatales                                                                                   
0                                                           0                    7                     1     8
1                                                           0                    8                     0     8
2                                                           0                   17                     1    18
3                                                           0                   51                     8    59
4                                                           1                  133                     6   140
5                                                           1                  229                    18   248
6                                                           4                  291                    20   315
7                                                           2                  265                    21   288
8                                                           3                  208                    14   225
9                                                           1                  330                    20   351
10                                                          0                   47                     6    53
11                                                          0                    8                     0     8
12                                                          0                    2                     1     3
14                                                          0                    1                     0     1
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
numero_controles_prenatales                                                                             
0                                                         0.0                 87.5                  12.5
1                                                         0.0                100.0                   0.0
2                                                         0.0                 94.4                   5.6
3                                                         0.0                 86.4                  13.6
4                                                         0.7                 95.0                   4.3
5                                                         0.4                 92.3                   7.3
6                                                         1.3                 92.4                   6.3
7                                                         0.7                 92.0                   7.3
8                                                         1.3                 92.4                   6.2
9                                                         0.3                 94.0                   5.7
10                                                        0.0                 88.7                  11.3
11                                                        0.0                100.0                   0.0
12                                                        0.0                 66.7                  33.3
14                                                        0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 18.600
- Valor p: 0.853
- Grados de libertad: 26

**Interpretación:**
La asociación entre numero_controles_prenatales y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 18.600, p = 0.853).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
numero_controles_prenatales                                                                               
0                                                       0                    8                     0     8
1                                                       0                    8                     0     8
2                                                       1                   16                     1    18
3                                                       1                   54                     4    59
4                                                       2                  123                    15   140
5                                                       1                  228                    19   248
6                                                       1                  295                    19   315
7                                                       4                  270                    14   288
8                                                       2                  208                    15   225
9                                                       5                  331                    15   351
10                                                      0                   48                     5    53
11                                                      0                    8                     0     8
12                                                      0                    2                     1     3
14                                                      0                    1                     0     1
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
numero_controles_prenatales                                                                         
0                                                     0.0                100.0                   0.0
1                                                     0.0                100.0                   0.0
2                                                     5.6                 88.9                   5.6
3                                                     1.7                 91.5                   6.8
4                                                     1.4                 87.9                  10.7
5                                                     0.4                 91.9                   7.7
6                                                     0.3                 93.7                   6.0
7                                                     1.4                 93.8                   4.9
8                                                     0.9                 92.4                   6.7
9                                                     1.4                 94.3                   4.3
10                                                    0.0                 90.6                   9.4
11                                                    0.0                100.0                   0.0
12                                                    0.0                 66.7                  33.3
14                                                    0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 23.996
- Valor p: 0.576
- Grados de libertad: 26

**Interpretación:**
La asociación entre numero_controles_prenatales y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 23.996, p = 0.576).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 29. ANÁLISIS DE LA VARIABLE: ULTRASONIDO_EMBARAZO

### Variable: ultrasonido_embarazo
==================================================

**Distribución de la variable ultrasonido_embarazo:**
- Sí: 1631 (94.6%)
- No: 94 (5.4%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
ultrasonido_embarazo                                                                                  
No                                                  1                   87                     6    94
Sí                                                 13                 1541                    77  1631
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
ultrasonido_embarazo                                                                            
No                                                1.1                 92.6                   6.4
Sí                                                0.8                 94.5                   4.7

**Estadísticos:**
- Chi-cuadrado: 0.623
- Valor p: 0.732
- Grados de libertad: 2

**Interpretación:**
La asociación entre ultrasonido_embarazo y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.623, p = 0.732).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
ultrasonido_embarazo                                                                                       
No                                                       5                   74                    15    94
Sí                                                      49                 1363                   219  1631
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
ultrasonido_embarazo                                                                                 
No                                                     5.3                 78.7                  16.0
Sí                                                     3.0                 83.6                  13.4

**Estadísticos:**
- Chi-cuadrado: 2.191
- Valor p: 0.334
- Grados de libertad: 2

**Interpretación:**
La asociación entre ultrasonido_embarazo y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.191, p = 0.334).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
ultrasonido_embarazo                                                                                     
No                                                     0                   91                     3    94
Sí                                                    24                 1486                   121  1631
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
ultrasonido_embarazo                                                                               
No                                                   0.0                 96.8                   3.2
Sí                                                   1.5                 91.1                   7.4

**Estadísticos:**
- Chi-cuadrado: 3.908
- Valor p: 0.142
- Grados de libertad: 2

**Interpretación:**
La asociación entre ultrasonido_embarazo y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.908, p = 0.142).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
ultrasonido_embarazo                                                                                          
No                                                          0                   87                     7    94
Sí                                                         12                 1510                   109  1631
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
ultrasonido_embarazo                                                                                    
No                                                        0.0                 92.6                   7.4
Sí                                                        0.7                 92.6                   6.7

**Estadísticos:**
- Chi-cuadrado: 0.769
- Valor p: 0.681
- Grados de libertad: 2

**Interpretación:**
La asociación entre ultrasonido_embarazo y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.769, p = 0.681).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
ultrasonido_embarazo                                                                                      
No                                                      2                   84                     8    94
Sí                                                     15                 1516                   100  1631
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
ultrasonido_embarazo                                                                                
No                                                    2.1                 89.4                   8.5
Sí                                                    0.9                 92.9                   6.1

**Estadísticos:**
- Chi-cuadrado: 2.243
- Valor p: 0.326
- Grados de libertad: 2

**Interpretación:**
La asociación entre ultrasonido_embarazo y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.243, p = 0.326).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 30. ANÁLISIS DE LA VARIABLE: PRENATALES_PRIMEROS_3_MESES

### Variable: prenatales_primeros_3_meses
==================================================

**Distribución de la variable prenatales_primeros_3_meses:**
- Sí: 1521 (88.2%)
- No: 204 (11.8%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_primeros_3_meses                                                                           
No                                                  2                  190                    12   204
Sí                                                 12                 1438                    71  1521
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_primeros_3_meses                                                                     
No                                                1.0                 93.1                   5.9
Sí                                                0.8                 94.5                   4.7

**Estadísticos:**
- Chi-cuadrado: 0.670
- Valor p: 0.715
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_primeros_3_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.670, p = 0.715).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_primeros_3_meses                                                                                
No                                                       4                  162                    38   204
Sí                                                      50                 1275                   196  1521
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_primeros_3_meses                                                                          
No                                                     2.0                 79.4                  18.6
Sí                                                     3.3                 83.8                  12.9

**Estadísticos:**
- Chi-cuadrado: 5.803
- Valor p: 0.055
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_primeros_3_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.803, p = 0.055).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_primeros_3_meses                                                                              
No                                                     2                  185                    17   204
Sí                                                    22                 1392                   107  1521
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_primeros_3_meses                                                                        
No                                                   1.0                 90.7                   8.3
Sí                                                   1.4                 91.5                   7.0

**Estadísticos:**
- Chi-cuadrado: 0.716
- Valor p: 0.699
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_primeros_3_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.716, p = 0.699).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_primeros_3_meses                                                                                   
No                                                          2                  183                    19   204
Sí                                                         10                 1414                    97  1521
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_primeros_3_meses                                                                             
No                                                        1.0                 89.7                   9.3
Sí                                                        0.7                 93.0                   6.4

**Estadísticos:**
- Chi-cuadrado: 2.782
- Valor p: 0.249
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_primeros_3_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.782, p = 0.249).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_primeros_3_meses                                                                               
No                                                      2                  184                    18   204
Sí                                                     15                 1416                    90  1521
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_primeros_3_meses                                                                         
No                                                    1.0                 90.2                   8.8
Sí                                                    1.0                 93.1                   5.9

**Estadísticos:**
- Chi-cuadrado: 2.590
- Valor p: 0.274
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_primeros_3_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.590, p = 0.274).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 31. ANÁLISIS DE LA VARIABLE: PRENATALES_RESTO_EMBARAZO

### Variable: prenatales_resto_embarazo
==================================================

**Distribución de la variable prenatales_resto_embarazo:**
- Sí: 1603 (92.9%)
- No: 122 (7.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_resto_embarazo                                                                             
No                                                  0                  116                     6   122
Sí                                                 14                 1512                    77  1603
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_resto_embarazo                                                                       
No                                                0.0                 95.1                   4.9
Sí                                                0.9                 94.3                   4.8

**Estadísticos:**
- Chi-cuadrado: 1.076
- Valor p: 0.584
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_resto_embarazo y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.076, p = 0.584).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_resto_embarazo                                                                                  
No                                                       3                   98                    21   122
Sí                                                      51                 1339                   213  1603
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_resto_embarazo                                                                            
No                                                     2.5                 80.3                  17.2
Sí                                                     3.2                 83.5                  13.3

**Estadísticos:**
- Chi-cuadrado: 1.617
- Valor p: 0.446
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_resto_embarazo y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.617, p = 0.446).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_resto_embarazo                                                                                
No                                                     2                  107                    13   122
Sí                                                    22                 1470                   111  1603
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_resto_embarazo                                                                          
No                                                   1.6                 87.7                  10.7
Sí                                                   1.4                 91.7                   6.9

**Estadísticos:**
- Chi-cuadrado: 2.452
- Valor p: 0.293
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_resto_embarazo y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.452, p = 0.293).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_resto_embarazo                                                                                     
No                                                          0                  111                    11   122
Sí                                                         12                 1486                   105  1603
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_resto_embarazo                                                                               
No                                                        0.0                 91.0                   9.0
Sí                                                        0.7                 92.7                   6.6

**Estadísticos:**
- Chi-cuadrado: 1.975
- Valor p: 0.373
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_resto_embarazo y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.975, p = 0.373).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
prenatales_resto_embarazo                                                                                 
No                                                      1                  113                     8   122
Sí                                                     16                 1487                   100  1603
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
prenatales_resto_embarazo                                                                           
No                                                    0.8                 92.6                   6.6
Sí                                                    1.0                 92.8                   6.2

**Estadísticos:**
- Chi-cuadrado: 0.055
- Valor p: 0.973
- Grados de libertad: 2

**Interpretación:**
La asociación entre prenatales_resto_embarazo y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.055, p = 0.973).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 32. ANÁLISIS DE LA VARIABLE: SERVICIO_ASISTENCIA_PARTO

### Variable: servicio_asistencia_parto
==================================================

**Distribución de la variable servicio_asistencia_parto:**
- Hospital público: 1116 (64.7%)
- Hospital privado: 408 (23.7%)
- Seguro social: 159 (9.2%)
- Comadrona: 37 (2.1%)
- CAIMI: 5 (0.3%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
servicio_asistencia_parto                                                                             
CAIMI                                               0                    5                     0     5
Comadrona                                           0                   35                     2    37
Hospital privado                                    5                  386                    17   408
Hospital público                                    8                 1048                    60  1116
Seguro social                                       1                  154                     4   159
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
servicio_asistencia_parto                                                                       
CAIMI                                             0.0                100.0                   0.0
Comadrona                                         0.0                 94.6                   5.4
Hospital privado                                  1.2                 94.6                   4.2
Hospital público                                  0.7                 93.9                   5.4
Seguro social                                     0.6                 96.9                   2.5

**Estadísticos:**
- Chi-cuadrado: 4.642
- Valor p: 0.795
- Grados de libertad: 8

**Interpretación:**
La asociación entre servicio_asistencia_parto y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.642, p = 0.795).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
servicio_asistencia_parto                                                                                  
CAIMI                                                    1                    4                     0     5
Comadrona                                                1                   35                     1    37
Hospital privado                                        11                  338                    59   408
Hospital público                                        34                  933                   149  1116
Seguro social                                            7                  127                    25   159
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
servicio_asistencia_parto                                                                            
CAIMI                                                 20.0                 80.0                   0.0
Comadrona                                              2.7                 94.6                   2.7
Hospital privado                                       2.7                 82.8                  14.5
Hospital público                                       3.0                 83.6                  13.4
Seguro social                                          4.4                 79.9                  15.7

**Estadísticos:**
- Chi-cuadrado: 11.201
- Valor p: 0.191
- Grados de libertad: 8

**Interpretación:**
La asociación entre servicio_asistencia_parto y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.201, p = 0.191).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
servicio_asistencia_parto                                                                                
CAIMI                                                  0                    4                     1     5
Comadrona                                              1                   32                     4    37
Hospital privado                                       5                  382                    21   408
Hospital público                                      15                 1011                    90  1116
Seguro social                                          3                  148                     8   159
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
servicio_asistencia_parto                                                                          
CAIMI                                                0.0                 80.0                  20.0
Comadrona                                            2.7                 86.5                  10.8
Hospital privado                                     1.2                 93.6                   5.1
Hospital público                                     1.3                 90.6                   8.1
Seguro social                                        1.9                 93.1                   5.0

**Estadísticos:**
- Chi-cuadrado: 7.828
- Valor p: 0.450
- Grados de libertad: 8

**Interpretación:**
La asociación entre servicio_asistencia_parto y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.828, p = 0.450).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
servicio_asistencia_parto                                                                                     
CAIMI                                                       1                    4                     0     5
Comadrona                                                   0                   34                     3    37
Hospital privado                                            3                  375                    30   408
Hospital público                                            7                 1040                    69  1116
Seguro social                                               1                  144                    14   159
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
servicio_asistencia_parto                                                                               
CAIMI                                                    20.0                 80.0                   0.0
Comadrona                                                 0.0                 91.9                   8.1
Hospital privado                                          0.7                 91.9                   7.4
Hospital público                                          0.6                 93.2                   6.2
Seguro social                                             0.6                 90.6                   8.8

**Estadísticos:**
- Chi-cuadrado: 29.550
- Valor p: 0.000
- Grados de libertad: 8

**Interpretación:**
La asociación entre servicio_asistencia_parto y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 29.550, p = 0.000).

**Análisis por categorías:**
- **CAIMI** muestra la mayor proporción de alto riesgo (20.0%)
- **Hospital público** muestra la mayor proporción de desarrollo adecuado (93.2%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
servicio_asistencia_parto                                                                                 
CAIMI                                                   0                    5                     0     5
Comadrona                                               0                   36                     1    37
Hospital privado                                        4                  368                    36   408
Hospital público                                       11                 1043                    62  1116
Seguro social                                           2                  148                     9   159
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
servicio_asistencia_parto                                                                           
CAIMI                                                 0.0                100.0                   0.0
Comadrona                                             0.0                 97.3                   2.7
Hospital privado                                      1.0                 90.2                   8.8
Hospital público                                      1.0                 93.5                   5.6
Seguro social                                         1.3                 93.1                   5.7

**Estadísticos:**
- Chi-cuadrado: 7.313
- Valor p: 0.503
- Grados de libertad: 8

**Interpretación:**
La asociación entre servicio_asistencia_parto y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.313, p = 0.503).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 33. ANÁLISIS DE LA VARIABLE: TIPO_PARTO

### Variable: tipo_parto
==================================================

**Distribución de la variable tipo_parto:**
- Parto eutócico: 1017 (59.0%)
- Cesárea electiva: 392 (22.7%)
- Cesárea de emergencia: 316 (18.3%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_parto                                                                                            
Cesárea de emergencia                               7                  295                    14   316
Cesárea electiva                                    3                  366                    23   392
Parto eutócico                                      4                  967                    46  1017
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_parto                                                                                      
Cesárea de emergencia                             2.2                 93.4                   4.4
Cesárea electiva                                  0.8                 93.4                   5.9
Parto eutócico                                    0.4                 95.1                   4.5

**Estadísticos:**
- Chi-cuadrado: 11.184
- Valor p: 0.025
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_parto y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.184, p = 0.025).

**Análisis por categorías:**
- **Cesárea de emergencia** muestra la mayor proporción de alto riesgo (2.2%)
- **Parto eutócico** muestra la mayor proporción de desarrollo adecuado (95.1%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_parto                                                                                                 
Cesárea de emergencia                                   16                  251                    49   316
Cesárea electiva                                        13                  327                    52   392
Parto eutócico                                          25                  859                   133  1017
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_parto                                                                                           
Cesárea de emergencia                                  5.1                 79.4                  15.5
Cesárea electiva                                       3.3                 83.4                  13.3
Parto eutócico                                         2.5                 84.5                  13.1

**Estadísticos:**
- Chi-cuadrado: 7.099
- Valor p: 0.131
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_parto y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.099, p = 0.131).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_parto                                                                                               
Cesárea de emergencia                                  2                  285                    29   316
Cesárea electiva                                       8                  362                    22   392
Parto eutócico                                        14                  930                    73  1017
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_parto                                                                                         
Cesárea de emergencia                                0.6                 90.2                   9.2
Cesárea electiva                                     2.0                 92.3                   5.6
Parto eutócico                                       1.4                 91.4                   7.2

**Estadísticos:**
- Chi-cuadrado: 5.679
- Valor p: 0.224
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_parto y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.679, p = 0.224).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_parto                                                                                                    
Cesárea de emergencia                                       4                  288                    24   316
Cesárea electiva                                            5                  364                    23   392
Parto eutócico                                              3                  945                    69  1017
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_parto                                                                                              
Cesárea de emergencia                                     1.3                 91.1                   7.6
Cesárea electiva                                          1.3                 92.9                   5.9
Parto eutócico                                            0.3                 92.9                   6.8

**Estadísticos:**
- Chi-cuadrado: 6.595
- Valor p: 0.159
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_parto y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 6.595, p = 0.159).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
tipo_parto                                                                                                
Cesárea de emergencia                                   6                  288                    22   316
Cesárea electiva                                        2                  368                    22   392
Parto eutócico                                          9                  944                    64  1017
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
tipo_parto                                                                                          
Cesárea de emergencia                                 1.9                 91.1                   7.0
Cesárea electiva                                      0.5                 93.9                   5.6
Parto eutócico                                        0.9                 92.8                   6.3

**Estadísticos:**
- Chi-cuadrado: 4.333
- Valor p: 0.363
- Grados de libertad: 4

**Interpretación:**
La asociación entre tipo_parto y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.333, p = 0.363).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 34. ANÁLISIS DE LA VARIABLE: RAZON_CESAREA_EMERGENCIA

### Variable: razon_cesarea_emergencia
==================================================

**Distribución de la variable razon_cesarea_emergencia:**
- Anhidramnios: 80 (4.6%)
- Sufrimiento fetal: 52 (3.0%)
- Anidramnios: 37 (2.1%)
- Preeclampsia: 23 (1.3%)
- Sufrimiento fetal : 12 (0.7%)
- Anhidramnios : 10 (0.6%)
- Preclampsia : 7 (0.4%)
- Oligohidramnios: 6 (0.3%)
- Sufrimiento fetal agudo: 6 (0.3%)
- Presentacion podalica: 6 (0.3%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_cesarea_emergencia                                                                             
ANHIDRAMNIOS                                        0                    2                     0    2
Ahnidramnios                                        0                    1                     0    1
Anhidramios                                         0                    1                     0    1
Anhidramnios                                        0                   76                     4   80
Anhidramnios                                        1                    8                     1   10
Anidramnios                                         0                   33                     4   37
Anihidramnios                                       0                    1                     0    1
Bradicardia fetal                                   0                    1                     0    1
Bradicardia fetal                                   0                    2                     0    2
Cardiopatia materna                                 0                    1                     1    2
Circular al cuello                                  0                    2                     0    2
Circular al cuello sufrimiento fetal                0                    1                     0    1
Cirugía previa                                      0                    1                     0    1
Desprendimiento placenta                            0                    1                     0    1
Detencion del parto                                 1                    0                     0    1
Detención de desenso                                0                    1                     0    1
Detención de dilatacion                             0                    1                     0    1
Detención de dilatación                             0                    2                     0    2
Detención de la dilatación.                         0                    1                     0    1
Detención del descenso                              0                    1                     0    1
Detención dilatación                                1                    1                     0    2
Disproporción cefalopélvica                         0                    1                     0    1
Distocia del parto                                  0                    4                     0    4
Embarazo gemelar                                    0                    1                     0    1
Embarazo gemelar                                    0                    1                     0    1
Embarazo post terminó                               0                    1                     0    1
Embarazo post término                               0                    1                     0    1
Fiebre materna                                      0                    1                     0    1
Hemorragia del tercer trimestre                     0                    1                     0    1
Indiccion fallida                                   0                    1                     0    1
Induccion fallida                                   0                    1                     0    1
Macrosomia                                          0                    1                     0    1
Macrosomia fetal                                    0                    2                     0    2
No TP                                               0                    0                     1    1
No descendio                                        0                    1                     0    1
No inicio de parto activo                           0                    1                     0    1
No razon clara                                      0                    1                     0    1
No tp                                               1                    2                     0    3
Oligohidramnios                                     0                    6                     0    6
Parto pre terminó                                   0                    1                     0    1
Placenta previa                                     0                    1                     0    1
Posicion podalica                                   0                    1                     0    1
Posición transversa                                 0                    1                     0    1
Preclampsia                                         1                    1                     0    2
Preclampsia                                         1                    6                     0    7
Preeclampsia                                        0                   21                     2   23
Preeclampsia                                        0                    4                     0    4
Prematurez                                          0                    1                     0    1
Presentacion podalica                               0                    6                     0    6
Presentación podálica                               0                    2                     0    2
Rmop                                                0                    1                     0    1
Roptura me membranas ovulares                       0                    1                     0    1
Roptura prematura de membranas ovulares             0                    1                     0    1
Ruptura prematura de membranas ovulares             0                    1                     0    1
Ruptura pretermino de membranas ovulares            0                    1                     0    1
Sospecha de corioamnioitis                          0                    1                     0    1
Sufrimiento fetal                                   0                   51                     1   52
Sufrimiento fetal                                   1                   11                     0   12
Sufrimiento fetal agudo                             0                    6                     0    6
Sufrimiento fetal circular al cuello                0                    2                     0    2
Sufrimiento fetal taquicardia fetal                 0                    1                     0    1
Sufrimiento fetal/ anhidramnios                     0                    1                     0    1
Taquicardia Fetal                                   0                    1                     0    1
Taquicardia fetal                                   0                    3                     0    3
Tinte meconial                                      0                    2                     0    2
Trabajo de parto pretermino                         0                    1                     0    1
All                                                 7                  295                    14  316

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_cesarea_emergencia                                                                        
ANHIDRAMNIOS                                      0.0                100.0                   0.0
Ahnidramnios                                      0.0                100.0                   0.0
Anhidramios                                       0.0                100.0                   0.0
Anhidramnios                                      0.0                 95.0                   5.0
Anhidramnios                                     10.0                 80.0                  10.0
Anidramnios                                       0.0                 89.2                  10.8
Anihidramnios                                     0.0                100.0                   0.0
Bradicardia fetal                                 0.0                100.0                   0.0
Bradicardia fetal                                 0.0                100.0                   0.0
Cardiopatia materna                               0.0                 50.0                  50.0
Circular al cuello                                0.0                100.0                   0.0
Circular al cuello sufrimiento fetal              0.0                100.0                   0.0
Cirugía previa                                    0.0                100.0                   0.0
Desprendimiento placenta                          0.0                100.0                   0.0
Detencion del parto                             100.0                  0.0                   0.0
Detención de desenso                              0.0                100.0                   0.0
Detención de dilatacion                           0.0                100.0                   0.0
Detención de dilatación                           0.0                100.0                   0.0
Detención de la dilatación.                       0.0                100.0                   0.0
Detención del descenso                            0.0                100.0                   0.0
Detención dilatación                             50.0                 50.0                   0.0
Disproporción cefalopélvica                       0.0                100.0                   0.0
Distocia del parto                                0.0                100.0                   0.0
Embarazo gemelar                                  0.0                100.0                   0.0
Embarazo gemelar                                  0.0                100.0                   0.0
Embarazo post terminó                             0.0                100.0                   0.0
Embarazo post término                             0.0                100.0                   0.0
Fiebre materna                                    0.0                100.0                   0.0
Hemorragia del tercer trimestre                   0.0                100.0                   0.0
Indiccion fallida                                 0.0                100.0                   0.0
Induccion fallida                                 0.0                100.0                   0.0
Macrosomia                                        0.0                100.0                   0.0
Macrosomia fetal                                  0.0                100.0                   0.0
No TP                                             0.0                  0.0                 100.0
No descendio                                      0.0                100.0                   0.0
No inicio de parto activo                         0.0                100.0                   0.0
No razon clara                                    0.0                100.0                   0.0
No tp                                            33.3                 66.7                   0.0
Oligohidramnios                                   0.0                100.0                   0.0
Parto pre terminó                                 0.0                100.0                   0.0
Placenta previa                                   0.0                100.0                   0.0
Posicion podalica                                 0.0                100.0                   0.0
Posición transversa                               0.0                100.0                   0.0
Preclampsia                                      50.0                 50.0                   0.0
Preclampsia                                      14.3                 85.7                   0.0
Preeclampsia                                      0.0                 91.3                   8.7
Preeclampsia                                      0.0                100.0                   0.0
Prematurez                                        0.0                100.0                   0.0
Presentacion podalica                             0.0                100.0                   0.0
Presentación podálica                             0.0                100.0                   0.0
Rmop                                              0.0                100.0                   0.0
Roptura me membranas ovulares                     0.0                100.0                   0.0
Roptura prematura de membranas ovulares           0.0                100.0                   0.0
Ruptura prematura de membranas ovulares           0.0                100.0                   0.0
Ruptura pretermino de membranas ovulares          0.0                100.0                   0.0
Sospecha de corioamnioitis                        0.0                100.0                   0.0
Sufrimiento fetal                                 0.0                 98.1                   1.9
Sufrimiento fetal                                 8.3                 91.7                   0.0
Sufrimiento fetal agudo                           0.0                100.0                   0.0
Sufrimiento fetal circular al cuello              0.0                100.0                   0.0
Sufrimiento fetal taquicardia fetal               0.0                100.0                   0.0
Sufrimiento fetal/ anhidramnios                   0.0                100.0                   0.0
Taquicardia Fetal                                 0.0                100.0                   0.0
Taquicardia fetal                                 0.0                100.0                   0.0
Tinte meconial                                    0.0                100.0                   0.0
Trabajo de parto pretermino                       0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 157.974
- Valor p: 0.048
- Grados de libertad: 130

**Interpretación:**
La asociación entre razon_cesarea_emergencia y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 157.974, p = 0.048).

**Análisis por categorías:**
- **Detencion del parto** muestra la mayor proporción de alto riesgo (100.0%)
- **ANHIDRAMNIOS ** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_cesarea_emergencia                                                                                  
ANHIDRAMNIOS                                             0                    1                     1    2
Ahnidramnios                                             0                    1                     0    1
Anhidramios                                              0                    1                     0    1
Anhidramnios                                             1                   67                    12   80
Anhidramnios                                             1                    8                     1   10
Anidramnios                                              1                   27                     9   37
Anihidramnios                                            1                    0                     0    1
Bradicardia fetal                                        0                    1                     0    1
Bradicardia fetal                                        0                    2                     0    2
Cardiopatia materna                                      0                    2                     0    2
Circular al cuello                                       1                    1                     0    2
Circular al cuello sufrimiento fetal                     0                    0                     1    1
Cirugía previa                                           0                    1                     0    1
Desprendimiento placenta                                 0                    1                     0    1
Detencion del parto                                      1                    0                     0    1
Detención de desenso                                     0                    1                     0    1
Detención de dilatacion                                  0                    1                     0    1
Detención de dilatación                                  1                    1                     0    2
Detención de la dilatación.                              0                    1                     0    1
Detención del descenso                                   0                    1                     0    1
Detención dilatación                                     0                    2                     0    2
Disproporción cefalopélvica                              0                    1                     0    1
Distocia del parto                                       0                    4                     0    4
Embarazo gemelar                                         0                    1                     0    1
Embarazo gemelar                                         0                    1                     0    1
Embarazo post terminó                                    0                    1                     0    1
Embarazo post término                                    0                    1                     0    1
Fiebre materna                                           0                    1                     0    1
Hemorragia del tercer trimestre                          0                    1                     0    1
Indiccion fallida                                        0                    1                     0    1
Induccion fallida                                        0                    1                     0    1
Macrosomia                                               0                    1                     0    1
Macrosomia fetal                                         0                    2                     0    2
No TP                                                    0                    1                     0    1
No descendio                                             1                    0                     0    1
No inicio de parto activo                                0                    1                     0    1
No razon clara                                           0                    1                     0    1
No tp                                                    1                    2                     0    3
Oligohidramnios                                          0                    3                     3    6
Parto pre terminó                                        0                    1                     0    1
Placenta previa                                          0                    1                     0    1
Posicion podalica                                        0                    1                     0    1
Posición transversa                                      0                    1                     0    1
Preclampsia                                              0                    1                     1    2
Preclampsia                                              0                    5                     2    7
Preeclampsia                                             2                   20                     1   23
Preeclampsia                                             0                    4                     0    4
Prematurez                                               0                    1                     0    1
Presentacion podalica                                    0                    5                     1    6
Presentación podálica                                    0                    1                     1    2
Rmop                                                     0                    1                     0    1
Roptura me membranas ovulares                            0                    1                     0    1
Roptura prematura de membranas ovulares                  0                    1                     0    1
Ruptura prematura de membranas ovulares                  1                    0                     0    1
Ruptura pretermino de membranas ovulares                 0                    1                     0    1
Sospecha de corioamnioitis                               0                    1                     0    1
Sufrimiento fetal                                        1                   38                    13   52
Sufrimiento fetal                                        2                    8                     2   12
Sufrimiento fetal agudo                                  1                    4                     1    6
Sufrimiento fetal circular al cuello                     0                    2                     0    2
Sufrimiento fetal taquicardia fetal                      0                    1                     0    1
Sufrimiento fetal/ anhidramnios                          0                    1                     0    1
Taquicardia Fetal                                        0                    1                     0    1
Taquicardia fetal                                        0                    3                     0    3
Tinte meconial                                           0                    2                     0    2
Trabajo de parto pretermino                              0                    1                     0    1
All                                                     16                  251                    49  316

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_cesarea_emergencia                                                                             
ANHIDRAMNIOS                                           0.0                 50.0                  50.0
Ahnidramnios                                           0.0                100.0                   0.0
Anhidramios                                            0.0                100.0                   0.0
Anhidramnios                                           1.2                 83.8                  15.0
Anhidramnios                                          10.0                 80.0                  10.0
Anidramnios                                            2.7                 73.0                  24.3
Anihidramnios                                        100.0                  0.0                   0.0
Bradicardia fetal                                      0.0                100.0                   0.0
Bradicardia fetal                                      0.0                100.0                   0.0
Cardiopatia materna                                    0.0                100.0                   0.0
Circular al cuello                                    50.0                 50.0                   0.0
Circular al cuello sufrimiento fetal                   0.0                  0.0                 100.0
Cirugía previa                                         0.0                100.0                   0.0
Desprendimiento placenta                               0.0                100.0                   0.0
Detencion del parto                                  100.0                  0.0                   0.0
Detención de desenso                                   0.0                100.0                   0.0
Detención de dilatacion                                0.0                100.0                   0.0
Detención de dilatación                               50.0                 50.0                   0.0
Detención de la dilatación.                            0.0                100.0                   0.0
Detención del descenso                                 0.0                100.0                   0.0
Detención dilatación                                   0.0                100.0                   0.0
Disproporción cefalopélvica                            0.0                100.0                   0.0
Distocia del parto                                     0.0                100.0                   0.0
Embarazo gemelar                                       0.0                100.0                   0.0
Embarazo gemelar                                       0.0                100.0                   0.0
Embarazo post terminó                                  0.0                100.0                   0.0
Embarazo post término                                  0.0                100.0                   0.0
Fiebre materna                                         0.0                100.0                   0.0
Hemorragia del tercer trimestre                        0.0                100.0                   0.0
Indiccion fallida                                      0.0                100.0                   0.0
Induccion fallida                                      0.0                100.0                   0.0
Macrosomia                                             0.0                100.0                   0.0
Macrosomia fetal                                       0.0                100.0                   0.0
No TP                                                  0.0                100.0                   0.0
No descendio                                         100.0                  0.0                   0.0
No inicio de parto activo                              0.0                100.0                   0.0
No razon clara                                         0.0                100.0                   0.0
No tp                                                 33.3                 66.7                   0.0
Oligohidramnios                                        0.0                 50.0                  50.0
Parto pre terminó                                      0.0                100.0                   0.0
Placenta previa                                        0.0                100.0                   0.0
Posicion podalica                                      0.0                100.0                   0.0
Posición transversa                                    0.0                100.0                   0.0
Preclampsia                                            0.0                 50.0                  50.0
Preclampsia                                            0.0                 71.4                  28.6
Preeclampsia                                           8.7                 87.0                   4.3
Preeclampsia                                           0.0                100.0                   0.0
Prematurez                                             0.0                100.0                   0.0
Presentacion podalica                                  0.0                 83.3                  16.7
Presentación podálica                                  0.0                 50.0                  50.0
Rmop                                                   0.0                100.0                   0.0
Roptura me membranas ovulares                          0.0                100.0                   0.0
Roptura prematura de membranas ovulares                0.0                100.0                   0.0
Ruptura prematura de membranas ovulares              100.0                  0.0                   0.0
Ruptura pretermino de membranas ovulares               0.0                100.0                   0.0
Sospecha de corioamnioitis                             0.0                100.0                   0.0
Sufrimiento fetal                                      1.9                 73.1                  25.0
Sufrimiento fetal                                     16.7                 66.7                  16.7
Sufrimiento fetal agudo                               16.7                 66.7                  16.7
Sufrimiento fetal circular al cuello                   0.0                100.0                   0.0
Sufrimiento fetal taquicardia fetal                    0.0                100.0                   0.0
Sufrimiento fetal/ anhidramnios                        0.0                100.0                   0.0
Taquicardia Fetal                                      0.0                100.0                   0.0
Taquicardia fetal                                      0.0                100.0                   0.0
Tinte meconial                                         0.0                100.0                   0.0
Trabajo de parto pretermino                            0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 148.338
- Valor p: 0.130
- Grados de libertad: 130

**Interpretación:**
La asociación entre razon_cesarea_emergencia y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 148.338, p = 0.130).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_cesarea_emergencia                                                                                
ANHIDRAMNIOS                                           0                    2                     0    2
Ahnidramnios                                           0                    0                     1    1
Anhidramios                                            0                    1                     0    1
Anhidramnios                                           0                   73                     7   80
Anhidramnios                                           1                    8                     1   10
Anidramnios                                            0                   33                     4   37
Anihidramnios                                          0                    1                     0    1
Bradicardia fetal                                      0                    1                     0    1
Bradicardia fetal                                      0                    1                     1    2
Cardiopatia materna                                    0                    2                     0    2
Circular al cuello                                     0                    2                     0    2
Circular al cuello sufrimiento fetal                   0                    1                     0    1
Cirugía previa                                         0                    1                     0    1
Desprendimiento placenta                               0                    1                     0    1
Detencion del parto                                    0                    1                     0    1
Detención de desenso                                   0                    1                     0    1
Detención de dilatacion                                0                    1                     0    1
Detención de dilatación                                0                    2                     0    2
Detención de la dilatación.                            0                    1                     0    1
Detención del descenso                                 0                    1                     0    1
Detención dilatación                                   0                    1                     1    2
Disproporción cefalopélvica                            0                    1                     0    1
Distocia del parto                                     0                    4                     0    4
Embarazo gemelar                                       0                    1                     0    1
Embarazo gemelar                                       0                    1                     0    1
Embarazo post terminó                                  0                    1                     0    1
Embarazo post término                                  0                    1                     0    1
Fiebre materna                                         0                    1                     0    1
Hemorragia del tercer trimestre                        0                    1                     0    1
Indiccion fallida                                      0                    1                     0    1
Induccion fallida                                      0                    1                     0    1
Macrosomia                                             0                    0                     1    1
Macrosomia fetal                                       0                    2                     0    2
No TP                                                  0                    1                     0    1
No descendio                                           0                    1                     0    1
No inicio de parto activo                              0                    1                     0    1
No razon clara                                         0                    1                     0    1
No tp                                                  1                    2                     0    3
Oligohidramnios                                        0                    6                     0    6
Parto pre terminó                                      0                    1                     0    1
Placenta previa                                        0                    1                     0    1
Posicion podalica                                      0                    1                     0    1
Posición transversa                                    0                    1                     0    1
Preclampsia                                            0                    1                     1    2
Preclampsia                                            0                    6                     1    7
Preeclampsia                                           0                   22                     1   23
Preeclampsia                                           0                    4                     0    4
Prematurez                                             0                    1                     0    1
Presentacion podalica                                  0                    6                     0    6
Presentación podálica                                  0                    2                     0    2
Rmop                                                   0                    1                     0    1
Roptura me membranas ovulares                          0                    1                     0    1
Roptura prematura de membranas ovulares                0                    1                     0    1
Ruptura prematura de membranas ovulares                0                    1                     0    1
Ruptura pretermino de membranas ovulares               0                    1                     0    1
Sospecha de corioamnioitis                             0                    1                     0    1
Sufrimiento fetal                                      0                   46                     6   52
Sufrimiento fetal                                      0                   12                     0   12
Sufrimiento fetal agudo                                0                    5                     1    6
Sufrimiento fetal circular al cuello                   0                    1                     1    2
Sufrimiento fetal taquicardia fetal                    0                    1                     0    1
Sufrimiento fetal/ anhidramnios                        0                    0                     1    1
Taquicardia Fetal                                      0                    1                     0    1
Taquicardia fetal                                      0                    2                     1    3
Tinte meconial                                         0                    2                     0    2
Trabajo de parto pretermino                            0                    1                     0    1
All                                                    2                  285                    29  316

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_cesarea_emergencia                                                                           
ANHIDRAMNIOS                                         0.0                100.0                   0.0
Ahnidramnios                                         0.0                  0.0                 100.0
Anhidramios                                          0.0                100.0                   0.0
Anhidramnios                                         0.0                 91.2                   8.8
Anhidramnios                                        10.0                 80.0                  10.0
Anidramnios                                          0.0                 89.2                  10.8
Anihidramnios                                        0.0                100.0                   0.0
Bradicardia fetal                                    0.0                100.0                   0.0
Bradicardia fetal                                    0.0                 50.0                  50.0
Cardiopatia materna                                  0.0                100.0                   0.0
Circular al cuello                                   0.0                100.0                   0.0
Circular al cuello sufrimiento fetal                 0.0                100.0                   0.0
Cirugía previa                                       0.0                100.0                   0.0
Desprendimiento placenta                             0.0                100.0                   0.0
Detencion del parto                                  0.0                100.0                   0.0
Detención de desenso                                 0.0                100.0                   0.0
Detención de dilatacion                              0.0                100.0                   0.0
Detención de dilatación                              0.0                100.0                   0.0
Detención de la dilatación.                          0.0                100.0                   0.0
Detención del descenso                               0.0                100.0                   0.0
Detención dilatación                                 0.0                 50.0                  50.0
Disproporción cefalopélvica                          0.0                100.0                   0.0
Distocia del parto                                   0.0                100.0                   0.0
Embarazo gemelar                                     0.0                100.0                   0.0
Embarazo gemelar                                     0.0                100.0                   0.0
Embarazo post terminó                                0.0                100.0                   0.0
Embarazo post término                                0.0                100.0                   0.0
Fiebre materna                                       0.0                100.0                   0.0
Hemorragia del tercer trimestre                      0.0                100.0                   0.0
Indiccion fallida                                    0.0                100.0                   0.0
Induccion fallida                                    0.0                100.0                   0.0
Macrosomia                                           0.0                  0.0                 100.0
Macrosomia fetal                                     0.0                100.0                   0.0
No TP                                                0.0                100.0                   0.0
No descendio                                         0.0                100.0                   0.0
No inicio de parto activo                            0.0                100.0                   0.0
No razon clara                                       0.0                100.0                   0.0
No tp                                               33.3                 66.7                   0.0
Oligohidramnios                                      0.0                100.0                   0.0
Parto pre terminó                                    0.0                100.0                   0.0
Placenta previa                                      0.0                100.0                   0.0
Posicion podalica                                    0.0                100.0                   0.0
Posición transversa                                  0.0                100.0                   0.0
Preclampsia                                          0.0                 50.0                  50.0
Preclampsia                                          0.0                 85.7                  14.3
Preeclampsia                                         0.0                 95.7                   4.3
Preeclampsia                                         0.0                100.0                   0.0
Prematurez                                           0.0                100.0                   0.0
Presentacion podalica                                0.0                100.0                   0.0
Presentación podálica                                0.0                100.0                   0.0
Rmop                                                 0.0                100.0                   0.0
Roptura me membranas ovulares                        0.0                100.0                   0.0
Roptura prematura de membranas ovulares              0.0                100.0                   0.0
Ruptura prematura de membranas ovulares              0.0                100.0                   0.0
Ruptura pretermino de membranas ovulares             0.0                100.0                   0.0
Sospecha de corioamnioitis                           0.0                100.0                   0.0
Sufrimiento fetal                                    0.0                 88.5                  11.5
Sufrimiento fetal                                    0.0                100.0                   0.0
Sufrimiento fetal agudo                              0.0                 83.3                  16.7
Sufrimiento fetal circular al cuello                 0.0                 50.0                  50.0
Sufrimiento fetal taquicardia fetal                  0.0                100.0                   0.0
Sufrimiento fetal/ anhidramnios                      0.0                  0.0                 100.0
Taquicardia Fetal                                    0.0                100.0                   0.0
Taquicardia fetal                                    0.0                 66.7                  33.3
Tinte meconial                                       0.0                100.0                   0.0
Trabajo de parto pretermino                          0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 125.120
- Valor p: 0.605
- Grados de libertad: 130

**Interpretación:**
La asociación entre razon_cesarea_emergencia y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 125.120, p = 0.605).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_cesarea_emergencia                                                                                     
ANHIDRAMNIOS                                                0                    1                     1    2
Ahnidramnios                                                0                    1                     0    1
Anhidramios                                                 0                    0                     1    1
Anhidramnios                                                0                   76                     4   80
Anhidramnios                                                1                    7                     2   10
Anidramnios                                                 0                   36                     1   37
Anihidramnios                                               0                    1                     0    1
Bradicardia fetal                                           0                    1                     0    1
Bradicardia fetal                                           0                    2                     0    2
Cardiopatia materna                                         0                    2                     0    2
Circular al cuello                                          0                    2                     0    2
Circular al cuello sufrimiento fetal                        0                    1                     0    1
Cirugía previa                                              0                    1                     0    1
Desprendimiento placenta                                    0                    1                     0    1
Detencion del parto                                         0                    1                     0    1
Detención de desenso                                        0                    1                     0    1
Detención de dilatacion                                     0                    1                     0    1
Detención de dilatación                                     0                    2                     0    2
Detención de la dilatación.                                 0                    1                     0    1
Detención del descenso                                      0                    1                     0    1
Detención dilatación                                        1                    1                     0    2
Disproporción cefalopélvica                                 0                    1                     0    1
Distocia del parto                                          0                    3                     1    4
Embarazo gemelar                                            0                    1                     0    1
Embarazo gemelar                                            0                    1                     0    1
Embarazo post terminó                                       0                    1                     0    1
Embarazo post término                                       0                    1                     0    1
Fiebre materna                                              0                    1                     0    1
Hemorragia del tercer trimestre                             0                    0                     1    1
Indiccion fallida                                           0                    1                     0    1
Induccion fallida                                           0                    1                     0    1
Macrosomia                                                  0                    1                     0    1
Macrosomia fetal                                            0                    2                     0    2
No TP                                                       0                    1                     0    1
No descendio                                                0                    1                     0    1
No inicio de parto activo                                   0                    1                     0    1
No razon clara                                              0                    0                     1    1
No tp                                                       1                    2                     0    3
Oligohidramnios                                             0                    5                     1    6
Parto pre terminó                                           0                    1                     0    1
Placenta previa                                             0                    1                     0    1
Posicion podalica                                           0                    1                     0    1
Posición transversa                                         0                    1                     0    1
Preclampsia                                                 0                    1                     1    2
Preclampsia                                                 1                    5                     1    7
Preeclampsia                                                0                   20                     3   23
Preeclampsia                                                0                    4                     0    4
Prematurez                                                  0                    1                     0    1
Presentacion podalica                                       0                    5                     1    6
Presentación podálica                                       0                    2                     0    2
Rmop                                                        0                    1                     0    1
Roptura me membranas ovulares                               0                    1                     0    1
Roptura prematura de membranas ovulares                     0                    1                     0    1
Ruptura prematura de membranas ovulares                     0                    1                     0    1
Ruptura pretermino de membranas ovulares                    0                    1                     0    1
Sospecha de corioamnioitis                                  0                    1                     0    1
Sufrimiento fetal                                           0                   48                     4   52
Sufrimiento fetal                                           0                   11                     1   12
Sufrimiento fetal agudo                                     0                    6                     0    6
Sufrimiento fetal circular al cuello                        0                    2                     0    2
Sufrimiento fetal taquicardia fetal                         0                    1                     0    1
Sufrimiento fetal/ anhidramnios                             0                    1                     0    1
Taquicardia Fetal                                           0                    1                     0    1
Taquicardia fetal                                           0                    3                     0    3
Tinte meconial                                              0                    2                     0    2
Trabajo de parto pretermino                                 0                    1                     0    1
All                                                         4                  288                    24  316

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_cesarea_emergencia                                                                                
ANHIDRAMNIOS                                              0.0                 50.0                  50.0
Ahnidramnios                                              0.0                100.0                   0.0
Anhidramios                                               0.0                  0.0                 100.0
Anhidramnios                                              0.0                 95.0                   5.0
Anhidramnios                                             10.0                 70.0                  20.0
Anidramnios                                               0.0                 97.3                   2.7
Anihidramnios                                             0.0                100.0                   0.0
Bradicardia fetal                                         0.0                100.0                   0.0
Bradicardia fetal                                         0.0                100.0                   0.0
Cardiopatia materna                                       0.0                100.0                   0.0
Circular al cuello                                        0.0                100.0                   0.0
Circular al cuello sufrimiento fetal                      0.0                100.0                   0.0
Cirugía previa                                            0.0                100.0                   0.0
Desprendimiento placenta                                  0.0                100.0                   0.0
Detencion del parto                                       0.0                100.0                   0.0
Detención de desenso                                      0.0                100.0                   0.0
Detención de dilatacion                                   0.0                100.0                   0.0
Detención de dilatación                                   0.0                100.0                   0.0
Detención de la dilatación.                               0.0                100.0                   0.0
Detención del descenso                                    0.0                100.0                   0.0
Detención dilatación                                     50.0                 50.0                   0.0
Disproporción cefalopélvica                               0.0                100.0                   0.0
Distocia del parto                                        0.0                 75.0                  25.0
Embarazo gemelar                                          0.0                100.0                   0.0
Embarazo gemelar                                          0.0                100.0                   0.0
Embarazo post terminó                                     0.0                100.0                   0.0
Embarazo post término                                     0.0                100.0                   0.0
Fiebre materna                                            0.0                100.0                   0.0
Hemorragia del tercer trimestre                           0.0                  0.0                 100.0
Indiccion fallida                                         0.0                100.0                   0.0
Induccion fallida                                         0.0                100.0                   0.0
Macrosomia                                                0.0                100.0                   0.0
Macrosomia fetal                                          0.0                100.0                   0.0
No TP                                                     0.0                100.0                   0.0
No descendio                                              0.0                100.0                   0.0
No inicio de parto activo                                 0.0                100.0                   0.0
No razon clara                                            0.0                  0.0                 100.0
No tp                                                    33.3                 66.7                   0.0
Oligohidramnios                                           0.0                 83.3                  16.7
Parto pre terminó                                         0.0                100.0                   0.0
Placenta previa                                           0.0                100.0                   0.0
Posicion podalica                                         0.0                100.0                   0.0
Posición transversa                                       0.0                100.0                   0.0
Preclampsia                                               0.0                 50.0                  50.0
Preclampsia                                              14.3                 71.4                  14.3
Preeclampsia                                              0.0                 87.0                  13.0
Preeclampsia                                              0.0                100.0                   0.0
Prematurez                                                0.0                100.0                   0.0
Presentacion podalica                                     0.0                 83.3                  16.7
Presentación podálica                                     0.0                100.0                   0.0
Rmop                                                      0.0                100.0                   0.0
Roptura me membranas ovulares                             0.0                100.0                   0.0
Roptura prematura de membranas ovulares                   0.0                100.0                   0.0
Ruptura prematura de membranas ovulares                   0.0                100.0                   0.0
Ruptura pretermino de membranas ovulares                  0.0                100.0                   0.0
Sospecha de corioamnioitis                                0.0                100.0                   0.0
Sufrimiento fetal                                         0.0                 92.3                   7.7
Sufrimiento fetal                                         0.0                 91.7                   8.3
Sufrimiento fetal agudo                                   0.0                100.0                   0.0
Sufrimiento fetal circular al cuello                      0.0                100.0                   0.0
Sufrimiento fetal taquicardia fetal                       0.0                100.0                   0.0
Sufrimiento fetal/ anhidramnios                           0.0                100.0                   0.0
Taquicardia Fetal                                         0.0                100.0                   0.0
Taquicardia fetal                                         0.0                100.0                   0.0
Tinte meconial                                            0.0                100.0                   0.0
Trabajo de parto pretermino                               0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 143.747
- Valor p: 0.193
- Grados de libertad: 130

**Interpretación:**
La asociación entre razon_cesarea_emergencia y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 143.747, p = 0.193).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_cesarea_emergencia                                                                                 
ANHIDRAMNIOS                                            0                    2                     0    2
Ahnidramnios                                            0                    1                     0    1
Anhidramios                                             0                    1                     0    1
Anhidramnios                                            0                   73                     7   80
Anhidramnios                                            1                    8                     1   10
Anidramnios                                             0                   33                     4   37
Anihidramnios                                           0                    1                     0    1
Bradicardia fetal                                       0                    1                     0    1
Bradicardia fetal                                       0                    2                     0    2
Cardiopatia materna                                     0                    2                     0    2
Circular al cuello                                      0                    2                     0    2
Circular al cuello sufrimiento fetal                    0                    1                     0    1
Cirugía previa                                          0                    1                     0    1
Desprendimiento placenta                                0                    1                     0    1
Detencion del parto                                     1                    0                     0    1
Detención de desenso                                    0                    1                     0    1
Detención de dilatacion                                 0                    1                     0    1
Detención de dilatación                                 0                    2                     0    2
Detención de la dilatación.                             0                    1                     0    1
Detención del descenso                                  0                    1                     0    1
Detención dilatación                                    0                    2                     0    2
Disproporción cefalopélvica                             0                    1                     0    1
Distocia del parto                                      0                    4                     0    4
Embarazo gemelar                                        0                    1                     0    1
Embarazo gemelar                                        0                    1                     0    1
Embarazo post terminó                                   0                    1                     0    1
Embarazo post término                                   0                    1                     0    1
Fiebre materna                                          0                    1                     0    1
Hemorragia del tercer trimestre                         0                    1                     0    1
Indiccion fallida                                       0                    1                     0    1
Induccion fallida                                       0                    1                     0    1
Macrosomia                                              0                    1                     0    1
Macrosomia fetal                                        0                    2                     0    2
No TP                                                   0                    1                     0    1
No descendio                                            0                    1                     0    1
No inicio de parto activo                               0                    0                     1    1
No razon clara                                          0                    1                     0    1
No tp                                                   0                    2                     1    3
Oligohidramnios                                         0                    6                     0    6
Parto pre terminó                                       0                    1                     0    1
Placenta previa                                         0                    1                     0    1
Posicion podalica                                       0                    1                     0    1
Posición transversa                                     0                    1                     0    1
Preclampsia                                             0                    2                     0    2
Preclampsia                                             0                    6                     1    7
Preeclampsia                                            1                   22                     0   23
Preeclampsia                                            0                    4                     0    4
Prematurez                                              0                    1                     0    1
Presentacion podalica                                   1                    5                     0    6
Presentación podálica                                   0                    2                     0    2
Rmop                                                    0                    1                     0    1
Roptura me membranas ovulares                           0                    1                     0    1
Roptura prematura de membranas ovulares                 0                    0                     1    1
Ruptura prematura de membranas ovulares                 0                    1                     0    1
Ruptura pretermino de membranas ovulares                0                    1                     0    1
Sospecha de corioamnioitis                              0                    1                     0    1
Sufrimiento fetal                                       1                   49                     2   52
Sufrimiento fetal                                       1                   10                     1   12
Sufrimiento fetal agudo                                 0                    5                     1    6
Sufrimiento fetal circular al cuello                    0                    1                     1    2
Sufrimiento fetal taquicardia fetal                     0                    1                     0    1
Sufrimiento fetal/ anhidramnios                         0                    1                     0    1
Taquicardia Fetal                                       0                    1                     0    1
Taquicardia fetal                                       0                    2                     1    3
Tinte meconial                                          0                    2                     0    2
Trabajo de parto pretermino                             0                    1                     0    1
All                                                     6                  288                    22  316

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_cesarea_emergencia                                                                            
ANHIDRAMNIOS                                          0.0                100.0                   0.0
Ahnidramnios                                          0.0                100.0                   0.0
Anhidramios                                           0.0                100.0                   0.0
Anhidramnios                                          0.0                 91.2                   8.8
Anhidramnios                                         10.0                 80.0                  10.0
Anidramnios                                           0.0                 89.2                  10.8
Anihidramnios                                         0.0                100.0                   0.0
Bradicardia fetal                                     0.0                100.0                   0.0
Bradicardia fetal                                     0.0                100.0                   0.0
Cardiopatia materna                                   0.0                100.0                   0.0
Circular al cuello                                    0.0                100.0                   0.0
Circular al cuello sufrimiento fetal                  0.0                100.0                   0.0
Cirugía previa                                        0.0                100.0                   0.0
Desprendimiento placenta                              0.0                100.0                   0.0
Detencion del parto                                 100.0                  0.0                   0.0
Detención de desenso                                  0.0                100.0                   0.0
Detención de dilatacion                               0.0                100.0                   0.0
Detención de dilatación                               0.0                100.0                   0.0
Detención de la dilatación.                           0.0                100.0                   0.0
Detención del descenso                                0.0                100.0                   0.0
Detención dilatación                                  0.0                100.0                   0.0
Disproporción cefalopélvica                           0.0                100.0                   0.0
Distocia del parto                                    0.0                100.0                   0.0
Embarazo gemelar                                      0.0                100.0                   0.0
Embarazo gemelar                                      0.0                100.0                   0.0
Embarazo post terminó                                 0.0                100.0                   0.0
Embarazo post término                                 0.0                100.0                   0.0
Fiebre materna                                        0.0                100.0                   0.0
Hemorragia del tercer trimestre                       0.0                100.0                   0.0
Indiccion fallida                                     0.0                100.0                   0.0
Induccion fallida                                     0.0                100.0                   0.0
Macrosomia                                            0.0                100.0                   0.0
Macrosomia fetal                                      0.0                100.0                   0.0
No TP                                                 0.0                100.0                   0.0
No descendio                                          0.0                100.0                   0.0
No inicio de parto activo                             0.0                  0.0                 100.0
No razon clara                                        0.0                100.0                   0.0
No tp                                                 0.0                 66.7                  33.3
Oligohidramnios                                       0.0                100.0                   0.0
Parto pre terminó                                     0.0                100.0                   0.0
Placenta previa                                       0.0                100.0                   0.0
Posicion podalica                                     0.0                100.0                   0.0
Posición transversa                                   0.0                100.0                   0.0
Preclampsia                                           0.0                100.0                   0.0
Preclampsia                                           0.0                 85.7                  14.3
Preeclampsia                                          4.3                 95.7                   0.0
Preeclampsia                                          0.0                100.0                   0.0
Prematurez                                            0.0                100.0                   0.0
Presentacion podalica                                16.7                 83.3                   0.0
Presentación podálica                                 0.0                100.0                   0.0
Rmop                                                  0.0                100.0                   0.0
Roptura me membranas ovulares                         0.0                100.0                   0.0
Roptura prematura de membranas ovulares               0.0                  0.0                 100.0
Ruptura prematura de membranas ovulares               0.0                100.0                   0.0
Ruptura pretermino de membranas ovulares              0.0                100.0                   0.0
Sospecha de corioamnioitis                            0.0                100.0                   0.0
Sufrimiento fetal                                     1.9                 94.2                   3.8
Sufrimiento fetal                                     8.3                 83.3                   8.3
Sufrimiento fetal agudo                               0.0                 83.3                  16.7
Sufrimiento fetal circular al cuello                  0.0                 50.0                  50.0
Sufrimiento fetal taquicardia fetal                   0.0                100.0                   0.0
Sufrimiento fetal/ anhidramnios                       0.0                100.0                   0.0
Taquicardia Fetal                                     0.0                100.0                   0.0
Taquicardia fetal                                     0.0                 66.7                  33.3
Tinte meconial                                        0.0                100.0                   0.0
Trabajo de parto pretermino                           0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 119.641
- Valor p: 0.732
- Grados de libertad: 130

**Interpretación:**
La asociación entre razon_cesarea_emergencia y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 119.641, p = 0.732).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 35. ANÁLISIS DE LA VARIABLE: LACTANCIA_PRIMEROS_6_MESES

### Variable: lactancia_primeros_6_meses
==================================================

**Distribución de la variable lactancia_primeros_6_meses:**
- Lactancia materna exclusiva: 1254 (72.7%)
- Mixta: 336 (19.5%)
- Fórmula infantil: 135 (7.8%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_primeros_6_meses                                                                            
Fórmula infantil                                    2                  124                     9   135
Lactancia materna exclusiva                         8                 1190                    56  1254
Mixta                                               4                  314                    18   336
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_primeros_6_meses                                                                      
Fórmula infantil                                  1.5                 91.9                   6.7
Lactancia materna exclusiva                       0.6                 94.9                   4.5
Mixta                                             1.2                 93.5                   5.4

**Estadísticos:**
- Chi-cuadrado: 3.449
- Valor p: 0.486
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_primeros_6_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.449, p = 0.486).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_primeros_6_meses                                                                                 
Fórmula infantil                                         3                  109                    23   135
Lactancia materna exclusiva                             42                 1044                   168  1254
Mixta                                                    9                  284                    43   336
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_primeros_6_meses                                                                           
Fórmula infantil                                       2.2                 80.7                  17.0
Lactancia materna exclusiva                            3.3                 83.3                  13.4
Mixta                                                  2.7                 84.5                  12.8

**Estadísticos:**
- Chi-cuadrado: 2.305
- Valor p: 0.680
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_primeros_6_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.305, p = 0.680).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_primeros_6_meses                                                                               
Fórmula infantil                                       2                  121                    12   135
Lactancia materna exclusiva                           20                 1149                    85  1254
Mixta                                                  2                  307                    27   336
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_primeros_6_meses                                                                         
Fórmula infantil                                     1.5                 89.6                   8.9
Lactancia materna exclusiva                          1.6                 91.6                   6.8
Mixta                                                0.6                 91.4                   8.0

**Estadísticos:**
- Chi-cuadrado: 3.137
- Valor p: 0.535
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_primeros_6_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.137, p = 0.535).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_primeros_6_meses                                                                                    
Fórmula infantil                                            1                  123                    11   135
Lactancia materna exclusiva                                 9                 1164                    81  1254
Mixta                                                       2                  310                    24   336
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_primeros_6_meses                                                                              
Fórmula infantil                                          0.7                 91.1                   8.1
Lactancia materna exclusiva                               0.7                 92.8                   6.5
Mixta                                                     0.6                 92.3                   7.1

**Estadísticos:**
- Chi-cuadrado: 0.730
- Valor p: 0.948
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_primeros_6_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.730, p = 0.948).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_primeros_6_meses                                                                                
Fórmula infantil                                        2                  125                     8   135
Lactancia materna exclusiva                            11                 1163                    80  1254
Mixta                                                   4                  312                    20   336
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_primeros_6_meses                                                                          
Fórmula infantil                                      1.5                 92.6                   5.9
Lactancia materna exclusiva                           0.9                 92.7                   6.4
Mixta                                                 1.2                 92.9                   6.0

**Estadísticos:**
- Chi-cuadrado: 0.734
- Valor p: 0.947
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_primeros_6_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.734, p = 0.947).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 36. ANÁLISIS DE LA VARIABLE: LACTANCIA_6-12_MESES

### Variable: lactancia_6-12_meses
==================================================

**Distribución de la variable lactancia_6-12_meses:**
- Lactancia materna exclusiva: 867 (50.3%)
- Mixta: 568 (32.9%)
- Fórmula infantil: 125 (7.2%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_6-12_meses                                                                                  
Fórmula infantil                                    1                  117                     7   125
Lactancia materna exclusiva                         2                  834                    31   867
Mixta                                               7                  529                    32   568
All                                                10                 1480                    70  1560

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_6-12_meses                                                                            
Fórmula infantil                                  0.8                 93.6                   5.6
Lactancia materna exclusiva                       0.2                 96.2                   3.6
Mixta                                             1.2                 93.1                   5.6

**Estadísticos:**
- Chi-cuadrado: 9.402
- Valor p: 0.052
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_6-12_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 9.402, p = 0.052).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_6-12_meses                                                                                       
Fórmula infantil                                         3                  105                    17   125
Lactancia materna exclusiva                             13                  741                   113   867
Mixta                                                   14                  475                    79   568
All                                                     30                 1321                   209  1560

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_6-12_meses                                                                                 
Fórmula infantil                                       2.4                 84.0                  13.6
Lactancia materna exclusiva                            1.5                 85.5                  13.0
Mixta                                                  2.5                 83.6                  13.9

**Estadísticos:**
- Chi-cuadrado: 2.169
- Valor p: 0.705
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_6-12_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.169, p = 0.705).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_6-12_meses                                                                                     
Fórmula infantil                                       2                  108                    15   125
Lactancia materna exclusiva                           12                  794                    61   867
Mixta                                                  6                  524                    38   568
All                                                   20                 1426                   114  1560

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_6-12_meses                                                                               
Fórmula infantil                                     1.6                 86.4                  12.0
Lactancia materna exclusiva                          1.4                 91.6                   7.0
Mixta                                                1.1                 92.3                   6.7

**Estadísticos:**
- Chi-cuadrado: 4.935
- Valor p: 0.294
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_6-12_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.935, p = 0.294).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_6-12_meses                                                                                          
Fórmula infantil                                            1                  117                     7   125
Lactancia materna exclusiva                                 4                  809                    54   867
Mixta                                                       4                  523                    41   568
All                                                         9                 1449                   102  1560

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_6-12_meses                                                                                    
Fórmula infantil                                          0.8                 93.6                   5.6
Lactancia materna exclusiva                               0.5                 93.3                   6.2
Mixta                                                     0.7                 92.1                   7.2

**Estadísticos:**
- Chi-cuadrado: 1.229
- Valor p: 0.873
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_6-12_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.229, p = 0.873).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_6-12_meses                                                                                      
Fórmula infantil                                        2                  118                     5   125
Lactancia materna exclusiva                             5                  803                    59   867
Mixta                                                   6                  531                    31   568
All                                                    13                 1452                    95  1560

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_6-12_meses                                                                                
Fórmula infantil                                      1.6                 94.4                   4.0
Lactancia materna exclusiva                           0.6                 92.6                   6.8
Mixta                                                 1.1                 93.5                   5.5

**Estadísticos:**
- Chi-cuadrado: 3.957
- Valor p: 0.412
- Grados de libertad: 4

**Interpretación:**
La asociación entre lactancia_6-12_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.957, p = 0.412).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 37. ANÁLISIS DE LA VARIABLE: LACTANCIA_12-24_MESES

### Variable: lactancia_12-24_meses
==================================================

**Distribución de la variable lactancia_12-24_meses:**
- Lactancia materna exclusiva: 609 (35.3%)
- Mixta: 547 (31.7%)
- Fórmula infantil: 101 (5.9%)
- Otro tipo de lactancia: 8 (0.5%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_12-24_meses                                                                                 
Fórmula infantil                                    1                   93                     7   101
Lactancia materna exclusiva                         1                  587                    21   609
Mixta                                               8                  501                    38   547
Otro tipo de lactancia                              0                    8                     0     8
All                                                10                 1189                    66  1265

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_12-24_meses                                                                           
Fórmula infantil                                  1.0                 92.1                   6.9
Lactancia materna exclusiva                       0.2                 96.4                   3.4
Mixta                                             1.5                 91.6                   6.9
Otro tipo de lactancia                            0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 14.814
- Valor p: 0.022
- Grados de libertad: 6

**Interpretación:**
La asociación entre lactancia_12-24_meses y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 14.814, p = 0.022).

**Análisis por categorías:**
- **Mixta** muestra la mayor proporción de alto riesgo (1.5%)
- **Otro tipo de lactancia** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_12-24_meses                                                                                      
Fórmula infantil                                         4                   82                    15   101
Lactancia materna exclusiva                              8                  514                    87   609
Mixta                                                   16                  445                    86   547
Otro tipo de lactancia                                   0                    8                     0     8
All                                                     28                 1049                   188  1265

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_12-24_meses                                                                                
Fórmula infantil                                       4.0                 81.2                  14.9
Lactancia materna exclusiva                            1.3                 84.4                  14.3
Mixta                                                  2.9                 81.4                  15.7
Otro tipo de lactancia                                 0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 7.287
- Valor p: 0.295
- Grados de libertad: 6

**Interpretación:**
La asociación entre lactancia_12-24_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.287, p = 0.295).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_12-24_meses                                                                                    
Fórmula infantil                                       1                   91                     9   101
Lactancia materna exclusiva                            7                  562                    40   609
Mixta                                                  7                  519                    21   547
Otro tipo de lactancia                                 0                    6                     2     8
All                                                   15                 1178                    72  1265

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_12-24_meses                                                                              
Fórmula infantil                                     1.0                 90.1                   8.9
Lactancia materna exclusiva                          1.1                 92.3                   6.6
Mixta                                                1.3                 94.9                   3.8
Otro tipo de lactancia                               0.0                 75.0                  25.0

**Estadísticos:**
- Chi-cuadrado: 11.983
- Valor p: 0.062
- Grados de libertad: 6

**Interpretación:**
La asociación entre lactancia_12-24_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 11.983, p = 0.062).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_12-24_meses                                                                                         
Fórmula infantil                                            1                   94                     6   101
Lactancia materna exclusiva                                 3                  576                    30   609
Mixta                                                       5                  503                    39   547
Otro tipo de lactancia                                      0                    7                     1     8
All                                                         9                 1180                    76  1265

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_12-24_meses                                                                                   
Fórmula infantil                                          1.0                 93.1                   5.9
Lactancia materna exclusiva                               0.5                 94.6                   4.9
Mixta                                                     0.9                 92.0                   7.1
Otro tipo de lactancia                                    0.0                 87.5                  12.5

**Estadísticos:**
- Chi-cuadrado: 4.029
- Valor p: 0.673
- Grados de libertad: 6

**Interpretación:**
La asociación entre lactancia_12-24_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.029, p = 0.673).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
lactancia_12-24_meses                                                                                     
Fórmula infantil                                        3                   95                     3   101
Lactancia materna exclusiva                             4                  563                    42   609
Mixta                                                   5                  509                    33   547
Otro tipo de lactancia                                  0                    8                     0     8
All                                                    12                 1175                    78  1265

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
lactancia_12-24_meses                                                                               
Fórmula infantil                                      3.0                 94.1                   3.0
Lactancia materna exclusiva                           0.7                 92.4                   6.9
Mixta                                                 0.9                 93.1                   6.0
Otro tipo de lactancia                                0.0                100.0                   0.0

**Estadísticos:**
- Chi-cuadrado: 7.763
- Valor p: 0.256
- Grados de libertad: 6

**Interpretación:**
La asociación entre lactancia_12-24_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.763, p = 0.256).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 38. ANÁLISIS DE LA VARIABLE: VITAMINA_A_6-12_MESES

### Variable: vitamina_a_6-12_meses
==================================================

**Distribución de la variable vitamina_a_6-12_meses:**
- VERDADERO: 1088 (63.1%)
- FALSO: 473 (27.4%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_6-12_meses                                                                                 
FALSO                                               4                  454                    15   473
VERDADERO                                           6                 1027                    55  1088
All                                                10                 1481                    70  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_6-12_meses                                                                           
FALSO                                             0.8                 96.0                   3.2
VERDADERO                                         0.6                 94.4                   5.1

**Estadísticos:**
- Chi-cuadrado: 3.142
- Valor p: 0.208
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_6-12_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.142, p = 0.208).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_6-12_meses                                                                                      
FALSO                                                   11                  398                    64   473
VERDADERO                                               19                  924                   145  1088
All                                                     30                 1322                   209  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_6-12_meses                                                                                
FALSO                                                  2.3                 84.1                  13.5
VERDADERO                                              1.7                 84.9                  13.3

**Estadísticos:**
- Chi-cuadrado: 0.610
- Valor p: 0.737
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_6-12_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.610, p = 0.737).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_6-12_meses                                                                                    
FALSO                                                  6                  431                    36   473
VERDADERO                                             14                  996                    78  1088
All                                                   20                 1427                   114  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_6-12_meses                                                                              
FALSO                                                1.3                 91.1                   7.6
VERDADERO                                            1.3                 91.5                   7.2

**Estadísticos:**
- Chi-cuadrado: 0.095
- Valor p: 0.953
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_6-12_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.095, p = 0.953).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_6-12_meses                                                                                         
FALSO                                                       4                  435                    34   473
VERDADERO                                                   5                 1015                    68  1088
All                                                         9                 1450                   102  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_6-12_meses                                                                                   
FALSO                                                     0.8                 92.0                   7.2
VERDADERO                                                 0.5                 93.3                   6.2

**Estadísticos:**
- Chi-cuadrado: 1.359
- Valor p: 0.507
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_6-12_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.359, p = 0.507).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_6-12_meses                                                                                     
FALSO                                                   6                  439                    28   473
VERDADERO                                               7                 1014                    67  1088
All                                                    13                 1453                    95  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_6-12_meses                                                                               
FALSO                                                 1.3                 92.8                   5.9
VERDADERO                                             0.6                 93.2                   6.2

**Estadísticos:**
- Chi-cuadrado: 1.583
- Valor p: 0.453
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_6-12_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.583, p = 0.453).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 39. ANÁLISIS DE LA VARIABLE: VITAMINA_A_12-18_MESES

### Variable: vitamina_a_12-18_meses
==================================================

**Distribución de la variable vitamina_a_12-18_meses:**
- VERDADERO: 731 (42.4%)
- FALSO: 536 (31.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_12-18_meses                                                                                
FALSO                                               6                  508                    22   536
VERDADERO                                           4                  683                    44   731
All                                                10                 1191                    66  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_12-18_meses                                                                          
FALSO                                             1.1                 94.8                   4.1
VERDADERO                                         0.5                 93.4                   6.0

**Estadísticos:**
- Chi-cuadrado: 3.519
- Valor p: 0.172
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_12-18_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.519, p = 0.172).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_12-18_meses                                                                                     
FALSO                                                   16                  445                    75   536
VERDADERO                                               12                  606                   113   731
All                                                     28                 1051                   188  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_12-18_meses                                                                               
FALSO                                                  3.0                 83.0                  14.0
VERDADERO                                              1.6                 82.9                  15.5

**Estadísticos:**
- Chi-cuadrado: 2.974
- Valor p: 0.226
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_12-18_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.974, p = 0.226).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_12-18_meses                                                                                   
FALSO                                                  8                  495                    33   536
VERDADERO                                              7                  685                    39   731
All                                                   15                 1180                    72  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_12-18_meses                                                                             
FALSO                                                1.5                 92.4                   6.2
VERDADERO                                            1.0                 93.7                   5.3

**Estadísticos:**
- Chi-cuadrado: 1.176
- Valor p: 0.555
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_12-18_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.176, p = 0.555).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_12-18_meses                                                                                        
FALSO                                                       7                  495                    34   536
VERDADERO                                                   2                  687                    42   731
All                                                         9                 1182                    76  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_12-18_meses                                                                                  
FALSO                                                     1.3                 92.4                   6.3
VERDADERO                                                 0.3                 94.0                   5.7

**Estadísticos:**
- Chi-cuadrado: 4.912
- Valor p: 0.086
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_12-18_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.912, p = 0.086).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_12-18_meses                                                                                    
FALSO                                                   5                  505                    26   536
VERDADERO                                               7                  672                    52   731
All                                                    12                 1177                    78  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_12-18_meses                                                                              
FALSO                                                 0.9                 94.2                   4.9
VERDADERO                                             1.0                 91.9                   7.1

**Estadísticos:**
- Chi-cuadrado: 2.748
- Valor p: 0.253
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_12-18_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.748, p = 0.253).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 40. ANÁLISIS DE LA VARIABLE: VITAMINA_A_18-24_MESES

### Variable: vitamina_a_18-24_meses
==================================================

**Distribución de la variable vitamina_a_18-24_meses:**
- VERDADERO: 554 (32.1%)
- FALSO: 473 (27.4%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_18-24_meses                                                                                
FALSO                                               7                  441                    25   473
VERDADERO                                           2                  512                    40   554
All                                                 9                  953                    65  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_18-24_meses                                                                          
FALSO                                             1.5                 93.2                   5.3
VERDADERO                                         0.4                 92.4                   7.2

**Estadísticos:**
- Chi-cuadrado: 5.173
- Valor p: 0.075
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_18-24_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.173, p = 0.075).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_18-24_meses                                                                                     
FALSO                                                   12                  389                    72   473
VERDADERO                                                9                  460                    85   554
All                                                     21                  849                   157  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_18-24_meses                                                                               
FALSO                                                  2.5                 82.2                  15.2
VERDADERO                                              1.6                 83.0                  15.3

**Estadísticos:**
- Chi-cuadrado: 1.061
- Valor p: 0.588
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_18-24_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.061, p = 0.588).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_18-24_meses                                                                                   
FALSO                                                  8                  429                    36   473
VERDADERO                                              4                  530                    20   554
All                                                   12                  959                    56  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_18-24_meses                                                                             
FALSO                                                1.7                 90.7                   7.6
VERDADERO                                            0.7                 95.7                   3.6

**Estadísticos:**
- Chi-cuadrado: 10.217
- Valor p: 0.006
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_18-24_meses y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.217, p = 0.006).

**Análisis por categorías:**
- **FALSO** muestra la mayor proporción de alto riesgo (1.7%)
- **VERDADERO** muestra la mayor proporción de desarrollo adecuado (95.7%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_18-24_meses                                                                                        
FALSO                                                       6                  438                    29   473
VERDADERO                                                   0                  518                    36   554
All                                                         6                  956                    65  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_18-24_meses                                                                                  
FALSO                                                     1.3                 92.6                   6.1
VERDADERO                                                 0.0                 93.5                   6.5

**Estadísticos:**
- Chi-cuadrado: 7.104
- Valor p: 0.029
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_18-24_meses y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.104, p = 0.029).

**Análisis por categorías:**
- **FALSO** muestra la mayor proporción de alto riesgo (1.3%)
- **VERDADERO** muestra la mayor proporción de desarrollo adecuado (93.5%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitamina_a_18-24_meses                                                                                    
FALSO                                                   7                  438                    28   473
VERDADERO                                               5                  505                    44   554
All                                                    12                  943                    72  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitamina_a_18-24_meses                                                                              
FALSO                                                 1.5                 92.6                   5.9
VERDADERO                                             0.9                 91.2                   7.9

**Estadísticos:**
- Chi-cuadrado: 2.275
- Valor p: 0.321
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitamina_a_18-24_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.275, p = 0.321).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 41. ANÁLISIS DE LA VARIABLE: VITAMINAS_MINERALES_6-12_MESES

### Variable: vitaminas_minerales_6-12_meses
==================================================

**Distribución de la variable vitaminas_minerales_6-12_meses:**
- VERDADERO: 1078 (62.5%)
- FALSO: 483 (28.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_6-12_meses                                                                        
FALSO                                               3                  461                    19   483
VERDADERO                                           7                 1020                    51  1078
All                                                10                 1481                    70  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_6-12_meses                                                                  
FALSO                                             0.6                 95.4                   3.9
VERDADERO                                         0.6                 94.6                   4.7

**Estadísticos:**
- Chi-cuadrado: 0.501
- Valor p: 0.778
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_6-12_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.501, p = 0.778).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_6-12_meses                                                                             
FALSO                                                   10                  407                    66   483
VERDADERO                                               20                  915                   143  1078
All                                                     30                 1322                   209  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_6-12_meses                                                                       
FALSO                                                  2.1                 84.3                  13.7
VERDADERO                                              1.9                 84.9                  13.3

**Estadísticos:**
- Chi-cuadrado: 0.135
- Valor p: 0.935
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_6-12_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.135, p = 0.935).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_6-12_meses                                                                           
FALSO                                                  5                  449                    29   483
VERDADERO                                             15                  978                    85  1078
All                                                   20                 1427                   114  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_6-12_meses                                                                     
FALSO                                                1.0                 93.0                   6.0
VERDADERO                                            1.4                 90.7                   7.9

**Estadísticos:**
- Chi-cuadrado: 2.129
- Valor p: 0.345
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_6-12_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.129, p = 0.345).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_6-12_meses                                                                                
FALSO                                                       3                  439                    41   483
VERDADERO                                                   6                 1011                    61  1078
All                                                         9                 1450                   102  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_6-12_meses                                                                          
FALSO                                                     0.6                 90.9                   8.5
VERDADERO                                                 0.6                 93.8                   5.7

**Estadísticos:**
- Chi-cuadrado: 4.413
- Valor p: 0.110
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_6-12_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.413, p = 0.110).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_6-12_meses                                                                            
FALSO                                                   5                  449                    29   483
VERDADERO                                               8                 1004                    66  1078
All                                                    13                 1453                    95  1561

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_6-12_meses                                                                      
FALSO                                                 1.0                 93.0                   6.0
VERDADERO                                             0.7                 93.1                   6.1

**Estadísticos:**
- Chi-cuadrado: 0.353
- Valor p: 0.838
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_6-12_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.353, p = 0.838).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 42. ANÁLISIS DE LA VARIABLE: VITAMINAS_MINERALES_12-18_MESES

### Variable: vitaminas_minerales_12-18_meses
==================================================

**Distribución de la variable vitaminas_minerales_12-18_meses:**
- VERDADERO: 769 (44.6%)
- FALSO: 498 (28.9%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_12-18_meses                                                                       
FALSO                                               6                  475                    17   498
VERDADERO                                           4                  716                    49   769
All                                                10                 1191                    66  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_12-18_meses                                                                 
FALSO                                             1.2                 95.4                   3.4
VERDADERO                                         0.5                 93.1                   6.4

**Estadísticos:**
- Chi-cuadrado: 7.039
- Valor p: 0.030
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_12-18_meses y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.039, p = 0.030).

**Análisis por categorías:**
- **FALSO** muestra la mayor proporción de alto riesgo (1.2%)
- **FALSO** muestra la mayor proporción de desarrollo adecuado (95.4%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_12-18_meses                                                                            
FALSO                                                   18                  394                    86   498
VERDADERO                                               10                  657                   102   769
All                                                     28                 1051                   188  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_12-18_meses                                                                      
FALSO                                                  3.6                 79.1                  17.3
VERDADERO                                              1.3                 85.4                  13.3

**Estadísticos:**
- Chi-cuadrado: 12.047
- Valor p: 0.002
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_12-18_meses y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.047, p = 0.002).

**Análisis por categorías:**
- **FALSO** muestra la mayor proporción de alto riesgo (3.6%)
- **VERDADERO** muestra la mayor proporción de desarrollo adecuado (85.4%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_12-18_meses                                                                          
FALSO                                                  6                  470                    22   498
VERDADERO                                              9                  710                    50   769
All                                                   15                 1180                    72  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_12-18_meses                                                                    
FALSO                                                1.2                 94.4                   4.4
VERDADERO                                            1.2                 92.3                   6.5

**Estadísticos:**
- Chi-cuadrado: 2.450
- Valor p: 0.294
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_12-18_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.450, p = 0.294).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_12-18_meses                                                                               
FALSO                                                       6                  461                    31   498
VERDADERO                                                   3                  721                    45   769
All                                                         9                 1182                    76  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_12-18_meses                                                                         
FALSO                                                     1.2                 92.6                   6.2
VERDADERO                                                 0.4                 93.8                   5.9

**Estadísticos:**
- Chi-cuadrado: 2.940
- Valor p: 0.230
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_12-18_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.940, p = 0.230).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_12-18_meses                                                                           
FALSO                                                   5                  461                    32   498
VERDADERO                                               7                  716                    46   769
All                                                    12                 1177                    78  1267

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_12-18_meses                                                                     
FALSO                                                 1.0                 92.6                   6.4
VERDADERO                                             0.9                 93.1                   6.0

**Estadísticos:**
- Chi-cuadrado: 0.134
- Valor p: 0.935
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_12-18_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.134, p = 0.935).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 43. ANÁLISIS DE LA VARIABLE: VITAMINAS_MINERALES_18-24_MESES

### Variable: vitaminas_minerales_18-24_meses
==================================================

**Distribución de la variable vitaminas_minerales_18-24_meses:**
- VERDADERO: 553 (32.1%)
- FALSO: 474 (27.5%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_18-24_meses                                                                       
FALSO                                               6                  442                    26   474
VERDADERO                                           3                  511                    39   553
All                                                 9                  953                    65  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_18-24_meses                                                                 
FALSO                                             1.3                 93.2                   5.5
VERDADERO                                         0.5                 92.4                   7.1

**Estadísticos:**
- Chi-cuadrado: 2.534
- Valor p: 0.282
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_18-24_meses y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.534, p = 0.282).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_18-24_meses                                                                            
FALSO                                                   13                  382                    79   474
VERDADERO                                                8                  467                    78   553
All                                                     21                  849                   157  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_18-24_meses                                                                      
FALSO                                                  2.7                 80.6                  16.7
VERDADERO                                              1.4                 84.4                  14.1

**Estadísticos:**
- Chi-cuadrado: 3.652
- Valor p: 0.161
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_18-24_meses y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.652, p = 0.161).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_18-24_meses                                                                          
FALSO                                                  7                  434                    33   474
VERDADERO                                              5                  525                    23   553
All                                                   12                  959                    56  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_18-24_meses                                                                    
FALSO                                                1.5                 91.6                   7.0
VERDADERO                                            0.9                 94.9                   4.2

**Estadísticos:**
- Chi-cuadrado: 4.705
- Valor p: 0.095
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_18-24_meses y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.705, p = 0.095).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_18-24_meses                                                                               
FALSO                                                       5                  435                    34   474
VERDADERO                                                   1                  521                    31   553
All                                                         6                  956                    65  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_18-24_meses                                                                         
FALSO                                                     1.1                 91.8                   7.2
VERDADERO                                                 0.2                 94.2                   5.6

**Estadísticos:**
- Chi-cuadrado: 4.491
- Valor p: 0.106
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_18-24_meses y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.491, p = 0.106).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vitaminas_minerales_18-24_meses                                                                           
FALSO                                                   6                  434                    34   474
VERDADERO                                               6                  509                    38   553
All                                                    12                  943                    72  1027

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vitaminas_minerales_18-24_meses                                                                     
FALSO                                                 1.3                 91.6                   7.2
VERDADERO                                             1.1                 92.0                   6.9

**Estadísticos:**
- Chi-cuadrado: 0.111
- Valor p: 0.946
- Grados de libertad: 2

**Interpretación:**
La asociación entre vitaminas_minerales_18-24_meses y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.111, p = 0.946).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 44. ANÁLISIS DE LA VARIABLE: RETARDO_CRECIMIENTO

### Variable: retardo_crecimiento
==================================================

**Distribución de la variable retardo_crecimiento:**
- No: 1533 (88.9%)
- Sí: 192 (11.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
retardo_crecimiento                                                                                   
No                                                 11                 1450                    72  1533
Sí                                                  3                  178                    11   192
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
retardo_crecimiento                                                                             
No                                                0.7                 94.6                   4.7
Sí                                                1.6                 92.7                   5.7

**Estadísticos:**
- Chi-cuadrado: 1.943
- Valor p: 0.379
- Grados de libertad: 2

**Interpretación:**
La asociación entre retardo_crecimiento y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.943, p = 0.379).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
retardo_crecimiento                                                                                        
No                                                      47                 1288                   198  1533
Sí                                                       7                  149                    36   192
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
retardo_crecimiento                                                                                  
No                                                     3.1                 84.0                  12.9
Sí                                                     3.6                 77.6                  18.8

**Estadísticos:**
- Chi-cuadrado: 5.307
- Valor p: 0.070
- Grados de libertad: 2

**Interpretación:**
La asociación entre retardo_crecimiento y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.307, p = 0.070).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
retardo_crecimiento                                                                                      
No                                                    16                 1409                   108  1533
Sí                                                     8                  168                    16   192
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
retardo_crecimiento                                                                                
No                                                   1.0                 91.9                   7.0
Sí                                                   4.2                 87.5                   8.3

**Estadísticos:**
- Chi-cuadrado: 12.718
- Valor p: 0.002
- Grados de libertad: 2

**Interpretación:**
La asociación entre retardo_crecimiento y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 12.718, p = 0.002).

**Análisis por categorías:**
- **Sí** muestra la mayor proporción de alto riesgo (4.2%)
- **No** muestra la mayor proporción de desarrollo adecuado (91.9%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
retardo_crecimiento                                                                                           
No                                                          8                 1422                   103  1533
Sí                                                          4                  175                    13   192
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
retardo_crecimiento                                                                                     
No                                                        0.5                 92.8                   6.7
Sí                                                        2.1                 91.1                   6.8

**Estadísticos:**
- Chi-cuadrado: 6.029
- Valor p: 0.049
- Grados de libertad: 2

**Interpretación:**
La asociación entre retardo_crecimiento y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 6.029, p = 0.049).

**Análisis por categorías:**
- **Sí** muestra la mayor proporción de alto riesgo (2.1%)
- **No** muestra la mayor proporción de desarrollo adecuado (92.8%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
retardo_crecimiento                                                                                       
No                                                     13                 1432                    88  1533
Sí                                                      4                  168                    20   192
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
retardo_crecimiento                                                                                 
No                                                    0.8                 93.4                   5.7
Sí                                                    2.1                 87.5                  10.4

**Estadísticos:**
- Chi-cuadrado: 9.245
- Valor p: 0.010
- Grados de libertad: 2

**Interpretación:**
La asociación entre retardo_crecimiento y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 9.245, p = 0.010).

**Análisis por categorías:**
- **Sí** muestra la mayor proporción de alto riesgo (2.1%)
- **No** muestra la mayor proporción de desarrollo adecuado (93.4%)

--------------------------------------------------------------------------------


## 45. ANÁLISIS DE LA VARIABLE: DESNUTRICION_AGUDA

### Variable: desnutricion_aguda
==================================================

**Distribución de la variable desnutricion_aguda:**
- No: 1623 (94.1%)
- Sí: 102 (5.9%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
desnutricion_aguda                                                                                    
No                                                 13                 1535                    75  1623
Sí                                                  1                   93                     8   102
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
desnutricion_aguda                                                                              
No                                                0.8                 94.6                   4.6
Sí                                                1.0                 91.2                   7.8

**Estadísticos:**
- Chi-cuadrado: 2.226
- Valor p: 0.329
- Grados de libertad: 2

**Interpretación:**
La asociación entre desnutricion_aguda y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.226, p = 0.329).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
desnutricion_aguda                                                                                         
No                                                      48                 1356                   219  1623
Sí                                                       6                   81                    15   102
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
desnutricion_aguda                                                                                   
No                                                     3.0                 83.5                  13.5
Sí                                                     5.9                 79.4                  14.7

**Estadísticos:**
- Chi-cuadrado: 2.924
- Valor p: 0.232
- Grados de libertad: 2

**Interpretación:**
La asociación entre desnutricion_aguda y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.924, p = 0.232).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
desnutricion_aguda                                                                                       
No                                                    20                 1487                   116  1623
Sí                                                     4                   90                     8   102
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
desnutricion_aguda                                                                                 
No                                                   1.2                 91.6                   7.1
Sí                                                   3.9                 88.2                   7.8

**Estadísticos:**
- Chi-cuadrado: 5.174
- Valor p: 0.075
- Grados de libertad: 2

**Interpretación:**
La asociación entre desnutricion_aguda y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 5.174, p = 0.075).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
desnutricion_aguda                                                                                            
No                                                         10                 1506                   107  1623
Sí                                                          2                   91                     9   102
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
desnutricion_aguda                                                                                      
No                                                        0.6                 92.8                   6.6
Sí                                                        2.0                 89.2                   8.8

**Estadísticos:**
- Chi-cuadrado: 3.337
- Valor p: 0.189
- Grados de libertad: 2

**Interpretación:**
La asociación entre desnutricion_aguda y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.337, p = 0.189).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
desnutricion_aguda                                                                                        
No                                                     13                 1511                    99  1623
Sí                                                      4                   89                     9   102
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
desnutricion_aguda                                                                                  
No                                                    0.8                 93.1                   6.1
Sí                                                    3.9                 87.3                   8.8

**Estadísticos:**
- Chi-cuadrado: 10.973
- Valor p: 0.004
- Grados de libertad: 2

**Interpretación:**
La asociación entre desnutricion_aguda y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.973, p = 0.004).

**Análisis por categorías:**
- **Sí** muestra la mayor proporción de alto riesgo (3.9%)
- **No** muestra la mayor proporción de desarrollo adecuado (93.1%)

--------------------------------------------------------------------------------


## 46. ANÁLISIS DE LA VARIABLE: HOSPITALIZADO_NEONATAL

### Variable: hospitalizado_neonatal
==================================================

**Distribución de la variable hospitalizado_neonatal:**
- No: 1518 (88.0%)
- Sí: 207 (12.0%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_neonatal                                                                                
No                                                 13                 1433                    72  1518
Sí                                                  1                  195                    11   207
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_neonatal                                                                          
No                                                0.9                 94.4                   4.7
Sí                                                0.5                 94.2                   5.3

**Estadísticos:**
- Chi-cuadrado: 0.437
- Valor p: 0.804
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_neonatal y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.437, p = 0.804).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_neonatal                                                                                     
No                                                      45                 1271                   202  1518
Sí                                                       9                  166                    32   207
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_neonatal                                                                               
No                                                     3.0                 83.7                  13.3
Sí                                                     4.3                 80.2                  15.5

**Estadísticos:**
- Chi-cuadrado: 2.009
- Valor p: 0.366
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_neonatal y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.009, p = 0.366).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_neonatal                                                                                   
No                                                    19                 1395                   104  1518
Sí                                                     5                  182                    20   207
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_neonatal                                                                             
No                                                   1.3                 91.9                   6.9
Sí                                                   2.4                 87.9                   9.7

**Estadísticos:**
- Chi-cuadrado: 4.090
- Valor p: 0.129
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_neonatal y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.090, p = 0.129).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_neonatal                                                                                        
No                                                         10                 1409                    99  1518
Sí                                                          2                  188                    17   207
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_neonatal                                                                                  
No                                                        0.7                 92.8                   6.5
Sí                                                        1.0                 90.8                   8.2

**Estadísticos:**
- Chi-cuadrado: 1.100
- Valor p: 0.577
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_neonatal y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.100, p = 0.577).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_neonatal                                                                                    
No                                                     15                 1414                    89  1518
Sí                                                      2                  186                    19   207
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_neonatal                                                                              
No                                                    1.0                 93.1                   5.9
Sí                                                    1.0                 89.9                   9.2

**Estadísticos:**
- Chi-cuadrado: 3.413
- Valor p: 0.182
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_neonatal y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.413, p = 0.182).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 47. ANÁLISIS DE LA VARIABLE: RAZON_HOSPITALIZADO_NEONATAL

### Variable: razon_hospitalizado_neonatal
==================================================

**Distribución de la variable razon_hospitalizado_neonatal:**
- Ictericia neonatal: 70 (4.1%)
- Prematuridad: 61 (3.5%)
- Taquipnea transitoria del recién nacido: 50 (2.9%)
- Neumonía: 9 (0.5%)
- Síndrome de aspiración meconial: 5 (0.3%)
- Sepsis: 3 (0.2%)
- Anomalías congénitas: 3 (0.2%)
- Asfixia perinatal: 2 (0.1%)
- Rotavirus: 1 (0.1%)
- Bajo peso: 1 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_neonatal                                                                         
Anomalías congénitas                                1                    2                     0    3
Asfixia perinatal                                   0                    1                     1    2
Bajo peso                                           0                    1                     0    1
Candidiasis bucal                                   0                    1                     0    1
Estenosis hipertrófica del píloro                   0                    0                     1    1
Ictericia neonatal                                  0                   68                     2   70
Neumonía                                            0                    8                     1    9
Prematuridad                                        0                   59                     2   61
Rotavirus                                           0                    1                     0    1
Sepsis                                              0                    3                     0    3
Síndrome de aspiración meconial                     0                    5                     0    5
Taquipnea transitoria del recién nacido             0                   46                     4   50
All                                                 1                  195                    11  207

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_neonatal                                                                    
Anomalías congénitas                             33.3                 66.7                   0.0
Asfixia perinatal                                 0.0                 50.0                  50.0
Bajo peso                                         0.0                100.0                   0.0
Candidiasis bucal                                 0.0                100.0                   0.0
Estenosis hipertrófica del píloro                 0.0                  0.0                 100.0
Ictericia neonatal                                0.0                 97.1                   2.9
Neumonía                                          0.0                 88.9                  11.1
Prematuridad                                      0.0                 96.7                   3.3
Rotavirus                                         0.0                100.0                   0.0
Sepsis                                            0.0                100.0                   0.0
Síndrome de aspiración meconial                   0.0                100.0                   0.0
Taquipnea transitoria del recién nacido           0.0                 92.0                   8.0

**Estadísticos:**
- Chi-cuadrado: 97.445
- Valor p: 0.000
- Grados de libertad: 22

**Interpretación:**
La asociación entre razon_hospitalizado_neonatal y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 97.445, p = 0.000).

**Análisis por categorías:**
- **Anomalías congénitas** muestra la mayor proporción de alto riesgo (33.3%)
- **Bajo peso** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_neonatal                                                                              
Anomalías congénitas                                     1                    2                     0    3
Asfixia perinatal                                        0                    2                     0    2
Bajo peso                                                0                    1                     0    1
Candidiasis bucal                                        0                    1                     0    1
Estenosis hipertrófica del píloro                        0                    1                     0    1
Ictericia neonatal                                       5                   55                    10   70
Neumonía                                                 0                    7                     2    9
Prematuridad                                             1                   52                     8   61
Rotavirus                                                1                    0                     0    1
Sepsis                                                   0                    3                     0    3
Síndrome de aspiración meconial                          0                    5                     0    5
Taquipnea transitoria del recién nacido                  1                   37                    12   50
All                                                      9                  166                    32  207

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_neonatal                                                                         
Anomalías congénitas                                  33.3                 66.7                   0.0
Asfixia perinatal                                      0.0                100.0                   0.0
Bajo peso                                              0.0                100.0                   0.0
Candidiasis bucal                                      0.0                100.0                   0.0
Estenosis hipertrófica del píloro                      0.0                100.0                   0.0
Ictericia neonatal                                     7.1                 78.6                  14.3
Neumonía                                               0.0                 77.8                  22.2
Prematuridad                                           1.6                 85.2                  13.1
Rotavirus                                            100.0                  0.0                   0.0
Sepsis                                                 0.0                100.0                   0.0
Síndrome de aspiración meconial                        0.0                100.0                   0.0
Taquipnea transitoria del recién nacido                2.0                 74.0                  24.0

**Estadísticos:**
- Chi-cuadrado: 38.220
- Valor p: 0.017
- Grados de libertad: 22

**Interpretación:**
La asociación entre razon_hospitalizado_neonatal y desarrollo de Motricidad Gruesa **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 38.220, p = 0.017).

**Análisis por categorías:**
- **Rotavirus** muestra la mayor proporción de alto riesgo (100.0%)
- **Asfixia perinatal** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_neonatal                                                                            
Anomalías congénitas                                   2                    1                     0    3
Asfixia perinatal                                      0                    2                     0    2
Bajo peso                                              0                    1                     0    1
Candidiasis bucal                                      0                    0                     1    1
Estenosis hipertrófica del píloro                      0                    1                     0    1
Ictericia neonatal                                     1                   65                     4   70
Neumonía                                               0                    8                     1    9
Prematuridad                                           2                   50                     9   61
Rotavirus                                              0                    1                     0    1
Sepsis                                                 0                    2                     1    3
Síndrome de aspiración meconial                        0                    5                     0    5
Taquipnea transitoria del recién nacido                0                   46                     4   50
All                                                    5                  182                    20  207

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_neonatal                                                                       
Anomalías congénitas                                66.7                 33.3                   0.0
Asfixia perinatal                                    0.0                100.0                   0.0
Bajo peso                                            0.0                100.0                   0.0
Candidiasis bucal                                    0.0                  0.0                 100.0
Estenosis hipertrófica del píloro                    0.0                100.0                   0.0
Ictericia neonatal                                   1.4                 92.9                   5.7
Neumonía                                             0.0                 88.9                  11.1
Prematuridad                                         3.3                 82.0                  14.8
Rotavirus                                            0.0                100.0                   0.0
Sepsis                                               0.0                 66.7                  33.3
Síndrome de aspiración meconial                      0.0                100.0                   0.0
Taquipnea transitoria del recién nacido              0.0                 92.0                   8.0

**Estadísticos:**
- Chi-cuadrado: 70.629
- Valor p: 0.000
- Grados de libertad: 22

**Interpretación:**
La asociación entre razon_hospitalizado_neonatal y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 70.629, p = 0.000).

**Análisis por categorías:**
- **Anomalías congénitas** muestra la mayor proporción de alto riesgo (66.7%)
- **Asfixia perinatal** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_neonatal                                                                                 
Anomalías congénitas                                        1                    2                     0    3
Asfixia perinatal                                           0                    2                     0    2
Bajo peso                                                   0                    1                     0    1
Candidiasis bucal                                           0                    1                     0    1
Estenosis hipertrófica del píloro                           0                    1                     0    1
Ictericia neonatal                                          1                   62                     7   70
Neumonía                                                    0                    7                     2    9
Prematuridad                                                0                   55                     6   61
Rotavirus                                                   0                    1                     0    1
Sepsis                                                      0                    3                     0    3
Síndrome de aspiración meconial                             0                    5                     0    5
Taquipnea transitoria del recién nacido                     0                   48                     2   50
All                                                         2                  188                    17  207

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_neonatal                                                                            
Anomalías congénitas                                     33.3                 66.7                   0.0
Asfixia perinatal                                         0.0                100.0                   0.0
Bajo peso                                                 0.0                100.0                   0.0
Candidiasis bucal                                         0.0                100.0                   0.0
Estenosis hipertrófica del píloro                         0.0                100.0                   0.0
Ictericia neonatal                                        1.4                 88.6                  10.0
Neumonía                                                  0.0                 77.8                  22.2
Prematuridad                                              0.0                 90.2                   9.8
Rotavirus                                                 0.0                100.0                   0.0
Sepsis                                                    0.0                100.0                   0.0
Síndrome de aspiración meconial                           0.0                100.0                   0.0
Taquipnea transitoria del recién nacido                   0.0                 96.0                   4.0

**Estadísticos:**
- Chi-cuadrado: 39.755
- Valor p: 0.012
- Grados de libertad: 22

**Interpretación:**
La asociación entre razon_hospitalizado_neonatal y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 39.755, p = 0.012).

**Análisis por categorías:**
- **Anomalías congénitas** muestra la mayor proporción de alto riesgo (33.3%)
- **Asfixia perinatal** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_neonatal                                                                             
Anomalías congénitas                                    0                    3                     0    3
Asfixia perinatal                                       0                    2                     0    2
Bajo peso                                               0                    1                     0    1
Candidiasis bucal                                       0                    1                     0    1
Estenosis hipertrófica del píloro                       0                    1                     0    1
Ictericia neonatal                                      2                   62                     6   70
Neumonía                                                0                    7                     2    9
Prematuridad                                            0                   55                     6   61
Rotavirus                                               0                    1                     0    1
Sepsis                                                  0                    3                     0    3
Síndrome de aspiración meconial                         0                    4                     1    5
Taquipnea transitoria del recién nacido                 0                   46                     4   50
All                                                     2                  186                    19  207

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_neonatal                                                                        
Anomalías congénitas                                  0.0                100.0                   0.0
Asfixia perinatal                                     0.0                100.0                   0.0
Bajo peso                                             0.0                100.0                   0.0
Candidiasis bucal                                     0.0                100.0                   0.0
Estenosis hipertrófica del píloro                     0.0                100.0                   0.0
Ictericia neonatal                                    2.9                 88.6                   8.6
Neumonía                                              0.0                 77.8                  22.2
Prematuridad                                          0.0                 90.2                   9.8
Rotavirus                                             0.0                100.0                   0.0
Sepsis                                                0.0                100.0                   0.0
Síndrome de aspiración meconial                       0.0                 80.0                  20.0
Taquipnea transitoria del recién nacido               0.0                 92.0                   8.0

**Estadísticos:**
- Chi-cuadrado: 7.831
- Valor p: 0.998
- Grados de libertad: 22

**Interpretación:**
La asociación entre razon_hospitalizado_neonatal y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 7.831, p = 0.998).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 48. ANÁLISIS DE LA VARIABLE: HOSPITALIZADO_INFANCIA

### Variable: hospitalizado_infancia
==================================================

**Distribución de la variable hospitalizado_infancia:**
- No: 1488 (86.3%)
- Sí: 237 (13.7%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_infancia                                                                                
No                                                 12                 1407                    69  1488
Sí                                                  2                  221                    14   237
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_infancia                                                                          
No                                                0.8                 94.6                   4.6
Sí                                                0.8                 93.2                   5.9

**Estadísticos:**
- Chi-cuadrado: 0.726
- Valor p: 0.696
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_infancia y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.726, p = 0.696).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_infancia                                                                                     
No                                                      45                 1249                   194  1488
Sí                                                       9                  188                    40   237
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_infancia                                                                               
No                                                     3.0                 83.9                  13.0
Sí                                                     3.8                 79.3                  16.9

**Estadísticos:**
- Chi-cuadrado: 3.135
- Valor p: 0.209
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_infancia y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 3.135, p = 0.209).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_infancia                                                                                   
No                                                    20                 1355                   113  1488
Sí                                                     4                  222                    11   237
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_infancia                                                                             
No                                                   1.3                 91.1                   7.6
Sí                                                   1.7                 93.7                   4.6

**Estadísticos:**
- Chi-cuadrado: 2.805
- Valor p: 0.246
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_infancia y desarrollo de Motricidad Fina **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.805, p = 0.246).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_infancia                                                                                        
No                                                         10                 1381                    97  1488
Sí                                                          2                  216                    19   237
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_infancia                                                                                  
No                                                        0.7                 92.8                   6.5
Sí                                                        0.8                 91.1                   8.0

**Estadísticos:**
- Chi-cuadrado: 0.831
- Valor p: 0.660
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_infancia y desarrollo de Resolución de Problemas **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 0.831, p = 0.660).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
hospitalizado_infancia                                                                                    
No                                                     13                 1385                    90  1488
Sí                                                      4                  215                    18   237
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
hospitalizado_infancia                                                                              
No                                                    0.9                 93.1                   6.0
Sí                                                    1.7                 90.7                   7.6

**Estadísticos:**
- Chi-cuadrado: 2.279
- Valor p: 0.320
- Grados de libertad: 2

**Interpretación:**
La asociación entre hospitalizado_infancia y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.279, p = 0.320).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------


## 49. ANÁLISIS DE LA VARIABLE: RAZON_HOSPITALIZADO_INFANCIA

### Variable: razon_hospitalizado_infancia
==================================================

**Distribución de la variable razon_hospitalizado_infancia:**
- Neumonía: 119 (6.9%)
- Síndrome diarreico agudo: 53 (3.1%)
- Bronquiolitis: 48 (2.8%)
- Fiebre de origen desconocido: 4 (0.2%)
- Intolerancia a la lactosa: 2 (0.1%)
- Hernioplastia: 2 (0.1%)
- Sepsis: 2 (0.1%)
- Apendicitis aguda: 2 (0.1%)
- Síndrome convulsivo: 1 (0.1%)
- Otitis media aguda: 1 (0.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_infancia                                                                         
Anemia                                              0                    1                     0    1
Apendicitis aguda                                   0                    2                     0    2
Bronquiolitis                                       0                   47                     1   48
Enfermedad renal no especificada                    0                    1                     0    1
Fiebre de origen desconocido                        0                    4                     0    4
Hernioplastia                                       0                    2                     0    2
Infeccion urinaria                                  0                    1                     0    1
Intolerancia a la lactosa                           0                    2                     0    2
Neumonía                                            1                  108                    10  119
Otitis media aguda                                  0                    1                     0    1
Sepsis                                              1                    0                     1    2
Síndrome convulsivo                                 0                    1                     0    1
Síndrome diarreico agudo                            0                   51                     2   53
All                                                 2                  221                    14  237

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_infancia                                                                    
Anemia                                            0.0                100.0                   0.0
Apendicitis aguda                                 0.0                100.0                   0.0
Bronquiolitis                                     0.0                 97.9                   2.1
Enfermedad renal no especificada                  0.0                100.0                   0.0
Fiebre de origen desconocido                      0.0                100.0                   0.0
Hernioplastia                                     0.0                100.0                   0.0
Infeccion urinaria                                0.0                100.0                   0.0
Intolerancia a la lactosa                         0.0                100.0                   0.0
Neumonía                                          0.8                 90.8                   8.4
Otitis media aguda                                0.0                100.0                   0.0
Sepsis                                           50.0                  0.0                  50.0
Síndrome convulsivo                               0.0                100.0                   0.0
Síndrome diarreico agudo                          0.0                 96.2                   3.8

**Estadísticos:**
- Chi-cuadrado: 70.746
- Valor p: 0.000
- Grados de libertad: 24

**Interpretación:**
La asociación entre razon_hospitalizado_infancia y desarrollo de Comunicación **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 70.746, p = 0.000).

**Análisis por categorías:**
- **Sepsis** muestra la mayor proporción de alto riesgo (50.0%)
- **Anemia** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_infancia                                                                              
Anemia                                                   0                    1                     0    1
Apendicitis aguda                                        0                    2                     0    2
Bronquiolitis                                            1                   41                     6   48
Enfermedad renal no especificada                         0                    1                     0    1
Fiebre de origen desconocido                             1                    3                     0    4
Hernioplastia                                            0                    2                     0    2
Infeccion urinaria                                       0                    1                     0    1
Intolerancia a la lactosa                                0                    2                     0    2
Neumonía                                                 5                   92                    22  119
Otitis media aguda                                       0                    1                     0    1
Sepsis                                                   1                    1                     0    2
Síndrome convulsivo                                      0                    1                     0    1
Síndrome diarreico agudo                                 1                   40                    12   53
All                                                      9                  188                    40  237

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_infancia                                                                         
Anemia                                                 0.0                100.0                   0.0
Apendicitis aguda                                      0.0                100.0                   0.0
Bronquiolitis                                          2.1                 85.4                  12.5
Enfermedad renal no especificada                       0.0                100.0                   0.0
Fiebre de origen desconocido                          25.0                 75.0                   0.0
Hernioplastia                                          0.0                100.0                   0.0
Infeccion urinaria                                     0.0                100.0                   0.0
Intolerancia a la lactosa                              0.0                100.0                   0.0
Neumonía                                               4.2                 77.3                  18.5
Otitis media aguda                                     0.0                100.0                   0.0
Sepsis                                                50.0                 50.0                   0.0
Síndrome convulsivo                                    0.0                100.0                   0.0
Síndrome diarreico agudo                               1.9                 75.5                  22.6

**Estadísticos:**
- Chi-cuadrado: 23.171
- Valor p: 0.510
- Grados de libertad: 24

**Interpretación:**
La asociación entre razon_hospitalizado_infancia y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 23.171, p = 0.510).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_infancia                                                                            
Anemia                                                 0                    1                     0    1
Apendicitis aguda                                      0                    2                     0    2
Bronquiolitis                                          0                   47                     1   48
Enfermedad renal no especificada                       0                    1                     0    1
Fiebre de origen desconocido                           1                    3                     0    4
Hernioplastia                                          0                    2                     0    2
Infeccion urinaria                                     0                    1                     0    1
Intolerancia a la lactosa                              0                    2                     0    2
Neumonía                                               2                  109                     8  119
Otitis media aguda                                     0                    1                     0    1
Sepsis                                                 1                    1                     0    2
Síndrome convulsivo                                    0                    1                     0    1
Síndrome diarreico agudo                               0                   51                     2   53
All                                                    4                  222                    11  237

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_infancia                                                                       
Anemia                                               0.0                100.0                   0.0
Apendicitis aguda                                    0.0                100.0                   0.0
Bronquiolitis                                        0.0                 97.9                   2.1
Enfermedad renal no especificada                     0.0                100.0                   0.0
Fiebre de origen desconocido                        25.0                 75.0                   0.0
Hernioplastia                                        0.0                100.0                   0.0
Infeccion urinaria                                   0.0                100.0                   0.0
Intolerancia a la lactosa                            0.0                100.0                   0.0
Neumonía                                             1.7                 91.6                   6.7
Otitis media aguda                                   0.0                100.0                   0.0
Sepsis                                              50.0                 50.0                   0.0
Síndrome convulsivo                                  0.0                100.0                   0.0
Síndrome diarreico agudo                             0.0                 96.2                   3.8

**Estadísticos:**
- Chi-cuadrado: 45.879
- Valor p: 0.005
- Grados de libertad: 24

**Interpretación:**
La asociación entre razon_hospitalizado_infancia y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 45.879, p = 0.005).

**Análisis por categorías:**
- **Sepsis** muestra la mayor proporción de alto riesgo (50.0%)
- **Anemia** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_infancia                                                                                 
Anemia                                                      0                    1                     0    1
Apendicitis aguda                                           0                    2                     0    2
Bronquiolitis                                               0                   47                     1   48
Enfermedad renal no especificada                            0                    1                     0    1
Fiebre de origen desconocido                                1                    3                     0    4
Hernioplastia                                               0                    2                     0    2
Infeccion urinaria                                          0                    1                     0    1
Intolerancia a la lactosa                                   0                    2                     0    2
Neumonía                                                    0                  106                    13  119
Otitis media aguda                                          0                    1                     0    1
Sepsis                                                      1                    0                     1    2
Síndrome convulsivo                                         0                    1                     0    1
Síndrome diarreico agudo                                    0                   49                     4   53
All                                                         2                  216                    19  237

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_infancia                                                                            
Anemia                                                    0.0                100.0                   0.0
Apendicitis aguda                                         0.0                100.0                   0.0
Bronquiolitis                                             0.0                 97.9                   2.1
Enfermedad renal no especificada                          0.0                100.0                   0.0
Fiebre de origen desconocido                             25.0                 75.0                   0.0
Hernioplastia                                             0.0                100.0                   0.0
Infeccion urinaria                                        0.0                100.0                   0.0
Intolerancia a la lactosa                                 0.0                100.0                   0.0
Neumonía                                                  0.0                 89.1                  10.9
Otitis media aguda                                        0.0                100.0                   0.0
Sepsis                                                   50.0                  0.0                  50.0
Síndrome convulsivo                                       0.0                100.0                   0.0
Síndrome diarreico agudo                                  0.0                 92.5                   7.5

**Estadísticos:**
- Chi-cuadrado: 98.191
- Valor p: 0.000
- Grados de libertad: 24

**Interpretación:**
La asociación entre razon_hospitalizado_infancia y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 98.191, p = 0.000).

**Análisis por categorías:**
- **Sepsis** muestra la mayor proporción de alto riesgo (50.0%)
- **Anemia** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos  All
razon_hospitalizado_infancia                                                                             
Anemia                                                  0                    1                     0    1
Apendicitis aguda                                       0                    2                     0    2
Bronquiolitis                                           0                   42                     6   48
Enfermedad renal no especificada                        0                    1                     0    1
Fiebre de origen desconocido                            0                    4                     0    4
Hernioplastia                                           0                    2                     0    2
Infeccion urinaria                                      0                    1                     0    1
Intolerancia a la lactosa                               0                    1                     1    2
Neumonía                                                3                  109                     7  119
Otitis media aguda                                      0                    1                     0    1
Sepsis                                                  1                    1                     0    2
Síndrome convulsivo                                     0                    1                     0    1
Síndrome diarreico agudo                                0                   49                     4   53
All                                                     4                  215                    18  237

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
razon_hospitalizado_infancia                                                                        
Anemia                                                0.0                100.0                   0.0
Apendicitis aguda                                     0.0                100.0                   0.0
Bronquiolitis                                         0.0                 87.5                  12.5
Enfermedad renal no especificada                      0.0                100.0                   0.0
Fiebre de origen desconocido                          0.0                100.0                   0.0
Hernioplastia                                         0.0                100.0                   0.0
Infeccion urinaria                                    0.0                100.0                   0.0
Intolerancia a la lactosa                             0.0                 50.0                  50.0
Neumonía                                              2.5                 91.6                   5.9
Otitis media aguda                                    0.0                100.0                   0.0
Sepsis                                               50.0                 50.0                   0.0
Síndrome convulsivo                                   0.0                100.0                   0.0
Síndrome diarreico agudo                              0.0                 92.5                   7.5

**Estadísticos:**
- Chi-cuadrado: 38.898
- Valor p: 0.028
- Grados de libertad: 24

**Interpretación:**
La asociación entre razon_hospitalizado_infancia y desarrollo de Desarrollo Socio-Individual **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 38.898, p = 0.028).

**Análisis por categorías:**
- **Sepsis** muestra la mayor proporción de alto riesgo (50.0%)
- **Anemia** muestra la mayor proporción de desarrollo adecuado (100.0%)

--------------------------------------------------------------------------------


## 50. ANÁLISIS DE LA VARIABLE: VACUNACION_COMPLETA

### Variable: vacunacion_completa
==================================================

**Distribución de la variable vacunacion_completa:**
- Sí: 1637 (94.9%)
- No: 88 (5.1%)

#### Comunicación

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vacunacion_completa                                                                                   
No                                                  2                   81                     5    88
Sí                                                 12                 1547                    78  1637
All                                                14                 1628                    83  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_comunicacion_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vacunacion_completa                                                                             
No                                                2.3                 92.0                   5.7
Sí                                                0.7                 94.5                   4.8

**Estadísticos:**
- Chi-cuadrado: 2.639
- Valor p: 0.267
- Grados de libertad: 2

**Interpretación:**
La asociación entre vacunacion_completa y desarrollo de Comunicación **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 2.639, p = 0.267).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Gruesa

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vacunacion_completa                                                                                        
No                                                       6                   72                    10    88
Sí                                                      48                 1365                   224  1637
All                                                     54                 1437                   234  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_gruesa_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vacunacion_completa                                                                                  
No                                                     6.8                 81.8                  11.4
Sí                                                     2.9                 83.4                  13.7

**Estadísticos:**
- Chi-cuadrado: 4.384
- Valor p: 0.112
- Grados de libertad: 2

**Interpretación:**
La asociación entre vacunacion_completa y desarrollo de Motricidad Gruesa **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 4.384, p = 0.112).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------

#### Motricidad Fina

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vacunacion_completa                                                                                      
No                                                     6                   75                     7    88
Sí                                                    18                 1502                   117  1637
All                                                   24                 1577                   124  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_motricidad_fina_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vacunacion_completa                                                                                
No                                                   6.8                 85.2                   8.0
Sí                                                   1.1                 91.8                   7.1

**Estadísticos:**
- Chi-cuadrado: 20.094
- Valor p: 0.000
- Grados de libertad: 2

**Interpretación:**
La asociación entre vacunacion_completa y desarrollo de Motricidad Fina **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 20.094, p = 0.000).

**Análisis por categorías:**
- **No** muestra la mayor proporción de alto riesgo (6.8%)
- **Sí** muestra la mayor proporción de desarrollo adecuado (91.8%)

--------------------------------------------------------------------------------

#### Resolución de Problemas

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vacunacion_completa                                                                                           
No                                                          3                   77                     8    88
Sí                                                          9                 1520                   108  1637
All                                                        12                 1597                   116  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_resolucion_problemas_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vacunacion_completa                                                                                     
No                                                        3.4                 87.5                   9.1
Sí                                                        0.5                 92.9                   6.6

**Estadísticos:**
- Chi-cuadrado: 10.845
- Valor p: 0.004
- Grados de libertad: 2

**Interpretación:**
La asociación entre vacunacion_completa y desarrollo de Resolución de Problemas **ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 10.845, p = 0.004).

**Análisis por categorías:**
- **No** muestra la mayor proporción de alto riesgo (3.4%)
- **Sí** muestra la mayor proporción de desarrollo adecuado (92.9%)

--------------------------------------------------------------------------------

#### Desarrollo Socio-Individual

**Tabla de Contingencia (Conteos absolutos):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos   All
vacunacion_completa                                                                                       
No                                                      2                   80                     6    88
Sí                                                     15                 1520                   102  1637
All                                                    17                 1600                   108  1725

**Tabla de Porcentajes (% por fila):**
zscore_desarrollo_socio_individual_categoria  Alto riesgo  Desarrollo adecuado  Riesgo de trastornos
vacunacion_completa                                                                                 
No                                                    2.3                 90.9                   6.8
Sí                                                    0.9                 92.9                   6.2

**Estadísticos:**
- Chi-cuadrado: 1.639
- Valor p: 0.441
- Grados de libertad: 2

**Interpretación:**
La asociación entre vacunacion_completa y desarrollo de Desarrollo Socio-Individual **NO ES ESTADÍSTICAMENTE SIGNIFICATIVA** (χ² = 1.639, p = 0.441).
No se puede concluir que exista una asociación significativa entre estas variables.

--------------------------------------------------------------------------------
