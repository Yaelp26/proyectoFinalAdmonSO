# codigo del analizador sintacticoimport matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Usa el backend "agg" para generar imágenes sin necesidad de una interfaz gráfica
import matplotlib.pyplot as plt
import numpy as np

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
        if command in ["triangulo"]:
            return self.draw_triangle()
        elif command in ["cuadrado"]:
            return self.draw_square()
        elif command in ["circulo"]:
            return self.draw_circle()
        elif command in ["rectangulo"]:
            return self.draw_rectangle()
        else:
            return False

    def draw_triangle(self):
        x = [0, 1, 0]
        y = [0, 0, 1]
        plt.plot(x, y)
        return True

    def draw_square(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), 1, 1, fill=None))
        return True

    def draw_circle(self):
        circle = plt.Circle((0.5, 0.5), 0.5, fill=None)
        plt.gca().add_patch(circle)
        return True

    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0.25, 0.25), 0.5, 0.75, fill=None))
        return True
