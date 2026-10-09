
import pandas as pd

print("=== RETO ABP: CONCEPTOS DE DATOS ===")
print("Hernandez Dylan 1245")

# 1. Crear datos de ejemplo
datos = {
    "id_paciente": [101, 102, 103, 104, 105],
    "edad": [25, 40, 35, 50, 29],
    "nivel_glucosa": [90, 130, 110, 150, 95],
    "presion_arterial": [115, 125, 120, 140, 118],
    "indice_masa_corporal": [22.5, 28.0, 25.5, 31.0, 23.0],
    "diagnostico_diabetes": [0, 1, 0, 1, 0]
}

# 2. Crear la tabla
df = pd.DataFrame(datos)

print("\n=== TABLA DE PACIENTES ===")
print(df)

# 3. Separar las variables de entrada X
X = df[[
    "edad",
    "nivel_glucosa",
    "presion_arterial",
    "indice_masa_corporal"
]]

# 4. Separar la variable objetivo y
y = df["diagnostico_diabetes"]

print("\n=== DATOS DE ENTRADA (X) ===")
print(X)

print("\n=== VARIABLE OBJETIVO (y) ===")
print(y)

# 5. Responder el reto
print("\n=== RESPUESTAS DEL ABP ===")
print("1. Target (y): diagnostico_diabetes")
print("2. Features (X): edad, nivel_glucosa,")
print("   presion_arterial e indice_masa_corporal")
print("3. Eliminar id_paciente porque solo identifica")
print("   al paciente y no describe su estado de salud.")

print("\nPrograma realizado por Hernandez Dylan 1245")