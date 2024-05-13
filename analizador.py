# codigo del analizador sintacticoimport matplotlib.pyplot as plt

import matplotlib
matplotlib.use('agg')  # Usa el backend "agg" para generar imágenes sin necesidad de una interfaz gráfica
import matplotlib.pyplot as plt
import graficacion

class Parser:
    def __init__(self):
        pass

    def parse(self, input_string):
        commands = input_string.split(',')
        for command in commands:
            if not self.command(command.strip().lower()):
                print("Comando inválido:", command.split()[0])
                return False
        return True

    def command(self, command):
        if command.startswith("triangulo"):
            return self.is_triangle(command)
        elif command.startswith("cuadrado"):
            return self.is_square(command)
        elif command.startswith("circulo"):
            return self.is_circle(command)
        elif command.startswith("rectangulo"):
            return self.is_rectangle(command)
        else:
            return False

    def is_triangle(self, command):
        params = command.split()[1:]
        if len(params) != 6:
            print("Comando de triángulo inválido. Debe proporcionar 6 parámetros: x1, y1, x2, y2, x3, y3")
            return False

        try:
            params = list(map(float, params))
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_triangle(*params)
        return True

    def is_square(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de cuadrado inválido. Debe proporcionar 3 parámetros: x y largo")
            return False

        try:
            x = float(params[0])
            y = float(params[1])
            large = float(params[2])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_square(x, y, large)
        return True

    def is_circle(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de círculo inválido. Debe proporcionar 3 parámetros: x y radio")
            return False
        
        try:
            x = float(params[0])
            y = float(params[1])
            radius = float(params[2])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_circle(x, y, radius)
        return True

    def is_rectangle(self, command):
        params = command.split()[1:]
        if len(params) != 4:
            print("Comando de rectángulo inválido. Debe proporcionar 4 parámetros: x, y, ancho, altura")
            return False

        try:
            params = list(map(float, params))
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_rectangle(*params)
        return True