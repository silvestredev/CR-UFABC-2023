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

# Definindo as arestas (Interações na quadra de baquete)

# Lebron
G.add_edge("LeBron James", "Bugs Bunny")
G.add_edge("LeBron James", "Daffy Duck")
G.add_edge("LeBron James", "Porky Pig")
G.add_edge("LeBron James", "Lola Bunny")
G.add_edge("LeBron James", "Tweety Bird")
G.add_edge("LeBron James", "Sylvester the Cat")
G.add_edge("LeBron James", "Granny")
G.add_edge("LeBron James", "Marvin the Martian")
G.add_edge("LeBron James", "Elmer Fudd")
G.add_edge("LeBron James", "Yosemite Sam")
G.add_edge("LeBron James", "Wile E. Coyote")
G.add_edge("LeBron James", "Road Runner")
G.add_edge("LeBron James", "Speedy Gonzales")
G.add_edge("LeBron James", "Foghorn Leghorn")
G.add_edge("LeBron James", "The Tazmanian Devil")
G.add_edge("LeBron James", "Gossamer")

# Bugs Buny
G.add_edge("Bugs Bunny", "Daffy Duck")
G.add_edge("Bugs Bunny", "Porky Pig")
G.add_edge("Bugs Bunny", "Lola Bunny")
G.add_edge("Bugs Bunny", "Tweety Bird")
G.add_edge("Bugs Bunny", "Sylvester the Cat")
G.add_edge("Bugs Bunny", "Granny")
G.add_edge("Bugs Bunny", "Marvin the Martian")

# Daffy Duck
G.add_edge("Daffy Duck", "Porky Pig")
G.add_edge("Daffy Duck", "Lola Bunny")
G.add_edge("Daffy Duck", "Tweety Bird")
G.add_edge("Daffy Duck", "Sylvester the Cat")
G.add_edge("Daffy Duck", "Elmer Fudd")
G.add_edge("Daffy Duck", "Yosemite Sam")
G.add_edge("Daffy Duck", "Wile E. Coyote")
G.add_edge("Daffy Duck", "Road Runner")

# Porky Pig  
G.add_edge("Porky Pig", "Lola Bunny")
G.add_edge("Porky Pig", "Tweety Bird")
G.add_edge("Porky Pig", "Sylvester the Cat")
G.add_edge("Porky Pig", "Granny")
G.add_edge("Porky Pig", "Elmer Fudd")
G.add_edge("Porky Pig", "Yosemite Sam")
G.add_edge("Porky Pig", "Wile E. Coyote")
G.add_edge("Porky Pig", "Road Runner")

# Lola Bunny
G.add_edge("Lola Bunny", "Tweety Bird")
G.add_edge("Lola Bunny", "Sylvester the Cat")
G.add_edge("Lola Bunny", "Granny")

# Tweety Bird
G.add_edge("Tweety Bird", "Sylvester the Cat")
G.add_edge("Tweety Bird", "Granny")

# Sylvester the Cat
G.add_edge("Sylvester the Cat", "Granny")

# Marvin the Martian
G.add_edge("Marvin the Martian", "Elmer Fudd")
G.add_edge("Marvin the Martian", "Yosemite Sam")
G.add_edge("Marvin the Martian", "Wile E. Coyote")
G.add_edge("Marvin the Martian", "Road Runner")

# Elmer Fudd
G.add_edge("Elmer Fudd", "Yosemite Sam")
G.add_edge("Elmer Fudd", "Wile E. Coyote")
G.add_edge("Elmer Fudd", "Road Runner")

# Yosemite Sam
G.add_edge("Yosemite Sam", "Wile E. Coyote")
G.add_edge("Yosemite Sam", "Road Runner")

# Wile E. Coyote
G.add_edge("Wile E. Coyote", "Road Runner")

# Speedy Gonzales
G.add_edge("Speedy Gonzales", "Foghorn Leghorn")
G.add_edge("Speedy Gonzales", "The Tazmanian Devil")

# Foghorn Leghorn
G.add_edge("Foghorn Leghorn", "The Tazmanian Devil")

# The Tazmanian Devil
G.add_edge("The Tazmanian Devil", "Gossamer")