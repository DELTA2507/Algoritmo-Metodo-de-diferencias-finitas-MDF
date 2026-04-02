import matplotlib.pyplot as plt
from metodo_diferencias_finitas import metodo_diferencias_finitas
from utilidades import error_absoluto


def graficar_error_vs_particiones(f, x, valor_exacto, lista_particiones):
    errores = []
    for n in lista_particiones:
        aprox, _ = metodo_diferencias_finitas(f, x, n)
        errores.append(error_absoluto(valor_exacto, aprox))

    plt.figure()
    plt.plot(lista_particiones, errores, marker='o')
    plt.xlabel("Número de particiones")
    plt.ylabel("Error absoluto")
    plt.title("Error vs Número de particiones")
    plt.grid(True)
    plt.show()


def graficar_tiempo_vs_particiones(f, x, lista_particiones):
    tiempos = []
    for n in lista_particiones:
        _, t = metodo_diferencias_finitas(f, x, n)
        tiempos.append(t)

    plt.figure()
    plt.plot(lista_particiones, tiempos, marker='o', color='orange')
    plt.xlabel("Número de particiones")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo vs Número de particiones")
    plt.grid(True)
    plt.show()