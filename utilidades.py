import math

def convertir_funcion(funcion_str):
    """
    Convierte un string en función ejecutable.
    Ej: "x**2 + math.sin(x)" -> función f(x)
    """
    def f(x):
        return eval(funcion_str, {"x": x, "math": math})
    return f

def error_absoluto(valor_exacto, valor_aproximado):
    return abs(valor_exacto - valor_aproximado)

def error_relativo(valor_exacto, valor_aproximado):
    return abs(valor_exacto - valor_aproximado) / abs(valor_exacto) if valor_exacto != 0 else float('inf')