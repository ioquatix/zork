#!/usr/bin/env python

import story

print("Welcome to ZORK!")

class Game:
    def __init__(self, player, start):
        self.player = player
        self.location = start
        self.running = True
    
    def once(self):
        self.location.print_description(self)
        
        user_input = input("> ")
        
        next_location = self.location.get_connection(user_input)
        
        if next_location:
            self.location = next_location
        else:
            print("You crash into an invisible wall, you can't go {}".format(user_input))

game = Game(story.Player("Shinji"), story.start)

while game.running:
    game.once()
