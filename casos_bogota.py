# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:45:34 2024

@author: juanb
"""

import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("covid_19_colombia.csv")
datos.set_index("ID de caso", inplace=True)
filtro = datos.loc[(datos["Estado"] == "Fallecido") & (datos["Nombre municipio"] == "BOGOTA")]
columnas_mostrar = ["fecha reporte web", "Edad", "Sexo", "Estado", "Nombre municipio"]
df = filtro[columnas_mostrar]
df["fecha reporte web"] = pd.to_datetime(df["fecha reporte web"], format="%Y-%m-%d %H:%M:%S") #convertir a datatime
df["Año"] = df["fecha reporte web"].dt.year # Extraer el año de la fecha de reporte
conteo_por_año = df["Año"].value_counts().sort_index()# Contar los casos por año
print("Conteo de casos de COVID-19 por año:")
print(conteo_por_año)
plt.figure(figsize=(10, 6))
plt.bar(conteo_por_año.index, conteo_por_año.values, color='blue')
plt.xlabel('Año')
plt.ylabel('Número de Casos')
plt.title('Número de Casos de COVID-19 en Colombia por Año')
plt.xticks(conteo_por_año.index)
plt.grid(True)
plt.show()
