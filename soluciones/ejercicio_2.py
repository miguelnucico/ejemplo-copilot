''' 
PLANTEAMIENTO DEL EJERCICIO 2
calcular n
'''

#PROBLEMA: calcular n, con los valores n
# ENTRADAS: n
# SALIDA: n

# ALGORITMO
# 1. Leer n
# 4. Calcular n
# 5. Mostrar n

#contrato de funciones
#leerDatos(): Lee los valores de entrada
#Entrada: ninguna
#Salida: n
#responsabilidad: pedir datos al usuario

#calcularN(n)
#Entrada: n
#Salida: n
#responsabilidad: calcular, no imprimir math.sqrt(2 * math.pi) * math.e ** -n * n ** (n+1/2)

#mostrarResultado(n)
#Entrada: n
#Salida: ninguna
#responsabilidad: imprimir el resultado

#casos de prueba
#caso 1: n=5
#entrada: 5
#salida: 118.0191679575901

#caso 2: n=10
#entrada: 10    
#salida: 362.0342453221169      

#caso 3: n=15
#entrada: 15
#salida: 1037.626330640298

# Restricciones:
# - no imprimir dentro de la funcion de calcularX
# - devolver el resultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realces llamadas a funciones dentro de la funcion de este archivo

def leerDatos():
    n = float(input("Ingrese el valor de n: "))
    return n

def calcularN(n):
    resultado = math.sqrt(2 * math.pi) * math.e ** -n * n ** (n + 1/2)
    return resultado

def mostrarResultado(n):
    print("El resultado es:", n)
