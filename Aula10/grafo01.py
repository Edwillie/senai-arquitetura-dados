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
# G.add_edge("C","D", peso=5)

print("Nós Disponíveis", list(G.nodes))

origem = input("Digite o vertice de origem: ").strip().upper()
destino = input("Digite o vertice de destino: ").strip().upper()

if (origem not in G.nodes) or (destino not in G.nodes):
    print("Não há origem ou destino")
else:
    try:
        caminho = nx.shortest_path(G, source=origem, target=destino, weight='peso')
        custo = nx.shortest_path_length(G, source=origem, target=destino, weight='peso')

        print("Caminho mínimo aplicado.")
        print("->".join(caminho))
        print("Custo Total ", custo)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, "peso")

        plt.figure(figsize=(8,6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=14, font_weight=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        caminho_minimo = list(zip(caminho[:-1], caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=caminho_minimo, edge_color='red', width=4)

        plt.axis('off')
        plt.show()
    except nx.NetworkXNoPath:
        print("Não existe caminho!")

