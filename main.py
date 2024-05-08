# codigo del main

from analizador import Parser
import matplotlib.pyplot as plt

def main():
    parser = Parser()
    while True:
        user_input = input("Ingrese el comando (triangulo, cuadrado, circulo, rectangulo), o 'exit' para salir: ")
        if user_input.lower() == 'exit':
            break
        if parser.parse(user_input):
            plt.axis('equal')
            plt.savefig('output.png')  # Guarda la figura como una imagen
            plt.close()  # Cierra la figura para liberar recursos

if __name__ == "__main__":
    main

