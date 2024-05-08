# codigo del analizador sintacticoimport matplotlib.pyplot as plt

import matplotlib
matplotlib.use('agg')  # Usa el backend "agg" para generar imágenes sin necesidad de una interfaz gráfica
import matplotlib.pyplot as plt

class Parser:
    def __init__(self):
        pass

    def parse(self, input_string):
        commands = input_string.split(',')
        for command in commands:
            if not self.command(command.strip().lower()):
                print("Comando inválido:", command.strip())
                return False
        return True

    def command(self, command):
        if command.startswith("triangulo"):
            return self.draw_triangle(command)
        elif command.startswith("cuadrado"):
            return self.draw_square(command)
        elif command.startswith("circulo"):
            return self.draw_circle(command)
        elif command.startswith("rectangulo"):
            return self.draw_rectangle(command)
        else:
            return False

    def draw_triangle(self, command):
        params = command.split()[1:]
        if len(params) != 6:
            print("Comando de triangulo inválido. Debe proporcionar 6 parámetros: x1, y1, x2, y2, x3, y3")
            return False
        x = [float(params[0]), float(params[2]), float(params[4])]
        y = [float(params[1]), float(params[3]), float(params[5])]
        plt.fill(x, y, edgecolor='black', fill=False)
        return True

    def draw_square(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de cuadrado inválido. Debe proporcionar 4 parámetros: x, y, largo")
            return False
        x = float(params[0])
        y = float(params[1])
        large = float(params[2])
        plt.gca().add_patch(plt.Rectangle((x, y), large, large, fill=None))
        return True

    def draw_circle(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de círculo inválido. Debe proporcionar 3 parámetros: x, y, radio")
            return False
        x = float(params[0])
        y = float(params[1])
        radius = float(params[2])
        circle = plt.Circle((x, y), radius, fill=None)
        plt.gca().add_patch(circle)
        return True

    def draw_rectangle(self, command):
        params = command.split()[1:]
        if len(params) != 4:
            print("Comando de rectángulo inválido. Debe proporcionar 4 parámetros: x, y, ancho, altura")
            return False
        x = float(params[0])
        y = float(params[1])
        width = float(params[2])
        height = float(params[3])
        plt.gca().add_patch(plt.Rectangle((x, y), width, height, fill=None))
        return True