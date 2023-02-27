from tensorflow import keras
from keras import layers

# Definir la arquitectura de la red neuronal
model = keras.Sequential(
    [
        layers.Dense(8, input_shape=(4,), activation="relu"), # Capa oculta con 8 neuronas y función de activación ReLU
        layers.Dense(1, activation="linear"), # Capa de salida con 1 neurona y función de activación lineal
    ]
)

# Compilar el modelo
model.compile(loss="mean_squared_error", optimizer="adam")

# Generar datos aleatorios para las 4 entradas y la salida igual a la cuarta entrada
X=[ [20, 18.5, 120,5], [82, 29.8, 143, 1.8], [2, 22.8, 119, 4.1], [85, 17.7, 115, 2.1], [12, 44.5, 144, 1.1], [57, 34.4, 136, 4.7],
    [78, 44.6, 141, 3.7], [64, 36.1, 127, 3.1], [35, 45.4, 148, 2.5], [47, 20.6, 144, 2.4],[15, 20.2, 124, 3.8],
    [80, 15.5, 135, 3.0], [35, 25.4, 120, 1.4], [1, 17.5, 128, 3], [40, 30, 140, 5.0], [80, 24.7, 123, 2.4],
    [51, 25.8, 125, 2.7], [45, 16.0, 140, 4.5], [6, 41.4, 145, 3.5], [0, 37.6, 143, 1.5], [23, 37.8, 128, 2.7],
    [52, 43.4, 150, 4.3], [64, 42.6, 128, 2.5], [10, 38.5, 120, 2.6], [79, 17.0, 134, 3.5], [22, 21.7, 137, 3.0],
    [42, 25.2, 140, 3.0], [69, 33.8, 143, 5.0], [49, 35.0, 128, 4.9], [19, 36.2, 132, 3.0], [8, 19.0, 136, 4.0],
    [76, 15.6, 134, 3.4], [39, 18.1, 122, 4.4], [4, 42.8, 139, 2.3], [60, 39.0, 118, 2.6], [36, 28.2, 122, 2.2],
    [27, 18.2, 129, 2.3], [52, 38.3, 117, 1.2], [6, 34.3, 128, 2.3], [54, 30.9, 150, 3.7], [84, 42.5, 136, 3.6],
    [17, 19.6, 134, 3.5], [20, 35.4, 145, 4.0], [56, 37.5, 133, 2.3], [67, 44.6, 113, 2.1], [14, 37.5, 139, 2.0],
    [52, 44.4, 150, 3.4], [52, 17.8, 148, 4.1], [68, 36.4, 120, 3.1], [36, 44.1, 138, 4.1], [88, 35.2, 125, 2.2],
    [15, 32.4, 133, 1.6], [90, 35.3, 144, 2.9], [67, 15.6, 141, 1.9], [54, 18.1, 142, 3.3], [43, 29.8, 128, 2.3],
    [25, 22.6, 125, 2.1], [76, 38.0, 127, 4.3], [85, 35.8, 143, 4.1], [52, 24.9, 116, 4.1], [41, 33.4, 110, 3.6],
    [30, 39.2, 142, 1.6], [86, 41.6, 143, 2.0], [49, 29.2, 121, 3.3], [64, 21.2, 144, 2.6], [64, 21.9, 116, 2.7],
    [41, 16.7, 143, 3.7], [86, 42.8, 149, 2.0], [74, 35.2, 127, 3.0], [65, 38.0, 131, 2.3], [82, 20.0, 141, 1.4],
    [6, 23.1, 134, 1.2], [68, 25.3, 139, 4.4], [68, 28.9, 150, 1.9], [81, 35.9, 131, 3.0], [13, 27.6, 112, 4.3],
    [21, 42.6, 121, 1.2], [68, 37.5, 149, 1.7], [16, 28.2, 131, 1.4], [85, 33.6, 120, 2.3], [68, 21.3, 111, 4.2], 
    [62, 19.1, 125, 4.8], [43, 32.4, 115, 2.8], [25, 27.2, 138, 1.4], [19, 28.2, 129, 3.4], [54, 35.3, 136, 3.6], 
    [32, 28.1, 150, 2.1], [28, 19.4, 138, 2.4], [77, 18.8, 119, 4.4], [47, 19.9, 132, 1.5], [84, 38.0, 144, 4.6], 
    [25, 42.2, 113, 4.5], [18, 36.1, 110, 3.5], [34, 32.2, 147, 3.7], [52, 26.7, 141, 3.2], [78, 28.7, 140, 2.2], 
    [69, 27.7, 135, 1.2], [36, 44.8, 143, 3.0], [73, 16.6, 148, 2.9], [18, 39.3, 123, 2.7], [41, 40.0, 110, 2.8], 
    [64, 27.6, 136, 1.2], [89, 33.0, 111, 2.5], [52, 34.4, 136, 4.5], [6, 25.3, 128, 4.1]]

Y=[5, 1, 4, 2, 1, 4,
    3, 3, 2, 2, 3,
    3, 1, 3, 5, 2,
    2, 4, 3, 1, 2,
    4, 2, 2, 3, 4,
    3, 4, 2, 3, 3,
    3, 4, 2, 2, 2,
    2, 1, 2, 3, 3, 
    3, 4 , 2, 2, 2, 
    3, 4, 3, 4, 2, 
    1, 2, 1, 3, 2, 
    2, 4, 4, 4, 3,
    1, 2, 3, 2, 2,
    3, 2, 3, 2, 1,
    1, 4, 1, 3, 4, 
    1, 1, 1, 2, 4, 
    4, 2, 1, 3, 3,
    2, 2, 3, 1, 3,
    4, 3, 3, 3, 2, 
    1, 3, 2, 3, 2,
    1, 2, 4, 4] # 1,2,3,4,5 puede salir


# Entrenar el modelo
model.fit(X, Y, epochs=1000, batch_size=32, verbose=False)

item = [80, 20.5, 180, 5]
resultado= model.predict([item])
model.save('modelo_completo.h5')

print(f'La predicción es {resultado}')


