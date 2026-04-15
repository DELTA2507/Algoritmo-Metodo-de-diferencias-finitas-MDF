from metodo_diferencias_finitas import metodo_diferencias_finitas
from utilidades import error_absoluto, error_relativo


def ejecutar_experimentos(f, x, valor_exacto, lista_particiones, metodo):
    print("\n=== Experimentos automáticos ===")
    print(f"Metodo usado: {metodo}")

    print("\nparticiones | paso_h | resultado | valor_exacto | error_abs | error_rel | tiempo")

    for n in lista_particiones:
        aprox, t = metodo_diferencias_finitas(f, x, n, metodo)

        err_absoluto = error_absoluto(valor_exacto, aprox)
        err_relativo = error_relativo(valor_exacto, aprox)

        h = 1 / n

        print(f"{n:<11} {h:<8.4f} {aprox:<10.6f} {valor_exacto:<12.6f} {err_absoluto:<10.6f} {err_relativo:<10.6f} {t:<10.6f}")

    return lista_particiones