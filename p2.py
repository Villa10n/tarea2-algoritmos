import random

# [
#   [0: arreglo comunas adyacentes, 1: costo, 2: (2 instalado, 1 instalacion adyacente, 0 otro), 3: probabilidad]
# ]
vacunatorios = [
    [[0, 1, 2, 3], 60, 0, 0],
    [[1, 0, 2, 3], 30, 0, 0],
    [[2, 0, 1, 3, 4, 5], 60, 0, 0],
    [[3, 0, 1, 2, 4], 70, 0, 0],
    [[4, 2, 3, 5, 6, 7, 8], 130, 0, 0],
    [[5, 2, 4, 8], 50, 0, 0],
    [[6, 4, 7, 9, 10], 70, 0, 0],
    [[7, 4, 5, 6, 8, 9], 60, 0, 0],
    [[8, 4, 5, 7, 9, 10], 50, 0, 0],
    [[9, 6, 7, 8, 10], 80, 0, 0],
    [[10, 6, 8, 9], 40, 0, 0]
]

colocadosEn = []

def agregarProbabilidades(array, seed):
    random.seed(seed)
    for i in range(0, 11):
        array[i][3] = random.random()
    return array

def colocarVacunatorios(array):
    # Buscamos la mayor probabilidad en las comunas
    indiceMayorProbabilidad = 0
    mayorProbabilidad = 0
    for i in range(0, len(array)):
        if (array[i][3] > mayorProbabilidad):
            indiceMayorProbabilidad = i
            mayorProbabilidad = array[i][3]
    colocadosEn.append(array[indiceMayorProbabilidad][0][0])

    # Eliminar los elementos del arreglo
    arrayComunasAdyacentes = array[indiceMayorProbabilidad][0].copy()
    arrayComunasAdyacentes.sort()
    arrayComunasAdyacentes.reverse()
    indicesBorrar = []
    for i in arrayComunasAdyacentes:
        for j in range(0, len(array)):
            if (array[j][0][0] == i):
                indicesBorrar.append(j)
    for index in indicesBorrar:
        del array[index]
    
    # Retornar arreglo
    return array

def calcularFuncionObjetivo():
    print("funcion objetivo")

def verificarRestricciones():
    print("verificar restricciones")

# Programa
array1 = agregarProbabilidades(vacunatorios, 3)
for i in array1:
    print(i)
array2 = colocarVacunatorios(array1)
for i in array2:
    print(i)
array3 = colocarVacunatorios(array2)
for i in array3:
    print(i)
array4 = colocarVacunatorios(array3)
for i in array4:
    print(i)

print(colocadosEn)