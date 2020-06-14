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
playerInventory = []
roomInventory = []
player = Player("Robert", room['outside'])
command=''

while command != 'q':

    # GAME DIALOG
    print(f"    Current player:   {player.name}")
    print(f"    Current Room:     {player.current_room.name}, Items: {player.current_room.items}")
    print(f"    Room Description: {player.current_room.description}")

    # PLAYER MOVEMENT AND COMMANDS
    command = input('Please enter a command. Direction: [n] , [s] , [e] , [w]. Actions: [i] , [take] , [get] , [drop] , [q] = quit the game: ')

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

    elif(command == 'pi'):

        playerItemName = input('Enter the name of the item you want to add to your inventory: ')
        playerItemDesc = input('Enter the items description: ')
        playerInventory.append(Item(playerItemName, playerItemDesc))

        print(f'Player Inventory: {playerInventory}')

        player.inventory = playerInventory

        print(player)

    elif( command == 'ri'):
        roomItemName = input('Enter the name of the item you want to remove from your inventory: ')

        roomItemDesc = input('Enter the item decription, you want to add to a room: ')

        roomInventory.append(Item(roomItemName,roomItemDesc))

        print(f'room Inventory: {roomInventory}')

        player.current_room.items = roomInventory        

        print(player.current_room.items)


    
    elif(len(command.split(' '))==2):
        if(command[0].lower() == 'get' or command[0].lower() == 'take'):
    
            print(f'the room inventory is: {player.current_room.items}')
            print(f'the player inventory is: {player.inventory}')

            for item in player.current_room.items:
                if(item.itemName == command[1]):
                    player.current_room.items.remove(item)
                    print(item.on_take(item.itemName))
                    player.inventory.append(item)
                    print(item.on_drop(item.itemName))
        else:
                    print(f'item {command[1]} not found')

    elif(command[0].lower() == 'drop'):
        print(f'the room inventory is: {player.current_room.items}')
        print(f'the player inventory is: {player.inventory}')
        for item in player.inventory:
            if(item.itemName == command[1]):
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    print(item.on_drop(item.itemName))
            else:
                    print(f'item {command[1]} not found')

    elif(command=='i'):
        print(f'Current inventory of the player is: {player.inventory}')

    elif command == 'i':
        if player.inventory != 0:
            print(f'{player.inventory}')
        else: print("Inventory is empty")

    # Q TO QUIT THE GAME
    if command == 'q':
        print("You have exited the game.")
        break
