#!/usr/bin/env python

import story

print("Welcome to ZORK!")

class Game:
    def __init__(self, player, start):
        self.player = player
        self.location = start
        self.running = True
    
    def once(self):
        self.player.print_status(self)
        
        if self.player.hp <= 1:
            print("You died :(")
            self.running = False
            return
        
        self.location.visit(self.player)
        self.location.print_description(self)
        
        user_input = input("> ")
        
        if user_input == "exit":
            self.running = False
            return
        
        next_location = self.location.get_connection(user_input)
        
        if next_location:
            self.location = next_location
            print("You travel {} to the {}".format(user_input, self.location.name))
        else:
            action_function = self.location.get_action(user_input)
            
            if action_function:
                action_function.act(game)
            else:
                print("Unfortunately, {} is not a possibility!".format(user_input))

        print()
        input("Press enter to continue...")
        print()

name = input("What is your name, humble adventurer? ")

game = Game(story.Player(name), story.start)

while game.running:
    game.once()
