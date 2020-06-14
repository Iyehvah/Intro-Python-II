# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}, {self.description}"
    
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
    
