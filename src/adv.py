from room import Room
from player import Player
from item import Item



# Declare all items
# Creating items
torch = Item("Torch", "Old forgotten torch lay on the ground. May light your travels.")
sword = Item('Sword', 'Quite an old dull sword but it will do the trick')
shield = Item("Shield", "A worn down shield may block a couple attacks?")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#Puting items into rooms

room['outside'].add_item(torch)
room['foyer'].add_item(sword)
room['overlook'].add_item(shield)



#
# Main
#



# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Make a new player object that is currently in the 'outside' room.
player = Player("Robert", room['outside'])

while True:

    # GAME DIALOG
    print(f"    Current player:   {player.name}")
    print(f"    Current Room:     {player.current_room.name}, Items: {player.current_room.items}")
    print(f"    Room Description: {player.current_room.description}")





    # PLAYER MOVEMENT AND COMMANDS
    command = input('Press [n], [s], [e], [w] to move. Press [i] for inventory. Type "take" or "get" to pick up items. Type "drop" to remove an item from your inventory and place it back into the room. Press [q] to quit: ')
    moves = ['n', 's', 'e', 'w', 'i', "take", "get", "drop"]

    if command == 'n':
            #fix this to check the room in the chosen direction
        if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to

        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
    elif command  == 's':
        if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
    elif command == 'e':
        if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
    elif command == 'w':
        if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
    elif command == 'i':
        if player.inventory != 0:
            print(f'{player.inventory}')
        else: print("Inventory is empty")

    elif command == 'take' or command == 'get':
        for item in player.current_room.items:
            if item.name in player.current_room.items:
                new_player_item = player.current_room.remove_item(item.name)
                player.add_item(new_player_item)
            else:
                print("Item does not exist")

    # Q TO QUIT THE GAME
    if command == 'q':
        print("You have exited the game.")
        break
