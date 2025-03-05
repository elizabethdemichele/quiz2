from modelo import *

def main():
    empresa = Empresa(
        nombre = input("Ingrese el nombre de la empresa: "),
        n_empleados = int(input("Ingrese el número de empleados: ")),
        mes = input("Ingrese el mes de trabajo: ")
    )
    empresa.hacer_pagos()
    empresa.resumir()

main()