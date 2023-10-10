import networkx as nx
import matplotlib.pyplot as plt

# Criando grafo vázio
G = nx.Graph()

# Adicionando vértices
G.add_node("v1")
G.add_node("v2")
G.add_node("v3")
G.add_node("v4")

# Adicionando arestas
G.add_edge("v1", "v2")
G.add_edge("v2", "v3")
G.add_edge("v3", "v4")
G.add_edge("v4", "v1")

# Listando os vértices
print("Lista de vértices")
print(G.nodes())
input()

# Percorre o conjunto de vértices
print("Percorrendo os vértices")
for v in G.nodes():
    print(v)
input()

# Lista as arestas
print("Lista de arestas")
print(G.edges())
input()

# Percorre o conjunto de arestas
print("Percorrendo as arestas")
for a in G.edges():
    print(a)
input()

# Mostra a lista de graus
print("Lista de graus de G")
print(G.degree())
input()

# Acessa o grau do vértice v2
print("O grau do vértice V2 é %d" %G.degree()["v2"])
print()

#...