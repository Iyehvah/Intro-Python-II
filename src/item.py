class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'{self.name}, {self.description}'

    def on_take(self, name):
        return f'Item {self.name} was picked up'

    def on_drop(self):
        return (f' You have dropped {self.name}')

    