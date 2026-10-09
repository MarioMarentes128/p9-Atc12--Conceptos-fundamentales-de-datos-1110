import pandas as pd

# Crear un dataset de ejemplo
datos = {
    "id_paciente": [1, 2, 3, 4, 5],
    "edad": [25, 45, 30, 60, 50],
    "nivel_glucosa": [90, 180, 110, 200, 150],
    "presion_arterial": [120, 140, 115, 150, 135],
    "indice_masa_corporal": [22.5, 30.2, 24.0, 35.5, 28.0],
    "diagnostico_diabetes": [0, 1, 0, 1, 1]
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Mostrar el dataset
print("Dataset original:")
print(df)

# Identificar el Target (y)
y = df["diagnostico_diabetes"]

# Identificar las Features (X) y eliminar el ID
X = df.drop(columns=["id_paciente", "diagnostico_diabetes"])

# Mostrar los resultados
print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)