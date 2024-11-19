from models.Person import Person

"""
to be honest this doesnt need to be used idk why I included this

"""


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, person: Person):
        """
        Add a person to the network.
        """
        self.people[person.name] = person

    def find_person(self, name: str):
        """
        Find a person by name.
        """
        return self.people.get(name)

    def add_friendship(self, name1: str, name2: str):
        """
        Create a friendship between two people.
        """
        person1 = self.find_person(name1)
        person2 = self.find_person(name2)

        if person1 and person2:
            person1.add_friend(person2)

    def remove_friendship(self, name1: str, name2: str):
        """
        Remove a friendship between two people.
        """
        person1 = self.find_person(name1)
        person2 = self.find_person(name2)

        if person1 and person2:
            person1.remove_friend(person2)

    def get_mutual_friends(self, name1: str, name2: str):
        """
        Get mutual friends between two people.
        """
        person1 = self.find_person(name1)
        person2 = self.find_person(name2)

        if person1 and person2:
            return list(person1.friends & person2.friends)

        return []

    def __repr__(self):
        return f"SocialNetwork(people={list(self.people.values())})"
