from room import Room
from player import Player


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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Robert", room['outside'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f"    Current player:   {player.name}")
    print(f"    Current Room:     {player.rooms.name}")
    print("")
    print(f"    Room Description: {player.rooms.description}")
    print("")

    command = input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
    moves = ['n', 's', 'e', 'w']


    if command in moves:

        if command == 'n':
            #fix this to check the room in the chosen direction
            if player.rooms.n_to != None:
                player.rooms = player.rooms.n_to

            else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        elif command  == 's':
            if player.rooms.s_to != None:
                player.rooms = player.rooms.s_to
            else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
        elif command == 'e':
            if player.rooms.e_to != None:
                player.rooms = player.rooms.e_to
            else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
        elif command == 'w':
            if player.rooms.w_to != None:
                player.rooms = player.rooms.w_to
            else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')

    if command == 'q':
        print("You have exited the game.")
        break
