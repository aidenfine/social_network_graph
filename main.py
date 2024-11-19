from models.graph import Graph
from helpers.helpers import reset_color
from helpers.create_graph import create_graph
from models.Person import Person
from custom_types.types import GenderType

graph = Graph()

person1 = Person("Natalia", 19, GenderType.FEMALE.value)
person2 = Person("Aiden", 20, GenderType.MALE.value)
person3 = Person("Kara", 17, GenderType.FEMALE.value)

person4 = Person("Cindy", 19, GenderType.FEMALE.value)
person5 = Person("Bryce", 20, GenderType.MALE)

graph.add_edge(person1.name, person2.name)
graph.add_edge(person4.name, person5.name)
graph.add_edge(person1.name, person4.name)
graph.add_edge(person3.name, person1.name)

# start = "Foo"
# end = "cindy"

# if graph.find_distance(start, end) != -1:
#     print("Path found")
#     print("All paths ---> ")
#     all_paths = graph.find_all_paths(start, end)
#     for path in all_paths:
#         print(path)
#     print("Best path ---> " + Fore.LIGHTGREEN_EX + str(graph.find_path(start, end)))
#     print("Fastest distance " + Fore.GREEN + str(graph.find_distance(start, end)))
# else:
#     print("uhhhh")

print(graph.find_distance(person1.name, person4.name), "dist")
print(person1.percent_of_being_friends(graph=graph, target=person4), "%")

reset_color()


# create graph

create_graph(graph=graph)
