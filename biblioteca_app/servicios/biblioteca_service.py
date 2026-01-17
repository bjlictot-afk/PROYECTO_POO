from biblioteca_app.modelos.libro import Libro
from biblioteca_app.modelos.usuario import Usuario

def prestar_libro(usuario: Usuario, libro: Libro):
    if libro.disponible:
        usuario.libros_prestados.append(libro)
        libro.disponible = False
        print(f"El libro '{libro.titulo}' fue prestado a {usuario.nombre}.")
    else:
        print(f"El libro '{libro.titulo}' no está disponible.")

def devolver_libro(usuario: Usuario, libro: Libro):
    if libro in usuario.libros_prestados:
        usuario.libros_prestados.remove(libro)
        libro.disponible = True
        print(f"El libro '{libro.titulo}' fue devuelto por {usuario.nombre}.")
    else:
        print(f"{usuario.nombre} no tiene el libro '{libro.titulo}' prestado.")
