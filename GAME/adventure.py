def main():
    
    # Introduction + Goodbye
    intro = "Welcome to Hannah's Haunted House! You will travel through several rooms and collect many objects in order to escape this spooky home."
    goodbye = "Thank you for playing, goodbye!"

    # All rooms
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

    # This starts with an intro statement, and then goes through each room by having the user press and key to continue. At the end, a goodbye message is printed.
    print(intro)
    begin = input("Press any any to begin: ")
    print(foyer)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(hallway)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(bathroom)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(bedroom)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(nursery)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(home_office)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(living_room)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(kitchen)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(storage_room)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(guest_room)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print(home_gym)
    cont = input("Press any key to continue: ")
    room_counter += 1
    print("You visited", room_counter, "rooms.")
    print(goodbye)

main()