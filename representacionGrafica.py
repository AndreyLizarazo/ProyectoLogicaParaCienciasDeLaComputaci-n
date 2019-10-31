import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node(1, pos = (20,60))
G.add_node(2, pos = (40,60))
G.add_node(3, pos =(60,60))

G.add_node(4,pos =(30,50))
G.add_node(5, pos =(40,50))
G.add_node(6,pos=(50,50))

G.add_node(7,pos=(20,40))
G.add_node(8,pos=(30,40))
G.add_node(9,pos=(50,40))
G.add_node(10,pos=(60,40))

G.add_node(11,pos=(30,30))
G.add_node(12,pos=(40,30))
G.add_node(13,pos=(50,30))

G.add_node(14,pos=(20,20))
G.add_node(15,pos=(40,20))
G.add_node(16,pos=(60,20))
#grafo
G.add_edge(1,2)
G.add_edge(2,5)
G.add_edge(2,3)
G.add_edge(3,10)
G.add_edge(5,6)
G.add_edge(5,4)
G.add_edge(7,8)
G.add_edge(9,6)
G.add_edge(9,10)
G.add_edge(8,11)
G.add_edge(8,4)
G.add_edge(10,16)
G.add_edge(11,12)
G.add_edge(12,13)
G.add_edge(12,15)
G.add_edge(13,9)
G.add_edge(16,15)
G.add_edge(15,16)
G.add_edge(15,14)
G.add_edge(14,7)
G.add_edge(7,1)

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels = True)
plt.show()
