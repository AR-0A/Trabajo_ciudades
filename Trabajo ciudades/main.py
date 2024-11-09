
#Este es el último módulo y sirve para ejecutar el programa

from entrada_grafo import cargar_ciudades
from optimización_rutas import nearest_neighbor, tsp_backtracking
from visualización import graficar_ruta
from reporte import generar_reporte

def main():
    archivo_ciudades = "ciudades.csv"
    grafo = cargar_ciudades(archivo_ciudades)
    
    ciudad_inicio = "A"  # Ciudad inicial para el recorrido
    
    # Algoritmo Nearest Neighbor
    ruta_nn = nearest_neighbor(grafo, ciudad_inicio)
    print("Ruta con Nearest Neighbor:", ruta_nn)
    
    # Algoritmo Backtracking
    ruta_bt, distancia_bt = tsp_backtracking(grafo, ciudad_inicio)
    print("Ruta con Backtracking:", ruta_bt)
    print("Distancia total:", distancia_bt)
    
    # Visualización
    graficar_ruta(grafo, ruta_bt)
    
    # Generar reporte
    generar_reporte(ruta_bt, distancia_bt)

if __name__ == "__main__":
    main()
