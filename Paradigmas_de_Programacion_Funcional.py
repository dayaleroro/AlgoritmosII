import pandas as pd

# Paso 1: Crear un DataFrame
data = {
    'nombre': ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta'],
    'edad': [22, 17, 35, 16, 29],
    'ingreso_usd': [2000, 1500, 2500, 1000, 3000]
}

df = pd.DataFrame(data)

# Paso 2: Filtrar personas mayores de edad (funcional: no usamos bucles)
mayores = df[df['edad'] >= 18]

# Paso 3: Calcular ingreso promedio
promedio_ingreso = mayores['ingreso_usd'].mean()

# Paso 4: Convertir ingreso a euros con map + lambda (funcional)
# Supongamos que 1 USD = 0.9 EUR
mayores['ingreso_eur'] = mayores['ingreso_usd'].map(lambda x: x * 0.9)

# Mostrar resultados
print("Mayores de edad:\n", mayores)
print("\nIngreso promedio (USD):", promedio_ingreso)

