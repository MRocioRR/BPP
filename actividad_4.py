### Buenas Prácticas de programación con Python
### Alumna: María del Rocío Roldán de la Rosa
### 14/06/2023

### ACTIVIDAD LECCIÓN 4 - DEPURACIÓN Y REGLAS DE OPTIMIZACIÓN DE CÓDIGO ###

# 1. Haciendo uso de comprensión de listas realice un programa que, dado una lista de 
# listas de números enteros, devuelva el máximo de cada lista. Por ejemplo, suponga 
# la siguiente listas de listas:
# [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
# 
# El programa debe devolver el mayor elemento de cada sublista (señalado en negrita).
# 
# Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea donde ha 
# implementado la compresión de listas. Haga pruebas mostrando el contenido de las 
# variables y continuar con la ejecución línea a línea. ¿Qué conclusiones obtiene?
# 
# 2. Haga uso de la función filter para construir un programa que, dado una lista de 
# n números devuelva aquellos que son primos. Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], 
# el programa que implemente debe devolver como resultado [3, 5, 5, 13]

# Ejercicio 1:
## PARTE I
def obtener_maximos(lista):
    maximos = [max(sublista) for sublista in lista]
    return maximos

# Lista de listas de números enteros de ejemplo
lista_numeros = [[6, 8, 5], [9, 10, 11, 12, 13, 14, 15, 16], [200, 350, 86]]

resultados = obtener_maximos(lista_numeros)
print(resultados)

## PARTE II
# Utilizando pdb se realiza las pruebas de debugger

import pdb
# pdb.set_trace()

def obtener_maximos(lista):
    pdb.set_trace()  # Punto de parada
    maximos = [max(sublista) for sublista in lista]
    return maximos

### Lista de listas de números enteros de ejemplo
lista_numeros = [[6, 8, 5], [9, 10, 11, 12, 13, 14, 15, 16], [200, 350, 86]]

resultados = obtener_maximos(lista_numeros)
print(resultados)

# Ejercicio 2:
# Utilizaremos la función filter de Python junto con una función auxiliar
# para determinar si un número es primo. 

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Optimizado 

def es_primo(n):
    return False if n < 2 else all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


lista = [6, 8, 16, 10, 10, 44, 73]
primos = list(filter(es_primo, lista))

print(primos)