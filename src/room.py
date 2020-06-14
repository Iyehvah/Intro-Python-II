# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        if self.items:
            result = f'This is {self.name} has {self.description}. Items are \n'

            for i in self.items:
                result += f' Item name: {i.name} Item Description: {i.description} \n'
            return result
        else:
            return f'This is {self.name} has {self.description}'
    
    def list_items(self):
        print(self.items)

    def add_item(self, item):
        self.items.append(item)
        return True
    
    def remove_item_from_room(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return False
    
