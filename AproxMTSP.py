import random
import numpy as np

#Clases paraa hacer graficas

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


# Variables globales

FILE_NAME = "prueba1.txt"
#FILE_NAME = "prueba2.txt"

#Abrimos el archivo
file = open(FILE_NAME)

#La primera linea la guardamos para trabajarla despues
strVertices = file.readline()
strVertices = strVertices[:-1]

#Llenamos las aristas con tuplas que representan las aristas
aristas = []
linea = file.readline()
while (linea != ''):
    aristas.append((linea[0],linea[2],int(linea[4:])))
    linea = file.readline()

#Trabajamos str Vertices
vertices = strVertices.split(',')

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end='\t')  # '\t' agrega un tabulador entre elementos
        print()  # Nueva línea después de cada fila



#creamos matriz de pesos
matrizPesos = np.zeros((len(vertices),len(vertices)))
for i in range(len(vertices)):
    for j in range(len(vertices)):
        if(i==j):
            matrizPesos[i][j] = 0
        else:
            for arista in aristas:
                if(arista[0] == vertices[i] and arista[1] == vertices[j]):
                    matrizPesos[i][j] = arista[2]
                    break
                elif(arista[1] == vertices[i] and arista[0] == vertices[j]):
                    matrizPesos[i][j] = arista[2]
                    break

# funciona imprimir la matriz
#imprimir_matriz(matrizPesos)