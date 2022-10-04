def main():
    
    # Game Name, Goodbye
    game_name = "Welcome to Hannah's Haunted House!"
    goodbye = "Thank you for playing, goodbye!"

    # All Rooms
    foyer = "This is an old foyer in front of a locked door. The lights are dim."
    hallway = "The hallway is long, and lacks decorations. The lights are bright. Doors line each wall."
    bathroom = "The bathroom is lit by a dim candle. There are cobwebs in the corner."
    bedroom = "The bedroom is a tight space with a queen size bed. The only light is coming from the hallway. There is a locked window."
    nursery = "The nursery is completely empty. There is a single floorboard coming up. The window is locked."
    home_office = "The home office has a small desk and a rolling chair. The window is locked."
    living_room = "The living room has a large old couch, and a TV playing at a low volume. The lights are dim. There are two locked windows."
    kitchen = "The kitchen has a stove, oven, fridge, and table with two chairs. The only light is coming from the hallway. The window is locked."
    storage_room = "The storage room has 6 shelves, but only one box on them. The only light is coming from the hallway. There are no windows."
    guest_room = "The guest room has a single bed and a nightstand. The lights are dim. There is no window."
    home_gym = "The home gym only contains a treadmill and set of weights. The lights are dim. The window is locked."
    room_counter = 0

    # Room Details
    foyer_details = "When you look closer, you see a large rug in front of the door."
    hallway_details = "On the left side of the hallway, there is a large painting of a fire."
    bathroom_details = "When you look closer, you see a rusted sink and a shower with a ripped curtain."
    bedroom_details = "When you look under the bed, there is a small shoebox and a key."
    nursery_details = "When you look under the floorboard, there is a pacifier."
    home_office_details = "When you open the desk, there is a notepad and pen."
    living_room_details =  "When you look closer at the TV, it is playing breaking news. The screen has cracks so you cannot see what is playing, and the volume is too quiet to hear it."
    kitchen_details = "When you open the fridge, there is a water bottle filled with a liquid."
    storage_room_details = "Inside the box, there is an old photo album."
    guest_room_details = "When you look inside the nightstand, there is a small box."
    home_gym_details = "Underneath the treadmill, there is a small box."

    #This starts with an intro statement, and then goes through each room by having the user press and key to continue. After each room detail is presented, there is a +1 to the room counter. At the end, the number of rooms visited and a goodbye message is printed.
    print(game_name)
    username = input("What's your name? ")
    print(f"Hello {username}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    begin = input("Press enter to begin: ")
    while True:
        print(foyer)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(hallway)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(bathroom)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(bedroom)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(nursery)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(home_office)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(living_room)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(kitchen)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(storage_room)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(guest_room)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    while True:
        print(home_gym)
        cont1 = str.lower(input("What would you like to do? "))
        if cont1 == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            input("What would you like to do? ")
        elif cont1 == "quit":
            break
        elif cont1 == "north" or cont1 == "south" or cont1 == "east" or cont1 == "west":
            room_counter += 1
            break
        else:
            print("That command is invalid.")
    
    print("You visited", room_counter, "rooms.")
    print(goodbye)
            
main()