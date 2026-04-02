import time

def metodo_diferencias_finitas(f, x, n, metodo="central"):
    """
    Calcula la derivada usando diferencias finitas.

    f: función
    x: punto donde derivar
    n: número de particiones
    metodo: "forward", "backward", "central"
    """
    h = 1 / n  # tamaño de paso
    inicio = time.time()

    if metodo == "forward":
        deriv = (f(x + h) - f(x)) / h
    elif metodo == "backward":
        deriv = (f(x) - f(x - h)) / h
    else:  # central
        deriv = (f(x + h) - f(x - h)) / (2 * h)

    fin = time.time()
    return deriv, fin - inicio