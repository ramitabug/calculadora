#calcular_precio_iva(1000,10) #Llamada -> NO

#Definición de una función
def calcular_precio_iva(importe_sin_iva : float,iva:float=21.0) -> float:
    '''
        Se encarga de calcular el precio con iva
        recibe un importe sin iva y también el iva (opcional) que por defecto es 21%
        Retorna el precio con iva
    '''
    
    importe_con_iva = importe_sin_iva * (1 + (iva / 100))
    return importe_con_iva

#numero_a y numero_b -> Son las entradas
def sumar(numero_a:int,numero_b:int) -> int:
    '''
    Se encarga de sumar dos numeros enteros
    Recibe el numero_a y el numero_b
    Retorna la suma de los mismos
    '''
    suma = numero_a + numero_b #Proceso
    return suma #Salida

def restar(numero_a:int,numero_b:int) -> int:
    '''
    Se encarga de restar dos numeros enteros
    Recibe el numero_a y el numero_b
    Retorna la suma de los mismos
    '''
    resta = numero_a - numero_b #Proceso
    return resta #Salida
    
#numero_uno = int(input("Ingrese numero 1 "))
#numero_dos = int(input("Ingrese numero 2 "))
#resultado = restar(10,5)#Pasaje de parametros por posicion
#resultado = restar(numero_b=10,numero_a=5)#Pasaje de parametros por nombre
#print(f"El resultado de la resta es {resultado}")


#resultado = sumar(numero_uno,numero_dos)

# print(f"El resultado entre {numero_uno} y {numero_dos} de la suma es {resultado}")

#resultado = calcular_precio_iva(1000.0,10) #Llamada -> SI
#print(type(resultado))

#calcular_precio_iva(1000) #Llamada -> SI, el parametro IVA va a ser reemplazado por 21
#calcular_precio_iva()#Llamada -> NO