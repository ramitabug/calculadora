# Ramiro Villalba
# Ejercicio 1, For.

# Para un hospital veterinario
# Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 20 mascotas), para esto hay que considerar los siguientes datos 
# y encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:

# -Edad (Validar entre 1 y 25 años) 
# -Tipo: (Validar “gato”, “perro”, “loro”) 
# -Peso: (Más de 0 kg) -
# -Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
# -Vacuna antirrábica (validar “si”, ”no”)

# CALCULAR
# 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
# 2. El tipo de mascota más ingresada con problemas digestivos.
# 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
# 4. Porcentaje de mascotas vacunadas y no vacunadas.
# 5. Promedio de edad de los gatos.


#1
mascotas_sin_antirrabica_edad_4a12 = 0

#2
contador_gato_diagnostico_digestivo = 0
contador_perro_diagnostico_digestivo = 0
contador_loro_diagnostico_digestivo = 0

#3
bandera_mascota_mas_vieja_con_antirrabica = 0

#4
mascotas_vacunadas = 0
mascotas_no_vacunadas = 0

#5
acumulador_edad_ingresada_gatos = 0
contador_gatos_ingresados = 0


for i in range(21):
    edad_ingresada = int(input("Ingrese la edad de la mascota: "))
    while edad_ingresada < 1 or edad_ingresada > 25:
        edad_ingresada = int(input("Ingrese correctamente la edad de la mascota: "))


    tipo_mascota = input("Ingrese el tipo de mascota: ")
    while tipo_mascota != "Gato" and tipo_mascota != "Perro" and tipo_mascota != "Loro":
        tipo_mascota = input("Ingrese correctamente el tipo de mascota: ")

    # 5. Promedio de edad de los gatos. 
    if tipo_mascota == "Gato":
        contador_gatos_ingresados += 1
        acumulador_edad_ingresada_gatos += edad_ingresada


    peso_mascota = float(input("Ingrese el peso de la mascota: "))
    while peso_mascota < 0:
        peso_mascota = float(input("Ingrese correctamente el peso de la mascota: "))
    

    diagnostico_mascota = input("Ingrese el diagnostico de la mascota: ")
    while diagnostico_mascota != "problemas digestivos" and diagnostico_mascota != "parasitos" and diagnostico_mascota != "infeccion":
        diagnostico_mascota = input("Ingrese correctamente el diagnostico de la mascota: ")


    vacuna_antirrabica = input("Ingrese por si o no si su mascota cuenta con vacuna antirrabica: ")
    while vacuna_antirrabica != "Si" and vacuna_antirrabica != "No":
        vacuna_antirrabica = input("Ingrese correctamente por si o no si su mascota cuenta con vacuna antirrabica: ")

    print("/////////")

   
    # 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
    if vacuna_antirrabica == "No" and edad_ingresada > 4 and edad_ingresada < 12:
        if diagnostico_mascota == "parásitos" or diagnostico_mascota == "infeccion":
            mascotas_sin_antirrabica_edad_4a12 += 1
            

    # 2. El tipo de mascota más ingresada con problemas digestivos.
    if diagnostico_mascota == "problemas digestivos":
        match tipo_mascota:
            case "Gato":
                contador_gato_diagnostico_digestivo += 1
            case "Perro":
                contador_perro_diagnostico_digestivo += 1
            case _:
                contador_loro_diagnostico_digestivo += 1
    

    # 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
    if vacuna_antirrabica == "Si":
        if bandera_mascota_mas_vieja_con_antirrabica == 0:
            edad_mascota_mayor_con_antirrabica = edad_ingresada
            tipo_mascota_mayor_con_antirrabica = tipo_mascota
            bandera_mascota_mas_vieja_con_antirrabica += 1
    elif edad_ingresada > edad_mascota_mayor_con_antirrabica:
            edad_mascota_mayor_con_antirrabica = edad_ingresada
            tipo_mascota_mayor_con_antirrabica = tipo_mascota



    # 4. Porcentaje de mascotas vacunadas y no vacunadas.
    match vacuna_antirrabica:
        case "Si":
            mascotas_vacunadas += 1
        case _:
            mascotas_no_vacunadas += 1



# 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
print(f"Mascotas sin antirrabica entre los 4 y 12 años, diagnostico por infeccion o parasitos: {mascotas_sin_antirrabica_edad_4a12} ")


# 2. El tipo de mascota más ingresada con problemas digestivos.
if contador_gato_diagnostico_digestivo > (contador_perro_diagnostico_digestivo and contador_loro_diagnostico_digestivo):
    print(f"El gato fue la mascota mas ingresada con problemas digestivos. {contador_gato_diagnostico_digestivo} ")
elif contador_perro_diagnostico_digestivo > (contador_gato_diagnostico_digestivo and contador_loro_diagnostico_digestivo):
    print(f"El perro fue la mascota mas ingresada con problemas digestivos. {contador_perro_diagnostico_digestivo} ")
else:
    print(f"El loro fue la mascota mas ingresada con problemas digestivos. {contador_loro_diagnostico_digestivo} ")


# 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
print(f"El {tipo_mascota_mayor_con_antirrabica} con {edad_mascota_mayor_con_antirrabica} años fue la mascota mas vieja con vacuna antirrabica.")


# 4. Porcentaje de mascotas vacunadas y no vacunadas.
porcentaje_vacunadas= mascotas_vacunadas * 100 // i
porcentaje_no_vacunadas = mascotas_no_vacunadas * 100 // i 
print(f"El porcentaje de mascotas vacunadas fue del {porcentaje_vacunadas} % y el de las no vacunadas del {porcentaje_no_vacunadas}%. ")


# 5. Promedio de edad de los gatos.
promedio_edad_gatos = acumulador_edad_ingresada_gatos / contador_gatos_ingresados
print(f"El promedio de edad de los gatos ingresados fue del {promedio_edad_gatos}." )