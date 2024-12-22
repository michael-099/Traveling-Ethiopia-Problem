import networkx as nx
import matplotlib.pyplot as plt

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = [
    ('Addis Ababa', 'Bahir Dar', 510),
    ('Addis Ababa', 'Hawassa', 275),
    ('Bahir Dar', 'Addis Ababa', 510),
    ('Bahir Dar', 'Gondar', 180),
    ('Gondar', 'Bahir Dar', 180),
    ('Gondar', 'Mekelle', 300),
    ('Hawassa', 'Addis Ababa', 275),
    ('Mekelle', 'Gondar', 300)
]


G = nx.Graph()
G.add_nodes_from(cities)
G.add_weighted_edges_from(roads)

pos = nx.spring_layout(G)  
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]} km' for u, v, d in G.edges(data=True)})

plt.title('City Road Network')
plt.axis('off')
plt.show()
