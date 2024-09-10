# INTEGRADOR
# La división de higiene está trabajando en un control de stock para productos sanitarios. 
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos: 
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
# 4. La marca y el Fabricante.

# Se debe informar lo siguiente:
# A. Del más caro de los barbijos: la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.


# A
bandera_barbijo_mas_caro = 0

for i in range(5):

    tipo_producto = input("Ingrese el tipo de producto: ")
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input("Ingrese correctamente el tipo de producto: ")


    precio_producto = float(input("Ingrese el precio del producto: "))
    while precio_producto < 100 or precio_producto > 300:
        precio_producto = float(input("Ingrese correctamente el precio del producto: "))

    unidades_producto = int(input("Ingrese la cantidad de productos: "))
    while unidades_producto < 0 or unidades_producto > 1000:
        unidades_producto = int(input("Ingrese correctamente la cantidad de productos: "))

    marca_producto = input("Ingrese la marca del producto: ")

    fabricante_producto = input("Ingrese el fabricante del producto: ")



# TAREA: 
# Realizar una calculadora en donde se le pida al usuario una operación
# Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

# (+) -> Suma
# (-) -> Resta
# (/) -> Dividir
# (*) -> Multiplicar

# Luego de tener el operador, pedir dos números y hacer la operación correspondiente.
contador = 0


while contador == 0:

    operacion = input("Ingrese el tipo de operacion: ") 
    while operacion != "suma" and operacion != "resta" and operacion != "division" and operacion != "multiplicar":
        operacion = input("ReIngrese el tipo de operacion: ")

    ingreso_primer_numero = int(input("Ingrese el primer numero: "))

    ingreso_segundo_numero = int(input("Ingrese el segundo numero: "))
