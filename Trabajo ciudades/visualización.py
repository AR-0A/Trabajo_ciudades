
#Este módulo sirve para visualizar el grafo y las rutas

import networkx as nx
import matplotlib.pyplot as plt

def graficar_ruta(grafo, ruta):
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(10, 8))
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    ruta_edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
    nx.draw_networkx_edges(grafo, pos, edgelist=ruta_edges, edge_color='blue', width=2)
    plt.show()
