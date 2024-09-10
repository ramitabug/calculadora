# Ejercitación Clase 3 (Funciones)
# 1.Crear una función que reciba dos números y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error.
# primer numero contador segundo numero acumulador

def operacion(num_uno: int, num_dos: int) -> int:

    suma = num_uno + num_dos
    promedio = suma / 2
    
    return promedio

resultado = operacion(5,10)
print(f"El promedio de los dos numeros es: {resultado}")


# 2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
# def calcular_area_rectangulo(base:float, altura:float) -> float:
#     '''
#     La funcion se encarga de calcular el area de un rectangulo.
#     Va a recibir como parametro, su base y su altura.
#     Va a retornar el area.
#     '''
#     area = (base*altura)
#     return area 

# resultado = calcular_area_rectangulo(5,8)
# print(resultado)

# 3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar.
# def verificar_numero_par(numero:int) -> int:
#     '''
#     Verificando si el numero es par.
#     '''
#     return numero % 2 == 0

# print(verificar_numero_par(2))


# 4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es.

# 5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.

# 6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.

# 7. Crear una función qué se encargue de dividir dos números, la misma debe recibir como parámetro dos números y retornar el resultado. Validar división por cero.

# 8. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.

# TAREA. 

# Realizar una función que me permita sumar dos números de las cuatro maneras siguientes.

# Una función sumar1 que reciba dos números y retorne el resultado
# Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)
# Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado
# Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.
