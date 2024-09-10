# 3: Calcular todas las operaciones

mensaje = "El resultado de"

def sumar(numero_a:int, numero_b:int) -> int:
    resultado_suma = numero_a + numero_b
    return resultado_suma


def restar(numero_a:int, numero_b:int) -> int:
    resultado_resta = numero_a - numero_b
    return resultado_resta


def dividir(numero_a:int, numero_b:int) -> int:
    resultado_division = numero_a / numero_b
    return resultado_division


def multiplicar(numero_a:int, numero_b:int) -> int:
    resultado_multiplicacion = numero_a * numero_b
    return resultado_multiplicacion


def potenciar(numero_a:int, numero_b:int) -> int:
    resultado_potenciacion = numero_a ** numero_b
    return resultado_potenciacion


def resto(numero_a:int, numero_b:int) -> int:
    resultado_resto = numero_a % numero_b
    if resto == 0:
        print(f"No se puede dividir por cero.")
    else:
        return resultado_resto
    

#def factorial... 