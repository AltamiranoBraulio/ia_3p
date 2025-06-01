# Función que implementa el método de Insertion Sort para ordenar contactos por nombre
def insertion_sort_contactos(contactos):
    for i in range(1, len(contactos)):
        actual = contactos[i]  # Contacto actual a insertar en la posición correcta
        j = i - 1

        # Comparamos nombres (ignora mayúsculas/minúsculas)
        while j >= 0 and contactos[j]['nombre'].lower() > actual['nombre'].lower():
            contactos[j + 1] = contactos[j]  # Desplazamos el contacto a la derecha
            j -= 1
        contactos[j + 1] = actual  # Insertamos el contacto en la posición correcta

    return contactos


# Función para mostrar la agenda de forma bonita
def mostrar_agenda(contactos):
    print("\n📖 Agenda de Contactos Ordenada:")
    for c in contactos:
        print(f"👤 {c['nombre']} - 📞 {c['telefono']}")
    print()


# Bloque principal
if __name__ == "__main__":
    # Creamos una lista de contactos con nombre y teléfono
    agenda = [
        {'nombre': 'Valeria', 'telefono': '555-1234'},
        {'nombre': 'Carlos', 'telefono': '555-8745'},
        {'nombre': 'ana', 'telefono': '555-6543'},
        {'nombre': 'Benjamín', 'telefono': '555-9999'},
        {'nombre': 'diana', 'telefono': '555-1111'},
        {'nombre': 'Erick', 'telefono': '555-2222'},
    ]

    print("📋 Agenda original (desordenada):")
    for c in agenda:
        print(f"👤 {c['nombre']} - 📞 {c['telefono']}")

    # Ordenamos usando Insertion Sort
    agenda_ordenada = insertion_sort_contactos(agenda.copy())

    # Mostramos la agenda ordenada
    mostrar_agenda(agenda_ordenada)
