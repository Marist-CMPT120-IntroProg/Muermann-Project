# Game Name
game_name = "Welcome to Hannah's Haunted House!"

room_names = ["foyer", "bathroom", "bedroom", "nursery", "home office", "living room", "kitchen", "storage room", "guest room", "home gym"]
direction_options = ["north", "east", "south", "west"]

rooms = [ 
    {"name": "foyer",
    "summary":"This is an old foyer in front of a locked door. The lights are dim.",
    "details":"When you look closer, you see a large rug in front of the door.",
    "was_visited":False},

    {"name":"bathroom",
    "summary":"The bathroom is lit by a dim candle. There are cobwebs in the corner.",
    "details":"When you look closer, you see a rusted sink and a shower with a ripped curtain.",
    "was_visited":False},

    {"name":"bedroom",
    "summary":"The bedroom is a tight space with a queen size bed. The only light is coming from the hallway. There is a locked window.",
    "details":"When you look under the bed, there is a small shoebox and a key.",
    "was_visited":False},

    {"name":"nursery",
    "summary":"The nursery is completely empty. There is a single floorboard coming up. The window is locked.",
    "details":"When you look under the floorboard, there is a pacifier.",
    "was_visited":False},

    {"name":"home office",
    "summary":"The home office has a small desk and a rolling chair. The window is locked.",
    "details":"When you open the desk, there is a notepad and pen.",
    "was_visited":False},

    {"name":"living room",
    "summary":"The living room has a large old couch, and a TV playing at a low volume. The lights are dim. There are two locked windows.",
    "details":"When you look closer at the TV, it is playing breaking news. The screen has cracks so you cannot see what is playing, and the volume is too quiet to hear it.",
    "was_visited":False},

    {"name":"kitchen",
    "summary": "The kitchen has a stove, oven, fridge, and table with two chairs. The only light is coming from the hallway. The window is locked.",
    "details":"When you open the fridge, there is a water bottle filled with a liquid.",
    "was_visited":False},

    {"name":"storage room",
    "summary": "The storage room has 6 shelves, but only one box on them. The only light is coming from the hallway. There are no windows.",
    "details": "Inside the box, there is an old photo album.",
    "was_visited":False},

    {"name":"guest room",
    "summary": "The guest room has a single bed and a nightstand. The lights are dim. There is no window.",
    "details": "Inside the box, there is an old photo album.",
    "was_visited":False},

    {"name":"home gym",
    "summary": "The home gym contains a treadmill and set of weights. The lights are dim. The window is locked.",
    "details": "Underneath the treadmill, there is a small box.",
    "was_visited":False}]

game_map = [["living room", None, None, None],
            ["bedroom", "living room", None, None],
            ["nursery", None, "bathroom", None],
            ["home office", None, "bedroom", None],
            [None, None, "nursery", None],
            ["kitchen", "home gym", "foyer", "bathroom"],
            [None, None, "living room", None],
            [None, None, "guest room", None],
            ["storage room", None, "home gym", None],
            ["guest room", None, None, "living room"]]

room_counter = 0

def move(current_room, desired_move):
    global room_counter
    row_num = room_names.index(current_room)
    column_num = direction_options.index(desired_move)
    new_room = game_map[row_num][column_num]
    if new_room == None:
        print("You cannot go that way. Try again.")
        return current_room
    else:
        for room in rooms:
            if room["name"] == new_room:
                current_room = new_room
                print(room["summary"])
                room_counter += 1
                return current_room


# Main Game
def main():
    print(game_name)
    username = input("What's your name? ")
    print(f"Hello {username}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    begin = input("Press enter to begin: ")
    current_room = rooms[0]["name"]
    print(rooms[0]["summary"])
    global room_counter
    room_counter += 1
    while True:
        desired_move = str.lower(input("What would you like to do? "))
        if desired_move == "help":
            print("These are the valid commands: Help, Quit, North, East, South, West, Examine")
            continue
        elif desired_move == "quit":
            break
        elif desired_move == "examine":
            if current_room == rooms[0]:
                print(rooms[0]["details"])
                continue
            elif current_room == rooms[1]:
                print(rooms[1]["details"])
                continue
            elif current_room == rooms[2]:
                print(rooms[2]["details"])
                continue
            elif current_room == rooms[3]:
                print(rooms[3]["details"])
                continue
            elif current_room == rooms[4]:
                print(rooms[4]["details"])
                continue
            elif current_room == rooms[5]:
                print(rooms[5]["details"])
                continue
            elif current_room == rooms[6]:
                print(rooms[6]["details"])
                continue
            elif current_room == rooms[7]:
                print(rooms[7]["details"])
                continue
            elif current_room == rooms[8]:
                print(rooms[8]["details"])
                continue
            elif current_room == rooms[9]:
                print(rooms[9]["details"])
                continue
            else:
                print("Error")
                continue
        else:
            current_room = move(current_room, desired_move)

            continue


        
        # elif current_room == rooms[0]:
        #     if desired_move == "north":
        #         current_room = rooms[5]
        #         print(rooms[5]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         print("The door to exit the house is locked. You cannot go this way.")
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[5]:
        #     if desired_move == "north":
        #         current_room = rooms[6]
        #         print(rooms[6]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[0]
        #         print(rooms[0]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         current_room = rooms[9]
        #         print(rooms[9]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "west":
        #         current_room = rooms[1]
        #         print(rooms[1]["summary"])
        #         room_counter += 1
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[6]:
        #     if desired_move == "north":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[5]
        #         print(rooms[5]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[1]:
        #     if desired_move == "north":
        #         current_room = rooms[2]
        #         print(rooms[2]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "east":
        #         current_room = rooms[5]
        #         print(rooms[5]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[9]:
        #     if desired_move == "north":
        #         current_room = rooms[8]
        #         print(rooms[8]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         current_room = rooms[5]
        #         print(rooms[5]["summary"])
        #         room_counter += 1
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[2]:
        #     if desired_move == "north":
        #         current_room = rooms[3]
        #         print(rooms[3]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[1]
        #         print(rooms[1]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[8]:
        #     if desired_move == "north":
        #         current_room = rooms[7]
        #         print(rooms[7]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[9]
        #         print(rooms[9]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[3]:
        #     if desired_move == "north":
        #         current_room = rooms[4]
        #         print(rooms[4]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[2]
        #         print(rooms[2]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[7]:
        #     if desired_move == "north":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[8]
        #         print(rooms[8]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue
        # elif current_room == rooms[4]:
        #     if desired_move == "north":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "south":
        #         current_room = rooms[3]
        #         print(rooms[3]["summary"])
        #         room_counter += 1
        #         continue
        #     elif desired_move == "east":
        #         print("There is no door on that side.")
        #         continue
        #     elif desired_move == "west":
        #         print("There is no door on that side.")
        #         continue
        #     else:
        #         print("That command is invalid.")
        #         continue

    print("You visited", room_counter, "rooms.")
    print(f"Thank you for playing, {username}. Goodbye!")
    print("© Hannah Muermann 2022. All rights reserved.")
            
main()