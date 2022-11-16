# Hannah's Haunted House!
# - By Hannah Muermann

# -- Global Variables
room_counter: int = 0
score: int = 0

# -- Lists
room_names: list = ["foyer", "bathroom", "bedroom", "nursery", "home office", "living room", "kitchen", "storage room", "guest room", "home gym"]
direction_options: list = ["north", "east", "south", "west"]

# -- List of Dictionaries
# --- Name of Location, Summary of Location, Details of Location, if it has been visited or not
rooms: dict = [ 
    {"name": "foyer",
    "summary":"This is an old foyer in front of a locked door. The lights are dim.",
    "details":"When you look closer, you see a large rug in front of the door.",
    "was_visited":True}, # Set to True since this is the room the player starts in, therefore they HAVE to visit it

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

# -- Game Map
# --- Each column associated with order of room list (ex: foyer = 0) and each column associated with directions list (ex: north = 0)
game_map: tuple = [["living room", None, None, None],
            ["bedroom", "living room", None, None],
            ["nursery", None, "bathroom", None],
            ["home office", None, "bedroom", None],
            [None, None, "nursery", None],
            ["kitchen", "home gym", "foyer", "bathroom"],
            [None, None, "living room", None],
            [None, None, "guest room", None],
            ["storage room", None, "home gym", None],
            ["guest room", None, None, "living room"]]

# -- Functions
def print_intro():
    global username
    print("Welcome to Hannah's Haunted House!")
    username = get_username()
    print(f"Hello {username}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    input("Press enter to begin: ")

def get_username():
    username: str = input("What's your name? ")
    return username

def print_first_room():
    global room_counter
    global score
    print(rooms[0]["summary"])
    room_counter += 1
    score += 1

def get_help():
    print("These are the valid commands: Help, Quit, North, East, South, West, Examine")

# --- Searches through each room in dictionary to find correct details
def examine(current_room):
    for room in rooms:
        if room["name"] == current_room:
            print(room["details"])
    
# --- Finds index of room and direction in order to find associated room in game map
# --- If the room is not the value None, it will update the current room and add to the score and room counter
# --- It also searches through the dictionary to possibly change was_visited to True, and print the correct summary for the new location
def move(current_room, desired_move):
    global room_counter
    global score
    row_num: int = room_names.index(current_room)
    column_num: int = direction_options.index(desired_move)
    new_room: str = game_map[row_num][column_num]
    if new_room == None:
        print("You cannot go that way. Try again.")
        return current_room
    else:
        for room in rooms:
            if room["name"] == new_room:
                if room["was_visited"] == False:
                    room["was_visited"] = True
                    score += 1
                current_room: str = new_room
                print(room["summary"])
                room_counter += 1
                return current_room

# --- This lets the player choose what they would like to do in the game
# --- It is all contained in an infinite While loop so they can keep playing until they quit
def choose_action(current_room):
    while True:
        desired_move = str.lower(input("What would you like to do? "))
        if desired_move == "help":
            get_help()
            continue
        elif desired_move == "quit":
            break
        elif desired_move == "examine":
            examine(current_room)
            continue
        elif desired_move == "north" or desired_move == "east" or desired_move == "south" or desired_move == "west":
            current_room = move(current_room, desired_move) # Changes the current room variable within the function
            continue
        else:
            print("That is not a valid command. Try again.")
            continue

def print_outro():
    print("You visited", room_counter, "rooms. You have scored", score, "points.")
    print(f"Thank you for playing, {username}. Goodbye!")
    print("© Hannah Muermann 2022. All rights reserved.")

# Main Game
def main():
    global room_counter
    global score
    current_room = rooms[0]["name"] # Intializes the first room
    print_intro()
    print_first_room()
    choose_action(current_room)
    print_outro()

# -- Running the Game          
main()