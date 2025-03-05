from helpers import *


class Empresa:
    def __init__(self, nombre,  n_empleados, mes):
        self.nombre = nombre
        self.empleados = {}
        for i in range(n_empleados):
            self.añadir_empleado(i)
        self.mes = mes
        self.pago_total = 0

    def añadir_empleado(self, idx):
        print(f"--- Empleado {idx + 1} ---")
        datos_personales = {
            "nombre": input("Ingrese el nombre del empleado: "),
            "apellido": input("Ingrese el apellido del empleado: "),
            "ci": input("Ingrese la cédula del empleado: "),
            "cargo": input("Ingrese el cargo del empleado: "),
            "especialidad": input("Ingrese la especialidad del empleado: ")
        }
        self.empleados[idx] = Trabajador(self, datos_personales)
    
    def hacer_pagos(self):
        for empleado in self.empleados.values():
            empleado.pagar()

    def resumir(self):
        pagos1 = 0
        pagos2 = 0
        pagos3 = 0
        n1 = 0
        n2 = 0
        n3 = 0
        e1 = 0
        e2 = 0
        e3 = 0
        for empleado in self.empleados.values():
            if empleado.datos["cargo"] == "ingeniero":
                pagos1 += empleado.pago
                n1 += 1
                if empleado.pago > e1:
                    e1 = empleado.pago
                    max_ing = empleado
            elif empleado.datos["cargo"] == "arquitecto":
                pagos2 += empleado.pago
                n2 += 1
                if empleado.pago > e2:
                    e2 = empleado.pago
                    max_arq = empleado
            elif empleado.datos["cargo"] == "obrero":
                pagos3 += empleado.pago
                n3 += 1
                if empleado.pago > e3:
                    e3 = empleado.pago
                    max_obr = empleado
        print("-----------------------------------------------------------------------")
        print(f"Resumen contable de la empresa {self.nombre} para el mes de {self.mes}")
        print(f"Monto total pagado: {self.pago_total}")
        print(f"# de ingenieros: {n1}")
        print(f"# de arquitectos: {n2}")
        print(f"# de obreros: {n3}")
        print(f"Promedio de pago para ingenieros: {pagos1 / n1}")
        print(f"Promedio de pago para arquitectos: {pagos2 / n2}")
        print(f"Promedio de pago para obreros: {pagos3 / n3}")
        print(f"Ingeniero más pagado: {max_ing.datos['nombre']} {max_ing.datos['apellido']}")
        print(f"Arquitecto más pagado: {max_arq.datos['nombre']} {max_arq.datos['apellido']}")
        print(f"Obrero más pagado: {max_obr.datos['nombre']} {max_obr.datos['apellido']}")
        print("-----------------------------------------------------------------------")


class Trabajador():
    def __init__(self, empresa, datos_personales):
        self.datos = datos_personales
        self.empresa = empresa
        if self.datos["cargo"] == "ingeniero":
            self.salario = 25
        elif self.datos["cargo"] == "arquitecto":
            self.salario = 10
        elif self.datos["cargo"] == "obrero":
            self.salario = 5
    
    def pagar(self):
        self.horas = int(input(f"Ingrese el número de horas para el trabajador {self.datos['nombre']} {self.datos['apellido']}: "))
        self.pago = self.horas * self.salario
        if es_primo(self.horas):
            self.pago *= 1.05
        if es_deficiente(int(self.pago)):
            self.pago *= 1.1
        self.empresa.pago_total += self.pago
    