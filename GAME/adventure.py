def main():
    
    # Game Name
    game_name = "Welcome to Hannah's Haunted House!"

    # All Rooms
    foyer = "This is an old foyer in front of a locked door. The lights are dim."
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

    # Room Names
    foy = "Foyer"
    bat = "Bathroom"
    bed = "Bedroom"
    nur = "Nursery"
    off = "Home Office"
    live = "Living Room"
    kit = "Kitchen"
    stor = "Storage Room"
    guest = "Guest Room"
    gym = "Home Gym"

    # Room Details
    foyer_details = "When you look closer, you see a large rug in front of the door."
    bathroom_details = "When you look closer, you see a rusted sink and a shower with a ripped curtain."
    bedroom_details = "When you look under the bed, there is a small shoebox and a key."
    nursery_details = "When you look under the floorboard, there is a pacifier."
    home_office_details = "When you open the desk, there is a notepad and pen."
    living_room_details =  "When you look closer at the TV, it is playing breaking news. The screen has cracks so you cannot see what is playing, and the volume is too quiet to hear it."
    kitchen_details = "When you open the fridge, there is a water bottle filled with a liquid."
    storage_room_details = "Inside the box, there is an old photo album."
    guest_room_details = "When you look inside the nightstand, there is a small box."
    home_gym_details = "Underneath the treadmill, there is a small box."

    # Main Game
    print(game_name)
    username = input("What's your name? ")
    print(f"Hello {username}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    begin = input("Press enter to begin: ")
    current_room = foy
    print(foyer)
    room_counter += 1

    while True:
        cont = str.lower(input("What would you like to do? "))
        if cont == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West")
            continue
        elif cont == "quit":
            break
        elif current_room == foy:
            if cont == "north":
                current_room = live
                print(living_room)
                room_counter += 1
                continue
            elif cont == "south":
                print("The door to exit the house is locked. You cannot go this way.")
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == live:
            if cont == "north":
                current_room = kit
                print(kitchen)
                room_counter += 1
                continue
            elif cont == "south":
                current_room = foy
                print(foyer)
                room_counter += 1
                continue
            elif cont == "east":
                current_room = gym
                print(home_gym)
                room_counter += 1
                continue
            elif cont == "west":
                current_room = bat
                print(bathroom)
                room_counter += 1
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == kit:
            if cont == "north":
                print("There is no door on that side.")
                continue
            elif cont == "south":
                current_room = live
                print(living_room)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == bat:
            if cont == "north":
                current_room = bed
                print(bedroom)
                room_counter += 1
                continue
            elif cont == "south":
                print("There is no door on that side.")
                continue
            elif cont == "east":
                current_room = live
                print(living_room)
                room_counter += 1
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == gym:
            if cont == "north":
                current_room = guest
                print(guest_room)
                room_counter += 1
                continue
            elif cont == "south":
                print("There is no door on that side.")
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                current_room = live
                print(living_room)
                room_counter += 1
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == bed:
            if cont == "north":
                current_room = nur
                print(nursery)
                room_counter += 1
                continue
            elif cont == "south":
                current_room = bat
                print(bathroom)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == guest:
            if cont == "north":
                current_room = stor
                print(storage_room)
                room_counter += 1
                continue
            elif cont == "south":
                current_room = gym
                print(home_gym)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == nur:
            if cont == "north":
                current_room = off
                print(home_office)
                room_counter += 1
                continue
            elif cont == "south":
                current_room = bed
                print(bedroom)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == stor:
            if cont == "north":
                print("There is no door on that side.")
                continue
            elif cont == "south":
                current_room = guest
                print(guest_room)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue
        elif current_room == off:
            if cont == "north":
                print("There is no door on that side.")
                continue
            elif cont == "south":
                current_room = nur
                print(nursery)
                room_counter += 1
                continue
            elif cont == "east":
                print("There is no door on that side.")
                continue
            elif cont == "west":
                print("There is no door on that side.")
                continue
            else:
                print("That command is invalid.")
                continue

    print("You visited", room_counter, "rooms.")
    print(f"Thank you for playing, {username}. Goodbye!")
    print("© Hannah Muermann 2022. All rights reserved.")
            
main()