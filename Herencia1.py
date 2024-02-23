# Define una clase base Animal con atributos comunes como nombre y edad. 
# Luego, crea dos clases derivadas, por ejemplo, Mamifero y Ave. 
# Cada clase derivada debe tener al menos un atributo y un método específicos. 
# Finalmente, crea instancias de las clases derivadas y muestra algunas características de cada animal.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Mamifero(Animal):
    def __init__(self, nombre, edad, crianza):
        super().__init__(nombre, edad)
        self.crianza = crianza

    def mostrar_informacion_mamifero(self):
        self.mostrar_informacion()
        print(f"Crianza: {self.crianza}")


class Ave(Animal):
    def __init__(self, nombre, edad, alas):
        super().__init__(nombre, edad)
        self.alas = alas

    def mostrar_informacion_ave(self):
        self.mostrar_informacion()
        print(f"Alas: {self.alas}")



mamifero1 = Mamifero("Vaca", 15, "Lactancia")
ave1 = Ave("Aguila", 5, "Grandes")

print("Información del mamífero:")
mamifero1.mostrar_informacion_mamifero()

print("\nInformación del ave:")
ave1.mostrar_informacion_ave()