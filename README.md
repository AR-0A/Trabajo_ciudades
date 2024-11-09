# Optimización de Entregas en una Red de Ciudades

Este proyecto implementa un sistema para optimizar las rutas de entrega en una red de ciudades conectadas por carreteras. El sistema utiliza técnicas basadas en el Problema del Viajante (TSP) para encontrar la ruta más corta y eficiente para un camión de entregas que debe visitar múltiples ciudades.

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un programa que modele las ciudades y carreteras como un grafo ponderado y utilice algoritmos de optimización de rutas. Los métodos incluyen el Algoritmo de Vecino Más Cercano (Nearest Neighbor) para una solución rápida y Backtracking para encontrar una solución óptima. 

El sistema realiza las siguientes funciones:
- Cargar datos de ciudades y carreteras desde un archivo CSV y construir un grafo ponderado.
- Ejecutar algoritmos de optimización de rutas (Nearest Neighbor y Backtracking).
- Visualizar gráficamente la ruta más corta en el grafo.
- Generar un informe en formato PDF con la ruta más corta y las métricas de eficiencia.

## Estructura del Proyecto

- **entrada_grafo.py**: Módulo de entrada que carga datos de ciudades y carreteras desde un archivo CSV y construye el grafo.
- **optimización_rutas.py**: Contiene las funciones para optimizar rutas usando Nearest Neighbor y Backtracking.
- **visualización.py**: Muestra gráficamente el recorrido en el grafo.
- **reporte.py**: Genera un informe en PDF con la ruta más corta y el tiempo de ejecución de cada método.
- **main.py**: Script principal que coordina la ejecución de todos los módulos.

## Requisitos

Este proyecto utiliza las siguientes bibliotecas de Python:

- `networkx`: Para la modelización y manipulación del grafo.
- `matplotlib`: Para visualizar las rutas en el grafo.
- `fpdf`: Para la generación del informe en PDF.
- `pandas`: Para leer datos desde el archivo CSV de forma más sencilla.

### Instalación de Dependencias

Puedes instalar todas las dependencias con el siguiente comando:

```bash
pip install networkx matplotlib fpdf pandas
