
ciudad = ["Quito","Guayaquil","Cuenca"]
Quito = [
    [[14], [16], [15], [17], [18], [16], [15]],
    # semana 1
    [[15], [17], [16], [18], [19], [17], [16]],
    # semana 2
    [[16], [18], [17], [19], [20], [18], [17]],
     # semana 3
    [[17], [19], [18], [20], [21], [19], [18]],
     # semana 4
 ]
Guayaquil = [
    [[14], [16], [15], [17], [18], [16], [15]],
    # semana 1
    [[15], [17], [16], [28], [19], [17], [16]],
    # semana 2
    [[16], [18], [17], [19], [20], [10], [17]],
     # semana 3
    [[17], [19], [18], [20], [21], [39], [18]],
     # semana 4
]
Cuenca = [
    [[14], [16], [15], [17], [18], [16], [15]],
    # semana 1
    [[15], [17], [16], [18], [19], [17], [16]],
    # semana 2
    [[16], [18], [17], [75], [20], [18], [17]],
     # semana 3
    [[17], [19], [18], [20], [21], [19], [18]],
     # semana 4
]
matrices_ciudad = [Quito, Guayaquil, Cuenca]
def promedio_ciudad(matriz):
# Calcula el promedio de temperaturas para una ciudad a partir de una matriz de temperaturas semanales""""
# patrametros:
# Una lista de listas que contiene las temperaturas semanales cada sub lista representa representa una semana
# y contiene las temperaturas de cada día.
# retorna:
# El promedio de todas las temperaturas en la matriz.
    total_temp = 0
    contador= 0
    for semana in matriz:
        for dia in semana:
            total_temp += dia [0]
            contador += 1
    return total_temp / contador
ciudad_idx = 0
promedio = promedio_ciudad(matrices_ciudad[ciudad_idx])
print(f"el promedio de temperaturas en {ciudad[ciudad_idx]} es: {promedio:.2f}°c")






