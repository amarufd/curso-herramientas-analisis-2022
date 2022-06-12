print("Cargando librerias...")
import time
import numpy as np
import pandas as pd

print("Cargando archivo...")

datos = pd.read_csv("data.csv")

print("Cargando archivo... OK")

print("\n\n\n%%%%%%%%%%%%%%%%%%%% Mostrando Datos %%%%%%%%%%%%%%%%%%%%%%")
for index, row in datos.iterrows():
    print('========================================')
    print("index: {} - row: \n{}".format(index, row))

print("\n\n\n%%%%%%%%%%%%%%%%%%%% Mostrando Información %%%%%%%%%%%%%%%%%%%%%%")
for col in datos.columns:
    print('========================================')
    print("col: {} - descripcion: \n{}".format(col, datos[col].info()))
