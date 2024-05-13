# codigo del main

from analizador import Parser
import graficacion

def main():
    parser = Parser()
    while True:
        user_input = input('Ingrese el comando "triangulo x1 y1 x2 y2 x3 y3", "cuadrado x y largo", "circulo x y radio", "rectangulo x y ancho altura", o "exit" para salir: ')
        if user_input.lower() == 'exit':
            break
        if parser.parse(user_input):
            graficacion.guardar_figura()

if __name__ == "__main__":
    main()