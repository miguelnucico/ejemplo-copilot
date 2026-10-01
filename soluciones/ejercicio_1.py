''' 
PLANTEAMIENTO DEL EJERCICIO 1
calcular x
'''

#PROBLEMA: calcular x, con los valores a,b,c
# ENTRADAS: valor_a, valor_b, valor_c
# SALIDA: resultado_x

# ALGORITMO
# 1. Leer valor_a
# 2. Leer valor_b   
# 3. Leer valor_c
# 4. Calcular resultado_x
# 5. Mostrar resultado_x

#contrato de funciones
#leerDatos(): Lee los valores de entrada
#Entrada: ninguna
#Salida: valor_a, valor_b, valor_c
#responsabilidad: pedir datos al usuario

#calcularX(valor_a, valor_b, valor_c)
#Entrada: valor_a, valor_b, valor_c
#Salida: resultado_x
#responsabilidad: calcular x=((b-a**2)**1/2)/c ,no imprimir

#mostrarResultado(resultado_x)
#Entrada: resultado_x
#Salida: ninguna
#responsabilidad: imprimir el resultado

#casos de prueba
#caso 1: valor_a=2, valor_b=20, valor_c=5
#entrada: 2, 20, 5
#salida: 0.8

#caso 2: valor_a=3, valor_b=30, valor_c=6
#entrada: 3, 30, 6
#salida: 1.0

#caso 3: valor_a=4, valor_b=40, valor_c=8
#entrada: 4, 40, 8  
#salida: 1.2

# Restricciones:
# - no imprimir dentro de la funcion de calcularX
# - devolver el resultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realces llamadas a funciones dentro de la funcion de este archivo

def leerDatos():
    valor_a = float(input("Ingrese el valor de a: "))
    valor_b = float(input("Ingrese el valor de b: "))
    valor_c = float(input("Ingrese el valor de c: "))
    return valor_a, valor_b, valor_c

def calcularX(valor_a, valor_b, valor_c):
    resultado_x = ((valor_b - valor_a ** 2) ** 0.5) / valor_c
    return resultado_x

def mostrarResultado(resultado_x):
    print("El resultado de x es:", resultado_x)
