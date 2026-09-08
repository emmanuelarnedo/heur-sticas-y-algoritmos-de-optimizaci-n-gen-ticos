import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter, LinearLocator
from mpl_toolkits.mplot3d import Axes3D


def graficarCaminata(fitness, solutions, bounds, resolution, alpha=0.5):
    """Graficar la funcion de evaluacion y las soluciones encontradas.
    Parametros
    ----------
    fitness : function
        Función de evaluación a optimizar
    solutions : list
        Lista de soluciones encontradas con método de optimización.
    bounds: list(tuple)
        Matriz de tamano nx2, donde n es la cantidad de variables que
        tiene el problema (cantidad de coordenadas del vector solución).
    resolution : float
        Resolución para graficar la función. Tomar un valor Mayor a 0.1.
    alpha : float
        Transparencia para el grafico de la función.
    """
    if len(bounds) == 1:
        fig = plt.figure()
        ax = fig.gca()

        ranges = []
        for i in range(len(bounds)):
            steps = round((bounds[i][1] - bounds[i][0]) / resolution)
            ranges.append([bounds[i][0] + s * resolution for s in range(steps)])

        X = []
        Y = []
        for i, xi in enumerate(ranges[0]):
            X.append(xi)
            Y.append(fitness([xi]))

        # Plot the line.
        plt.plot(X, Y, antialiased=False, alpha=alpha)

        # Add title and axis names
        plt.title("Función de Evaluación")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()

        x = [s[0] for s in solutions]
        y = [fitness(s) for s in solutions]

        ax.scatter(x, y, c="k", marker="o")

    elif len(bounds) == 2:
        fig = plt.figure()
        # ax = fig.gca(projection="3d")
        ax = plt.axes(projection='3d')

        ranges = []
        for i in range(len(bounds)):
            steps = round((bounds[i][1] - bounds[i][0]) / resolution)
            ranges.append([bounds[i][0] + s * resolution for s in range(steps)])

        X = []
        Y = []
        Z = []
        for i, xi in enumerate(ranges[0]):
            x_row = []
            y_row = []
            z_row = []
            for j, yj in enumerate(ranges[1]):
                x_row.append(xi)
                y_row.append(yj)
                z_row.append(fitness([xi, yj]))
            X.append(x_row)
            Y.append(y_row)
            Z.append(z_row)

        # Plot the surface.
        surf = ax.plot_surface(
            X,
            Y,
            np.array(Z),
            cmap=cm.coolwarm,
            linewidth=0,
            antialiased=False,
            alpha=alpha,
        )

        # Add title and axis names
        plt.title("Función de Evaluación")
        plt.xlabel("x")
        plt.ylabel("y")
        ax.set_zlabel("f(x,y)")

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        x = [s[0] for s in solutions]
        y = [s[1] for s in solutions]
        z = [fitness(s) + 1 for s in solutions]

        ax.scatter(x, y, z, c="k", marker="o")
        ax.view_init(elev=40.0, azim=60)

    else:
        print("No implementado para más de dos variables.")


def graficarEvolucionFitness(trace_f):
    """Método para graficar la evolucion del fitness con las iteraciones.
    Parametros
    ----------
    trace_f : list
        Lista con los valores de evaluación de la mejor y peor solución.
    """
    fig = plt.figure()
    ax = plt.axes()

    x = np.linspace(0, 10, 1000)
    x = [i for i in range(len(trace_f))]
    best = [t[0] for t in trace_f]
    worst = [t[1] for t in trace_f]
    plt.plot(x, best, label="Mejor solución")
    plt.plot(x, worst, label="Peor solución")

    # Add title and axis names
    plt.title("Valores de Evaluación")
    plt.xlabel("Iteración")
    plt.ylabel("Fitness")
    plt.grid()
    plt.legend()


def validate_inputs(X_mejor, bounds, cant_iterac, max_eps) -> bool:
    """
    Valida input data used in Hill Climbing algorithm.

    Parameters:
        - X_mejor
        - bounds
        - cant_interac
        - max_eps
    """
    if len(X_mejor) == 0:
        print("La solucion inicial debe tener al menos una variable.")
        return False

    if len(bounds) != len(X_mejor) or len(bounds[0]) != 2:
        print("La matriz de Bounds tiene un tamaño incorrecto.")
        return False

    if cant_iterac < 1:
        print("El número máximo de iteraciones debe ser positivo mayor a cero.")
        return False
    if max_eps <= 0:
        print("El tamaño del paso debe ser real y positivo.")
        return False
    return True
