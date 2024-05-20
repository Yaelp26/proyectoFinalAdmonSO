#Codigo de graficacion

import matplotlib.pyplot as plt
import math

def draw_equilateral_triangle(x, y, lado):
    altura = (math.sqrt(3) / 2) * lado
    x2 = x + lado
    y2 = y
    x3 = x + (lado / 2)
    y3 = y + altura
    x_coords = [x, x2, x3, x]
    y_coords = [y, y2, y3, y]
    plt.plot(x_coords, y_coords, marker='o')
    return True

def draw_square(x, y, large):
    plt.gca().add_patch(plt.Rectangle((x, y), large, large, fill=None))
    return True

def draw_circle(x, y, radius):
    circle = plt.Circle((x, y), radius, fill=None)
    plt.gca().add_patch(circle)
    return True

def draw_rectangle(x, y, width, height):
    plt.gca().add_patch(plt.Rectangle((x, y), width, height, fill=None))
    return True

def guardar_figura():
    plt.axis([-10, 10, -10, 10])  # Establece el tamano de los ejes x y
    plt.gca().set_aspect('equal', adjustable='box')  
    plt.savefig('output.png')  # Guarda la figura como una imagen
    plt.close()  
    print("Figura generada en output.png")