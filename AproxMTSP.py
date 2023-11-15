class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

    def agregar_vecino(self, nodo, peso):
        self.vecinos[nodo] = peso

    def __str__(self):
        return f"Nodo {self.nombre}"


class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo):
        self.nodos[nodo.nombre] = nodo

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1.nombre in self.nodos and nodo2.nombre in self.nodos:
            nodo1.agregar_vecino(nodo2, peso)
            nodo2.agregar_vecino(nodo1, peso)
        else:
            print("Uno o ambos nodos no existen en el grafo.")

    def __str__(self):
        resultado = "Grafo:\n"
        for nodo in self.nodos.values():
            resultado += f"{nodo}\n"
            for vecino, peso in nodo.vecinos.items():
                resultado += f"  --> {vecino} (Peso: {peso})\n"
        return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Crear nodos
    nodo1 = Nodo("A")
    nodo2 = Nodo("B")
    nodo3 = Nodo("C")

    # Crear grafo
    grafo = Grafo()

    # Agregar nodos al grafo
    grafo.agregar_nodo(nodo1)
    grafo.agregar_nodo(nodo2)
    grafo.agregar_nodo(nodo3)

    # Agregar aristas con pesos
    grafo.agregar_arista(nodo1, nodo2, 3)
    grafo.agregar_arista(nodo2, nodo3, 5)
    grafo.agregar_arista(nodo1, nodo3, 2)

    # Imprimir el grafo
    print(grafo)
