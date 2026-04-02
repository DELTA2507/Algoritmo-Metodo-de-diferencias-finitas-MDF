from metodo_diferencias_finitas import metodo_diferencias_finitas
from utilidades import error_absoluto, error_relativo


def ejecutar_experimentos(f, x, valor_exacto):
    print("\n=== Experimentos automáticos ===")
    lista_particiones = [1, 2, 5, 10, 20, 50, 100]

    print("particiones | resultado | error_absoluto | error_relativo | tiempo_ejecución_segundos")
    for n in lista_particiones:
        aprox, t = metodo_diferencias_finitas(f, x, n)
        err_absoluto = error_absoluto(valor_exacto, aprox)
        err_relativo = error_relativo(valor_exacto, aprox)
        print(f"{n:<11} {aprox:<10.6f} {err_absoluto:<10.6f} {err_relativo:<10.6f} {t:<10.6f}")

    return lista_particiones