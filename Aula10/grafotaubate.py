import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt

grafo = ox.graph_from_place("Taubaté, São Paulo, Brazil", network_type="drive")

end_origem = "Avenida Independencia, 846, Taubaté, São Paulo, Brazil"
end_destino = "Rua Alfredo Jorge Pulinho Portugal, 181, Taubaté, São Paulo, Brazil"

lat, lon = ox.geocode(end_origem)
origem = ox.distance.nearest_nodes(grafo, X=lon, Y=lat)

lat, lon = ox.geocode(end_destino)
destino = ox.distance.nearest_nodes(grafo, X=lon, Y=lat)

try:
    caminho = nx.shortest_path(grafo, origem, destino, weight="length")
    distancia = nx.shortest_path_length(grafo, origem, destino, weight="length")

    ox.plot_graph_route(grafo, caminho, route_color="blue", route_linewidth=3, node_size=1, bgcolor="lightgreen")

except nx.NetworkXNoPath:
    print("Não há caminho!")