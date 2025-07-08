# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    fig = plt.figure()
    fig.suptitle('Grilla con 4 funciones', fontsize=16)

    # Crear 4 subplots en disposición 2x2
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # Gráfico 1: y1 = x^2
    ax1.plot(x, y1, color='darkred', label='y1 = x^2')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls='dashed')
    ax1.set_ylabel("Y[amplitud]")
    ax1.set_xlabel("X")
    ax1.legend()

    # Gráfico 2: y2 = x^3
    ax2.plot(x, y2, color='green', label='y2 = x^3')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dashed')
    ax2.set_ylabel("Y[amplitud]")
    ax2.set_xlabel("X")
    ax2.legend()

    # Gráfico 3: y3 = x^4
    ax3.plot(x, y3, color='orange', label='y3 = x^4')
    ax3.set_facecolor('whitesmoke')
    ax3.grid(ls='dashed')
    ax3.set_ylabel("Y[amplitud]")
    ax3.set_xlabel("X")
    ax3.legend()

    # Gráfico 4: y4 = sqrt(x)
    ax4.plot(x, y4, color='blue', label='y4 = sqrt(x)')
    ax4.set_facecolor('whitesmoke')
    ax4.grid(ls='dashed')
    ax4.set_ylabel("Y[amplitud]")
    ax4.set_xlabel("X")
    ax4.legend()

    # Mostrar figura con los 4 gráficos
    plt.tight_layout()
    plt.show()

    print("terminamos")