import time
import numpy as np
import pandas as pd
import scipy
import statsmodels

# cargando archivos csv
datos_df = pd.read_csv('CASEN_2017.csv', sep=';', encoding='latin-1')
#print(datos_df)

pd.options.display.max_rows=160

print(datos_df.info())


for col in datos_df.columns:
    print(col)
    print(datos_df[col].info())