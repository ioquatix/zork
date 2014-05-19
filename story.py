
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 101
        self.level = -1
        self.inventory = {}

class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def print_description(self, game):
        print(self.description)
        
        print("Directions: {}".format(", ".join(self.connections.keys())))

    def get_connection(self, name):
        if name in self.connections:
            return self.connections[name]
        else:
            return None

start = Place("Outside", """
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.
""")

start.connections["east"] = Place("White House", """
It's white. The inside is black.
""")
