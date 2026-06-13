# Programa para calcular la ruta más conveniente

# Entrada de datos
ruta1 = float(input("Ingrese la distancia de la primera ruta (en km): "))
ruta2 = float(input("Ingrese la distancia de la segunda ruta (en km): "))

# Procesamiento con operadores
# Usamos min() para encontrar la menor distancia
distancia_minima = min(ruta1, ruta2)

# Determinar cuál ruta corresponde
if distancia_minima == ruta1:
    ruta = "primera"
else:
    ruta = "segunda"

# Salida formateada con f-strings
print(f"La ruta más conveniente es la {ruta} con {distancia_minima:.2f} km")
