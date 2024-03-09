
import matplotlib.pyplot as plt
import networkx as nx


def create_graph(graph):
    G = nx.Graph()
    for person in graph.all_vertices():
        G.add_node(person)
    for person in graph.all_vertices():
        for friend in graph.edges(person):
            G.add_edge(person, friend)

    # Visualize the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='grey', node_size=1000, font_size=9, font_color="white", arrowstyle="fancy", arrowsize=12, edge_color="blue",)
    plt.title('Social Network Graph')
    plt.show()


