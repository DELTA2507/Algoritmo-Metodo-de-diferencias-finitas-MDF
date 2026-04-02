from metodo_diferencias_finitas import metodo_diferencias_finitas
from utilidades import convertir_funcion
from experimentos import ejecutar_experimentos
from graficos import graficar_error_vs_particiones, graficar_tiempo_vs_particiones


def main():
    print("==== Método de Diferencias Finitas ====")

    funcion_str = input("Ingrese la función a derivar (ej: x**2 + 3*x): ")
    f = convertir_funcion(funcion_str)

    punto = float(input("Ingrese el punto donde derivar: "))
    num_particiones = int(input("Ingrese el número de particiones: "))

    resultado, tiempo = metodo_diferencias_finitas(f, punto, num_particiones)
    print(f"\nResultado aproximado: {resultado}")
    print(f"Tiempo de ejecución: {tiempo:.6f} s")

    valor_exacto = float(input("Ingrese el valor exacto de la derivada: "))

    # Ejecutar experimentos automáticos
    particiones = ejecutar_experimentos(f, punto, valor_exacto)

    # Graficar resultados
    graficar_error_vs_particiones(f, punto, valor_exacto, particiones)
    graficar_tiempo_vs_particiones(f, punto, particiones)


if __name__ == "__main__":
    main()