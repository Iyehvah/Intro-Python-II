# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        output = f"Welcome {self.name}. Current Location: {self.current_room}. Current Items: {self.inventory}"
        i = 1
        for room in self.current_room:
            output += f'\n {i}. {room.name}'
            i += 1
        return output

    def __repr__(self):
        return f"self.name = {self.name} ; self.rooms = {self.current_room}"
    
    def update_room(self, room):
        self.current_room = room.name

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            item.on_drop()
            return item
        else:
            return false

    def list_inventory(self):
        print(self.inventory)
    
