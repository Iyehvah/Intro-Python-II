# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        if self.inventory:
            result = f'Name: {self.name} is in {self.current_room.name} \n {self.current_room.description} Items are \n'
            for i in self.inventory:
                result += f' item names: {i.name} item description: {i.description} \n'
            return result

        else:
            return f"Name: {self.name} is in {self.current_room.name} \n {self.current_room.description}"

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
    
