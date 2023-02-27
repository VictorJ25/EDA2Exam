import tensorflow as tf

# Definir la arquitectura de la red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

X = [34, 45, 38, 35, 36, 
     31, 33, 34, 45, 32, 
     30, 44, 44, 45, 34, 
     30, 37, 34, 40, 41, 
     44, 41, 32, 36, 43, 
     34, 43, 40, 41, 42, 
     39, 32, 42, 35, 30, 
     38, 38, 43, 31, 40, 
     40, 32, 39, 41, 31, 
     43, 34, 41, 36, 43]

Y = [20, 10, 10, 20, 20, 
     20, 20, 20, 10, 20, 
     20, 10, 10, 10, 20, 
     20, 10, 20, 10, 10, 
     10, 10, 20, 20, 10, 
     20, 10, 10, 10, 10, 
     10, 20, 10, 20, 20, 
     10, 10, 10, 20, 10, 
     10, 20, 10, 10, 20, 
     10, 20, 10, 20, 10]

modelo.fit(X, Y, epochs=500, verbose=False)

item = [47]
resultado= modelo.predict([item])
modelo.save('modelo_completo.h6')

print(f'La predicción es {resultado}')