# ---------------------------------------------------------
# Ejemplo de uso de TimSort en Python para sensores de temperatura
# ---------------------------------------------------------

from random import uniform  
# Importamos la función 'uniform' del módulo 'random' para generar números decimales aleatorios en un rango dado.

def generar_datos_sensores(num_sensores):
    """
    Genera una lista de sensores con IDs y temperaturas simuladas.
    Cada sensor es representado como una tupla: (id_sensor, temperatura)
    Las temperaturas varían entre -20.0 y 120.0 grados Celsius.
    """
    sensores = []  
    # Creamos una lista vacía para almacenar los datos de los sensores.

    for i in range(1, num_sensores + 1):  
        # Bucle que se repite desde 1 hasta el número total de sensores (inclusive).

        temp = round(uniform(-20.0, 120.0), 2)  
        # Generamos un número decimal aleatorio entre -20.0 y 120.0,
        # redondeado a 2 decimales para simular la temperatura del sensor.

        sensores.append((f"Sensor_{i:03d}", temp))  
        # Añadimos a la lista un nuevo sensor como una tupla:
        # El ID tiene formato "Sensor_001", "Sensor_002", etc. usando ceros a la izquierda para 3 dígitos.
        # La temperatura es el número aleatorio generado.

    return sensores  
    # Devolvemos la lista completa de sensores con sus temperaturas.

def detectar_anomalias(sensores, umbral_temp=100.0):
    """
    Detecta sensores cuya temperatura supera un umbral (posible fallo o sobrecalentamiento).
    Primero ordena los sensores por temperatura (de menor a mayor) usando TimSort,
    que es el algoritmo nativo de Python en sorted().
    """
    # Ordenamos usando sorted() (que internamente usa TimSort), especificando que
    # la clave para ordenar es la temperatura, que está en la posición 1 de cada tupla.
    sensores_ordenados = sorted(sensores, key=lambda x: x[1])

    # Creamos una lista con solo los sensores cuya temperatura es mayor que el umbral.
    anomalias = [sensor for sensor in sensores_ordenados if sensor[1] > umbral_temp]

    return sensores_ordenados, anomalias  
    # Devolvemos dos listas: sensores ordenados y sensores con temperatura anómala.

def mostrar_sensores(sensores):
    print("\nLista de sensores ordenados por temperatura:")
    # Mensaje informativo antes de mostrar la lista ordenada.

    for sensor_id, temp in sensores:  
        # Recorremos cada sensor en la lista, extrayendo su ID y temperatura.

        print(f"{sensor_id}: {temp} °C")  
        # Imprimimos el ID del sensor y su temperatura con unidad.

def mostrar_anomalias(anomalias):
    if anomalias:  
        # Comprobamos si la lista de anomalías no está vacía.

        print("\n⚠️ Sensores con temperatura anómala (sobre 100°C):")
        # Mensaje de alerta para los sensores con temperaturas altas.

        for sensor_id, temp in anomalias:  
            # Recorremos la lista de sensores anómalos.

            print(f" - {sensor_id}: {temp} °C")  
            # Imprimimos cada sensor anómalo con su temperatura.

    else:
        print("\n✅ No se detectaron sensores con temperaturas anómalas.")
        # Si no hay anomalías, mostramos mensaje de todo normal.

# ----------------------------------------
# Bloque principal
# ----------------------------------------

if __name__ == "__main__":  
    # Esto asegura que el código solo se ejecute si este archivo es el programa principal
    # y no cuando se importe como módulo en otro script.

    sensores = generar_datos_sensores(20)  
    # Generamos datos de 20 sensores simulados con temperaturas aleatorias.

    sensores_ordenados, sensores_anomalias = detectar_anomalias(sensores)  
    # Ordenamos los sensores por temperatura y detectamos cuáles superan el umbral.

    mostrar_sensores(sensores_ordenados)  
    # Imprimimos la lista completa de sensores ordenados.

    mostrar_anomalias(sensores_anomalias)  
    # Imprimimos la lista (si existe) de sensores con temperaturas anómalas.
    