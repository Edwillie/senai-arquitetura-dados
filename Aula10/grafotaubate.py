import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt

grafo = ox.graph_from_place("Taubaté, São Paulo, Brazil", network_type="walk")

origem = list(grafo.nodes())
destino = 0

print(origem)