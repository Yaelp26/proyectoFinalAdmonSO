#Codigo de graficacion

import matplotlib.pyplot as plt

def draw_triangle(x1, y1, x2, y2, x3, y3):
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    plt.fill(x, y, edgecolor='black', fill=False)
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