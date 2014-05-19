
import random

class Terminal:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 101
        self.level = -1
        self.inventory = {}
    
    def print_status(self, game):
        print(Terminal.OKGREEN + "[{} HP:{} LVL:{}]".format(self.name.ljust(20), self.hp, self.level) + Terminal.END)

class Place:
    def __init__(self, name, description = None):
        self.name = name
        self.description = description
        self.connections = {}

    def visit(self, player):
        pass

    def print_description(self, game):
        print(Terminal.OKBLUE + self.name + Terminal.END)
        
        if self.description:
            print(self.description)
        
        print("Directions: {}".format(", ".join(self.connections.keys())))

    def get_connection(self, name):
        if name in self.connections:
            return self.connections[name]
        else:
            return None
    
    def connect(self, in_word, out_word, other_place):
        self.connections[in_word] = other_place
        if out_word:
            other_place.connections[out_word] = self

class GruePlace(Place):
    def visit(self, player):
        if random.random() > 0.99:
            print("You have been eaten by a Grue.")
            player.hp -= 100
        elif random.random() > 0.95:
            print("You have been attacked by a Grue.")
            player.hp -= 5
        elif random.random() > 0.5:
            print("You hear a faint rustling sound in the shadows...")

start = Place("Outside", """
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.
""")

house = start.connections["east"] = Place("White House", """
It's white. The inside is black.
""")

house.connections["west"] = start

hallway = house.connections["in"] = GruePlace("Hallway", """
It is pitch black.
""")

kitchen = Place("Kitchen")
hallway.connect("left", "back", kitchen)

pool = Place("In-door Swimming Pool")
hallway.connect("right", "back", pool)
