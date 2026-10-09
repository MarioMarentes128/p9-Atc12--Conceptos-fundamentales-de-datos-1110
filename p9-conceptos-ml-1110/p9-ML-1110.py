import pandas as pd
print(pd.__version__) # Output: 1.5.2

# 29.
datos29 = {
    'distancia_km': [3.8, 2.0, 4.4, 1.9, 6.0],
    'trafico_nivel': [3, 1, 2, 3, 2],
    'edad_repartidor': [39, 28, 31, 45, 23],
    'tiempo_entrega_min': [36, 14, 33, 20, 52]
}


df = pd.DataFrame(datos29)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
