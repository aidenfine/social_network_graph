import string
from models.graph import Graph
import random
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt
import networkx as nx
from helpers.helpers import reset_color
from helpers.create_graph import create_graph

graph = Graph()

# Create a social network graph
graph.add_edge("Bob", "Charlie", "David")
graph.add_edge("Alice", "Foo", "Bob")
graph.add_edge("Aiden", "Bob")
graph.add_edge("Natalia", "Aiden")
graph.add_edge("Kara", "Myra", "lucy", "Natalia")
graph.add_edge("Natalia", "Kerira")


start = "Aiden"
end = "David"

if graph.find_distance(start, end) != -1:
    print('Path found')
    print('All paths ---> ')
    all_paths = graph.find_all_paths(start, end)
    for path in all_paths:
        print(path)
    print('Best path ---> ' + Fore.LIGHTGREEN_EX + str(graph.find_path(start, end)))
    print('Fastest distance ' + Fore.GREEN + str(graph.find_distance(start, end)))
else:
    print('uhhhh')

reset_color()


# create graph

create_graph(graph=graph)


