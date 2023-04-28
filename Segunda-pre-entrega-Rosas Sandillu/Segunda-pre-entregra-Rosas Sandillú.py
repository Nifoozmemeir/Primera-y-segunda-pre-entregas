class Cliente:
    def __init__(self, nombre, apellido, edad, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    def __str__(self):
        return f"Hola, soy el cliente {self.nombre} {self.apellido}, tengo {self.edad} años, mis datos son los siguientes:\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nEmail: {self.email}"
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
    def cambiar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"El nuevo teléfono del cliente {self.nombre} {self.apellido} es {self.telefono}")

Juli = Cliente("Julián", "Rosas Sandillú", 24, "Rosario", 1234567890, "NewellsElMasGrandeDelInterior@gmail.com")
Leo = Cliente("Lionel", "Messi", 35, "Paris", 503087405, "MessiTieneLepra@hotmail.com")
King = Cliente("LeBron", "James", 38, "Los Angeles", 30405689, "LeBronJamesGOAT@yahoo.com")

print(Juli)
print(Leo.imprimir_info())
print(King.cambiar_telefono(123789021))
