from metodo_diferencias_finitas import metodo_diferencias_finitas
from utilidades import convertir_funcion
from experimentos import ejecutar_experimentos
from graficos import graficar_error_vs_particiones, graficar_tiempo_vs_particiones


def main():

    # --------------------------------------------------
    # 1. Inicio del programa
    # --------------------------------------------------

    print("==== Método de Diferencias Finitas ====")


    # --------------------------------------------------
    # 2. El usuario introduce la función a derivar
    #    Ejemplo: x**2 + 3*x
    # --------------------------------------------------

    funcion_str = input("Ingrese la función a derivar ej: (x**2 + 3*x) o sin(x): ")
    f = convertir_funcion(funcion_str)


    # --------------------------------------------------
    # 3. El usuario introduce el punto donde se evaluará
    #    la derivada
    # --------------------------------------------------

    punto = float(input("Ingrese el punto donde derivar: "))


    # --------------------------------------------------
    # 4. El usuario selecciona el metodo de diferencias
    #    finitas que se utilizará
    #
    #    forward  -> diferencia hacia adelante
    #    backward -> diferencia hacia atrás
    #    central  -> diferencia central
    # --------------------------------------------------

    metodo = input("Ingrese el metodo (forward, backward, central): ").strip().lower()


    # --------------------------------------------------
    # 5. El usuario introduce el valor exacto de la
    #    derivada para poder calcular errores
    # --------------------------------------------------

    valor_exacto = float(input("Ingrese el valor exacto de la derivada: "))


    # --------------------------------------------------
    # 6. El usuario introduce una lista de particiones
    #    separadas por comas para realizar los
    #    experimentos numéricos
    #
    #    Ejemplo:
    #    1,2,5,10,20,50,100
    # --------------------------------------------------

    lista_particiones_str = input(
        "Ingrese las particiones separadas por coma (ej: 1,2,5,10,20,50,100): "
    )

    lista_particiones = [int(x.strip()) for x in lista_particiones_str.split(",")]


    # --------------------------------------------------
    # 7. Se toma la primera partición de la lista para
    #    mostrar un cálculo inicial de la derivada
    # --------------------------------------------------

    n_inicial = lista_particiones[0]


    # --------------------------------------------------
    # 8. Se ejecuta el metodo de diferencias finitas
    #    con la partición inicial
    # --------------------------------------------------

    resultado, tiempo = metodo_diferencias_finitas(f, punto, n_inicial, metodo)


    # --------------------------------------------------
    # 9. Se muestra el resultado aproximado y el
    #    tiempo de ejecución
    # --------------------------------------------------

    print(f"\nResultado aproximado con n = {n_inicial}: {resultado}")
    print(f"Tiempo de ejecución: {tiempo:.6f} s")


    # --------------------------------------------------
    # 10. Se ejecutan los experimentos automáticos
    #     usando todas las particiones indicadas por
    #     el usuario
    # --------------------------------------------------

    particiones = ejecutar_experimentos(
        f,
        punto,
        valor_exacto,
        lista_particiones,
        metodo
    )


    # --------------------------------------------------
    # 11. Se generan los gráficos del experimento
    #
    #     - Error vs número de particiones
    #     - Tiempo vs número de particiones
    # --------------------------------------------------

    graficar_error_vs_particiones(f, punto, valor_exacto, particiones, metodo)
    graficar_tiempo_vs_particiones(f, punto, particiones, metodo)


# --------------------------------------------------
# Punto de entrada del programa
# --------------------------------------------------

if __name__ == "__main__":
    main()