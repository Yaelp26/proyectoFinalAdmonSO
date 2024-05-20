from analizador import Parser
import graficacion

def main():
    parser = Parser()
    while True:
        if parser.figura_generada:
            user_input = input('Ingrese el comando "eliminar", "transformar", "modificar x y", o "exit" para salir: ')
        else:
            user_input = input('Ingrese el comando "triangulo x y largo", "cuadrado x y largo", "circulo x y radio", "rectangulo x y ancho altura", o "exit" para salir: ')
        
        if user_input.lower() == 'exit':
            break
        
        parser.parse(user_input)

if __name__ == "__main__":
    main()