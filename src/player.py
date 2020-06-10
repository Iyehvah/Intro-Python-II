# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, player, room):
        self.player = player
        self.room = room
    
    def __str__(self):
        output = f"This is player {self.player}"

    def __repr__(self):
        return f"self.player = {self.player}"

new_player = Player("Bob")

print(new_player)