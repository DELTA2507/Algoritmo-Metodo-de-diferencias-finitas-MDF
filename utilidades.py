import math

def convertir_funcion(funcion_str):
    entorno = {"x": 0}
    entorno.update(vars(math))

    def f(x):
        entorno["x"] = x
        return eval(funcion_str, {"__builtins__": {}}, entorno)

    return f

def error_absoluto(valor_exacto, valor_aproximado):
    return abs(valor_exacto - valor_aproximado)

def error_relativo(valor_exacto, valor_aproximado):
    return abs(valor_exacto - valor_aproximado) / abs(valor_exacto) if valor_exacto != 0 else float("inf")