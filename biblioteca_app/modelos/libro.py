# libro.py
# Define la clase Libro

class Libro:
    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"
