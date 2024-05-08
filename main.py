# codigo del main

from analizador import Parser
import matplotlib.pyplot as plt

def main():
    parser = Parser()
    while True:
        user_input = input("Ingrese el comando (triangulo x1 y1 x2 y2 x3 y3, cuadrado x y ancho altura, circulo x y radio, rectangulo x y ancho altura), o 'exit' para salir: ")
        if user_input.lower() == 'exit':
            break
        if parser.parse(user_input):
            plt.axis([-10, 10, -10, 10])  # Establece el rango de los ejes x e y
            plt.gca().set_aspect('equal', adjustable='box')  # Establece la relación de aspecto de los ejes a igual
            plt.show()  # Muestra la figura de manera interactiva
            plt.savefig('output.png')  # Guarda la figura como una imagen
            plt.close()  # Cierra la figura para liberar recursos

if __name__ == "__main__":
    main()