numero_ingresado = int(input("Ingrese un numero: "))
bandera = True

for i in range(2, numero_ingresado, 1):
    if numero_ingresado % i == 0:
        print(f"{numero_ingresado} / {i} da resultado entero. Por lo tanto NO es primo")
        bandera = False
        break # Cuando ya verifique que no es primo, corto con el for.

if bandera == True:
    print(f"El numero {numero_ingresado} da resultado flotante. Por lo tanto SI es primo.")