from models.graph import Graph


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        # self.friends = friends

    def get_linked_nodes(self, graph: Graph):
        """
        Linked Nodes aka "friends"
        """
        return graph.edges(self.name)

    def get_person(self):
        """
        simply return the person
        """
        return {"name": self.name, "age": self.age, "gender": self.gender}

    def get_total_friends(self, graph: Graph, path=None) -> int:
        if path is None:
            path = []
        graph = graph._graph_dict
        path = path + [self.name]

    def percent_of_being_friends(self, graph: Graph, target: "Person") -> float:
        distance = graph.find_distance(self.name, target.name)
        if self.gender == target.gender:
            gender_weight = 1 - (1 / 2)
        else:
            gender_weight = 1 - (1 / 3)

        age_diff = self.age - target.age
        if age_diff < 0:
            age_diff = age_diff * -1

        distance_weight = 0
        if distance <= 2:
            distance_weight = 1 - (2 / 3)
        elif distance <= 4:
            distance_weight = 1 - (4 / 10)
        elif distance <= 8:
            distance_weight = 1 - (3 / 16)
        elif distance <= 14:
            distance_weight = 1 - (2 / 16)
        else:
            distance_weight = 1 - (2 / 30)

        age_weight = 1 - (age_diff / 10)
        print(distance_weight, gender_weight, age_weight)

        return round((distance_weight + gender_weight) * 100, 4)
