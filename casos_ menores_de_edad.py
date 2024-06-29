# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
datos=pd.read_csv("covid_19_colombia.csv")



df = datos.iloc[:, [0, 1, 4, 7, 9] ] #Columnas especificas
df.set_index("ID de caso", inplace=True) # indice de referencia
menor = df [df["Edad"]< 17 ] #filtro columna especifica con condiciones
orden_fecha = menor.sort_values(by= "fecha reporte web") #ordenar fechas
total_registros = len(orden_fecha) #recuento de regitros totales
conteo = orden_fecha["Sexo"].value_counts() #recuento tan de M como de F
porcentaje_sexo = (conteo / total_registros) * 100
orden_fecha= orden_fecha.replace("Santander","SANTANDER") 
conteo_region = orden_fecha["Nombre departamento"].value_counts() 
porcentaje_region = (conteo_region / total_registros) * 100


print("El % de cada region de casos de Covid-19  \n", porcentaje_region)
print(f"El numero de datos por sexo es: \n  {conteo}")
print("Y el % para cada uno de ellos es de: \n", round(porcentaje_sexo))