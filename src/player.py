# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    
    def __str__(self):
        output = f"Welcome {self.name}"
        i = 1
        for room in self.rooms:
            output += f'\n {i}. {room.name}'
            i += 1
        return output

    def __repr__(self):
        return f"self.name = {self.name} ; self.rooms = {self.rooms}"

new_player = Room("Outside", "Farting around")
