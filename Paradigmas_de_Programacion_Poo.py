# POO
import pandas as pd

class AnalizadorDeDatos:
    def __init__(self, dataframe):
        self.df = dataframe

    def filtrar_mayores(self):
        self.df = self.df[self.df['edad'] >= 18]

    def calcular_promedio_ingreso_usd(self):
        return self.df['ingreso_usd'].mean()

    def convertir_a_euros(self, tasa_cambio=0.9):
        self.df['ingreso_eur'] = self.df['ingreso_usd'] * tasa_cambio

    def mostrar_datos(self):
        print(self.df)

# Datos de entrada
data = {
    'nombre': ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta'],
    'edad': [22, 17, 35, 16, 29],
    'ingreso_usd': [2000, 1500, 2500, 1000, 3000]
}
df = pd.DataFrame(data)

# Crear objeto y analizar datos
analisis = AnalizadorDeDatos(df)
analisis.filtrar_mayores()
promedio = analisis.calcular_promedio_ingreso_usd()
analisis.convertir_a_euros()
analisis.mostrar_datos()

print("\nPromedio de ingresos en USD:", promedio)
