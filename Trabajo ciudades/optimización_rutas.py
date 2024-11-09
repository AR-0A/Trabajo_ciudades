
#Este módulo va a ser usado para hacer algoritmo de optimización (TSP)

import networkx as nx
import itertools

def nearest_neighbor(grafo, ciudad_inicio): #Busca la ciudad cercano no visitada y se mueve hacia ella, repiéndolo hasta visitar todas
    camino = [ciudad_inicio]
    nodo_actual = ciudad_inicio
    nodos_por_visitar = set(grafo.nodes) - {ciudad_inicio}
    while nodos_por_visitar:
        ciudad_cercana = min(nodos_por_visitar, key=lambda x: grafo[nodo_actual][x]['weight'])
        camino.append(ciudad_cercana)
        nodo_actual = ciudad_cercana
        nodos_por_visitar.remove(ciudad_cercana)
    return camino + [ciudad_inicio]

def tsp_backtracking(grafo, ciudad_inicio):
    nodos = list(grafo.nodes)
    nodos.remove(ciudad_inicio)
    rutas_posibles = itertools.permutations(nodos)
    mejor_camino = None
    menor_distancia = float('inf')
    for ruta in rutas_posibles:
        distancia_actual = 0
        camino = [ciudad_inicio] + list(ruta) + [ciudad_inicio]
        for i in range(len(camino) - 1):
            distancia_actual += grafo[camino[i]][camino[i + 1]]['weight']
        if distancia_actual < menor_distancia:
            menor_distancia = distancia_actual
            mejor_camino = camino
    return mejor_camino, menor_distancia

