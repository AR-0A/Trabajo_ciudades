
#Este módulo va a estar destinado a manejar la entrada y crear el grafo

import networkx as nx
import csv

def cargar_ciudades():
    archivo = "ciudades.csv"  # Nombre del archivo a cargar
    grafo = nx.Graph()
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Omitir la primera fila si contiene encabezados
        for fila in reader:
            ciudad1, ciudad2, distancia = fila
            grafo.add_edge(ciudad1, ciudad2, weight=float(distancia))
    return grafo

