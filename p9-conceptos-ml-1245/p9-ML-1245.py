import pandas as pd

print("Version de Pandas:")
print(pd.__version__)

print("Hernandez Dylan 1245")


import pandas as pd

print("=== CONCEPTOS FUNDAMENTALES DE DATOS ===")
print("Hernandez Dylan 1245")

# 1. Crear los datos correspondientes al numero de lista
datos28 = {
    "distancia_km": [1.3, 4.1, 5.9, 2.6, 3.5],
    "trafico_nivel": [1, 2, 3, 1, 3],
    "edad_repartidor": [22, 37, 43, 29, 25],
    "tiempo_entrega_min": [10, 30, 55, 18, 33]
}

# 2. Crear la tabla
df = pd.DataFrame(datos28)

print("\n=== TABLA COMPLETA ===")
print(df)

# 3. Separar los datos de entrada X
X = df[[
    "distancia_km",
    "trafico_nivel",
    "edad_repartidor"
]]

# 4. Separar la variable objetivo y
y = df["tiempo_entrega_min"]

# 5. Mostrar las entradas
print("\n=== DATOS DE ENTRADA (X) ===")
print(X.head(2))

# 6. Mostrar la salida
print("\n=== VARIABLE OBJETIVO (y) ===")
print(y.head(2))

print("\nPrograma realizado por Hernandez Dylan 1245")