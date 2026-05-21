class Client:
    def __init__(self, id, nombre, apellido, categoria, estado, creacion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.categoria = categoria
        self.estado = estado
        self.creacion = creacion

    def guardar(self):
        return 'guardado'
    
    def actualizar(self):
        return ''

    def eliminar(self):
        return ''
    

class Prestamo:
    def __init__(self, id, tipo, estado, creacion):
        self.id = id
        self.tipo = tipo
        self.estado = estado
        self.creacion = creacion

    def guardar(self):
        return 'guardado'
    
    def actualizar(self):
        return ''

    def eliminar(self):
        return ''