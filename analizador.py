import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Usa el backend "agg" para generar imágenes sin necesidad de una interfaz gráfica
import graficacion

class Parser:
    def __init__(self):
        self.figura_generada = False
        self.figura_actual = None

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
        elif command == "eliminar":
            return self.eliminar()
        elif command == "transformar":
            return self.transformar()
        elif command.startswith("modificar"):
            return self.modificar(command)
        else:
            return False

    def is_triangle(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de triángulo inválido. Debe proporcionar 3 parámetros: x, y, largo")
            return False

        try:
            x = float(params[0])
            y = float(params[1])
            largo = float(params[2])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_equilateral_triangle(x, y, largo)
        self.figura_generada = True
        self.figura_actual = ("triangulo", x, y, largo)
        graficacion.guardar_figura()
        print("Figura generada en output.png")
        return True

    def is_square(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de cuadrado inválido. Debe proporcionar 3 parámetros: x, y, largo")
            return False

        try:
            x = float(params[0])
            y = float(params[1])
            largo = float(params[2])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_square(x, y, largo)
        self.figura_generada = True
        self.figura_actual = ("cuadrado", x, y, largo)
        graficacion.guardar_figura()
        print("Figura generada en output.png")
        return True

    def is_circle(self, command):
        params = command.split()[1:]
        if len(params) != 3:
            print("Comando de círculo inválido. Debe proporcionar 3 parámetros: x, y, radio")
            return False
        
        try:
            x = float(params[0])
            y = float(params[1])
            radio = float(params[2])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_circle(x, y, radio)
        self.figura_generada = True
        self.figura_actual = ("circulo", x, y, radio)
        graficacion.guardar_figura()
        print("Figura generada en output.png")
        return True

    def is_rectangle(self, command):
        params = command.split()[1:]
        if len(params) != 4:
            print("Comando de rectángulo inválido. Debe proporcionar 4 parámetros: x, y, ancho, altura")
            return False

        try:
            x = float(params[0])
            y = float(params[1])
            ancho = float(params[2])
            altura = float(params[3])
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        graficacion.draw_rectangle(x, y, ancho, altura)
        self.figura_generada = True
        self.figura_actual = ("rectangulo", x, y, ancho, altura)
        graficacion.guardar_figura()
        print("Figura generada en output.png")
        return True

    def eliminar(self):
        plt.gca().clear()  # Limpia el contenido del plano actual
        plt.close()  # Cierra la figura actual
        graficacion.guardar_figura()  # Guarda la figura vacía
        print("Plano limpiado")
        self.figura_generada = False
        return True

    def transformar(self):
        self.figura_generada = False
        return True

    def modificar(self, command):
        if not self.figura_generada or self.figura_actual is None:
            print("No hay figura generada para modificar")
            return False

        params = command.split()[1:]
        figura_tipo = self.figura_actual[0]
        if figura_tipo in ["triangulo", "cuadrado", "circulo", "rectangulo"] and len(params) != 2:
            print(f"Comando de modificación de {figura_tipo} inválido. Debe proporcionar 2 parámetros: nuevo x, nuevo y")
            return False

        try:
            new_params = list(map(float, params))
        except ValueError:
            print("Error: Los parámetros deben ser números")
            return False

        # Actualizar los parámetros de la figura actual
        self.figura_actual = (self.figura_actual[0], new_params[0], new_params[1], *self.figura_actual[3:])

        # Dibujar la figura nuevamente
        if figura_tipo == "triangulo":
            graficacion.draw_equilateral_triangle(*new_params, self.figura_actual[3])
        elif figura_tipo == "cuadrado":
            graficacion.draw_square(*new_params, self.figura_actual[3])
        elif figura_tipo == "circulo":
            graficacion.draw_circle(*new_params, self.figura_actual[3])
        elif figura_tipo == "rectangulo":
            graficacion.draw_rectangle(*new_params, *self.figura_actual[3:])

        # Guardar la figura
        graficacion.guardar_figura()

        return True