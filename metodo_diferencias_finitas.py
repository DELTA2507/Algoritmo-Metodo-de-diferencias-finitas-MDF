import time

def metodo_diferencias_finitas(f, x, n, metodo):
    h = 1 / n
    inicio = time.time()

    if metodo == "forward":
        deriv = (f(x + h) - f(x)) / h
    elif metodo == "backward":
        deriv = (f(x) - f(x - h)) / h
    else:
        deriv = (f(x + h) - f(x - h)) / (2 * h)

    fin = time.time()
    return deriv, fin - inicio