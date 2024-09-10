#Ejercitación Clase 2 (Resolver con for).

# 1.Mostrar números ascendentes del 1 al 10
for i in range(1,11,1):
   print(i)


# 2.Mostrar números descendentes del 10 al 1
for i in range(10,0,-1):
   print(i)


# 3.Ingresar dos números y mostrar desde el primer número hasta el segundo que ingresaron de manera ascendente, 
# en caso de que el primer número sea mayor al segundo mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
# Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)
numero_uno = int(input("Primer numero: "))
numero_dos = int(input("Segundo numero: "))

if numero_uno < numero_dos:
    for i in range(numero_uno, numero_dos, +1 ):
        print(i)
elif numero_uno > numero_dos:
    for i in range(numero_uno, numero_dos -1, -1):
        print(i)
else:
    print(numero_uno)


# 4.Se ingresan un máximo de 5 números o hasta que el usuario ingrese el número 0. Mostrar la suma y promedio de los mismos.
contador_num = 0
acumulador_num = 0

for i in range(5):
    num = int(input("Ingrese números: "))

    if num == 0:
        break

    contador_num += 1
    acumulador_num += num
#observacion# en caso de que el primer numero ingresado sea el 0 y no lo promedie, solamente lo muestre por consola
# ya que no se puede dividir por 0
if contador_num != 0: 
    promedio = acumulador_num / contador_num
    print(acumulador_num)
    print(promedio)
else:
    print("No se ingreso ningun numero, no se pude promediar por 0.")


#5.Mostrar todos los números pares entre el 1 hasta el 100 (sin usar condiciones lógicas)
for i in range(1,100,2):
    print(i + 1)

# 6.Ingresar un número. Determinar si el número es primo o no.
numero_ingresado = int(input("Ingrese un numero: "))
bandera = True

for i in range(2, numero_ingresado, 1):
    if numero_ingresado % i == 0:
        print(f"{numero_ingresado} / {i} da resultado entero. Por lo tanto NO es primo")
        bandera = False
        break # Cuando ya verifique que no es primo, corto con el for.

if bandera == True:
    print(f"El numero {numero_ingresado} da resultado flotante. Por lo tanto SI es primo.")


# 7.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
numero = int(input("Ingrese un numero: "))

contador = 0
bandera = True

for i in range(2, numero+1, 1):
    if numero % i == 0:
        bandera == True
        
    if bandera == False:
        contador += 1
        print(numero)

print(f"Se encontraron {contador} numeros primos.\n")
        

# 8. Ingresar un número y mostrar la tabla de multiplicar de ese número.
# Por ejemplo si se ingresa el numero 3:
# 3 x 0 = 0 
# 3 x 1  = 3
# 3 x 2 = 6
# 3 x 3  = 9

numero = int(input("Ingresar numero: "))
contador = 0

for i in range(0,10,1):
    contador += 1
    print(contador * numero)
    print(f"")








