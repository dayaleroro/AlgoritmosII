import pandas as pd

# Paso 1: Crear el DataFrame
data = {
    'nombre': ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta'],
    'edad': [22, 17, 35, 16, 29],
    'ingreso_usd': [2000, 1500, 2500, 1000, 3000]
}

df = pd.DataFrame(data)

# Paso 2: Filtrar mayores de edad
mayores = df[df['edad'] >= 18]

# Paso 3: Calcular el promedio de ingreso en USD
suma_ingresos = 0
for ingreso in mayores['ingreso_usd']:
    suma_ingresos += ingreso

promedio = suma_ingresos / len(mayores)

# Paso 4: Crear una nueva columna con ingresos en euros
ingresos_eur = []
for ingreso in mayores['ingreso_usd']:
    ingresos_eur.append(ingreso * 0.9)

mayores['ingreso_eur'] = ingresos_eur

# Paso 5: Mostrar resultados
print("Mayores de edad:")
print(mayores)
print("\nPromedio de ingreso en USD:", promedio)