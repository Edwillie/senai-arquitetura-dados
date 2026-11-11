import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #criar o grafo
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

G.add_edge("A","B", peso=10) #Crio Aresta
G.add_edge("A","C", peso=20)
G.add_edge("B","C", peso=35)
G.add_edge("C","D", peso=5)

print("Nós Disponíveis", list(G.nodes))

origem = input("Digite o vertice de origem: ").strip().upper()
destino = input("Digite o vertice de destino: ").strip().upper()

arestas = list(nx.dfs_edges(G, source=origem))
visitados = [origem] + [v for u,v in arestas]

print("Visitados: ", visitados)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="purple", node_size=500, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=arestas, edge_color="red", width=3)

edge_labels = nx.get_edge_attributes(G, "peso")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()