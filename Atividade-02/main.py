import networkx as nx
import matplotlib.pyplot as plt

# Lista de personagens (vértices)
characters = ["LeBron James", "Bugs Bunny", "Daffy Duck", "Porky Pig", "Lola Bunny",
               "Tweety Bird", "Sylvester the Cat", "Granny", "Marvin the Martian",
               "Elmer Fudd", "Yosemite Sam", "Wile E. Coyote", "Road Runner",
               "Speedy Gonzales", "Foghorn Leghorn", "The Tazmanian Devil",
               "Gossamer", "The Monstars", "Michael Jordan", "Bill Murray",
               "Don Cheadle"]

# Criando grafo
G = nx.Graph()
 
# Adicionando vértices
for char in characters:
    G.add_node(char)

# Definindo as arestas
