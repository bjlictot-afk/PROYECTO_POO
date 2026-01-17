# main.py
# Archivo principal para probar la biblioteca

from biblioteca_app.modelos.libro import Libro
from biblioteca_app.modelos.usuario import Usuario
from biblioteca_app.servicios.biblioteca_service import prestar_libro, devolver_libro

def main():
    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Crear usuarios
    usuario1 = Usuario("Belgica", 1)
    usuario2 = Usuario("Juan", 2)

    # Mostrar estado inicial
    print("\n--- Estado inicial ---")
    print(libro1)
    print(libro2)
    print(usuario1)
    print(usuario2)

    # Prestar libros
    print("\n--- Prestamos ---")
    prestar_libro(usuario1, libro1)
    prestar_libro(usuario2, libro2)
    prestar_libro(usuario2, libro1)  # Este ya está prestado

    # Mostrar estado después de los préstamos
    print("\n--- Estado después de préstamos ---")
    print(libro1)
    print(libro2)
    print(usuario1)
    print(usuario2)

    # Devolver libros
    print("\n--- Devoluciones ---")
    devolver_libro(usuario1, libro1)
    devolver_libro(usuario2, libro2)

    # Estado final
    print("\n--- Estado final ---")
    print(libro1)
    print(libro2)
    print(usuario1)
    print(usuario2)

if __name__ == "__main__":
    main()
