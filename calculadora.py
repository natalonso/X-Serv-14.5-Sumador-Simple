#!/usr/bin/python3
#SEGUNDA VERSIÓN DE LA CALCULADORA CON IN NAME == MAIN
#COMPATIBLE CON LA APP WEB SUMADOR_SIMPLE

import sys

def suma(operando1, operando2):
    resultado = int(operando1) + int(operando2)
    return resultado

def resta(operando1, operando2):
    resultado = int(operando1) - int(operando2)
    return resultado

def multiplicacion(operando1,operando2):
    resultado = int(operando1) * int(operando2)
    return resultado

def division(operando1,operando2):
        try:
            resultado = int(operando1) / int(operando2)
            return resultado
        except ZeroDivisionError:
            resultado = "No intentes dividir entre cero"
            return resultado
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("El numero de argumentos introducidos no es correcto")
        sys.exit()

    operacion = sys.argv[1]
    operando1 = sys.argv[2]
    operando2 = sys.argv[3]

    if operacion == "suma":
        resultado = suma(operando1,operando2)
        print("El resultado es: " + str(resultado))
        sys.exit()

    if operacion == "resta":
        resultado = resta(operando1,operando2)
        print("El resultado es: " + str(resultado))
        sys.exit()

    if operacion == "multiplicacion":
        resultado = multiplicacion(operando1,operando2)
        print("El resultado es: " + str(resultado))
        sys.exit()

    if operacion == "division":
        resultado = division(operando1,operando2)
        print("El resultado es: " + str(resultado))
        sys.exit()
