
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

class Bag:
    def __init__(self):
        pass
    
    def print_description(self):
        pass
    
    def act(self, game):
        inventory = game.player.inventory
        
        if len(inventory) == 0:
            print("Your bag is empty.")
        else:
            for item in inventory.values():
                print("You have a {}".format(item.name))

class Place:
    def __init__(self, name, description = None):
        self.name = name
        self.description = description
        self.connections = {}
        self.actions = {"inventory": Bag()}

    def visit(self, player):
        pass

    def print_description(self, game):
        print(Terminal.OKBLUE + self.name + Terminal.END)
        
        if self.description:
            print(self.description)
        
        for action in self.actions.values():
            action.print_description()
        
        print()
        
        if len(self.connections) > 0:
            print("You can go: {}".format(", ".join(self.connections.keys())))
        
        if len(self.actions) > 0:
            print("You can do: {}".format(", ".join(self.actions.keys())))

    def get_connection(self, name):
        if name in self.connections:
            return self.connections[name]
        else:
            return None
    
    def get_action(self, name):
        if name in self.actions:
            return self.actions[name]
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

class Mailbox:
    def __init__(self):
        self.opened = False
        self.fire = False
    
    def print_description(self):
        if self.opened:
            print("There is a small mailbox and it is opened.")
        elif self.fire:
            print("There is a small fire where the mailbox used to be.")
        else:
            print("There is a small mailbox here.")
    
    def act(self, game):
        if self.opened:
            if random.random() > 0.97:
                print("You try to open the mailbox, but it catches on fire!")
                game.player.hp -= 20
            else:
                print("The mailbox is already open.")
        else:
            print("You open the mailbox and find a level up.")
            game.player.level += 1
            self.opened = True

class Item:
    def __init__(self, name):
        self.name = name
    
    def print_description(self):
        print("You see a {}".format(self.name))
    
    def act(self, game):
        print("You take the {}".format(self.name))
        game.player.inventory[self.name] = self
    
class RubberChicken(Item):
    def __init__(self):
        super().__init__("Rubber Chicken")

start = Place("Outside", """
You are standing in an open field west of a white house, with a boarded front door.
""")

start.actions["mailbox"] = Mailbox()

house = Place("White House", """
It's white. The inside is black.
""")

start.connect("east", "west", house)

hallway = GruePlace("Hallway", """
It is pitch black.
""")

house.connect("in", "out", hallway)

kitchen = Place("Kitchen")
hallway.connect("left", "back", kitchen)

pool = Place("In-door Swimming Pool")
pool.actions["inspect"] = RubberChicken()

hallway.connect("right", "back", pool)
