# Hannah's Haunted House!
# - By Hannah Muermann

from loc import *
from player import *
from world import *

# Lists
foyer = Location("foyer", "This is an old foyer in front of a locked door. The lights are dim.", "When you look closer, you see a large rug in front of the door.", True)
bathroom = Location("bathroom", "The bathroom is lit by a dim candle. There are cobwebs in the corner.", "When you look closer, you see a rusted sink and a shower with a ripped curtain.", False)
bedroom = Location("bedroom", "The bedroom is a tight space with a queen size bed. The only light is coming from the hallway. There is a locked window.", "When you look under the bed, there is a small shoebox and a key.", False)
nursery = Location("nursery", "The nursery is completely empty. There is a single floorboard coming up. The window is locked.", "When you look under the floorboard, there is a pacifier.", False)
home_office = Location("home office", "The home office has a small desk and a rolling chair. The window is locked.", "When you open the desk, there is a notepad and pen.", False)
living_room = Location("living room", "The living room has a large old couch, and a TV playing at a low volume. The lights are dim. There are two locked windows.", "When you look closer at the TV, it is playing breaking news. The screen has cracks so you cannot see what is playing, and the volume is too quiet to hear it.", False)
kitchen = Location("kitchen", "The kitchen has a stove, oven, fridge, and table with two chairs. The only light is coming from the hallway. The window is locked.", "When you open the fridge, there is a water bottle filled with a liquid.", False)
storage_room = Location("storage room", "The storage room has 6 shelves, but only one box on them. The only light is coming from the hallway. There are no windows.", "Inside the box, there is an old photo album.", False)
guest_room = Location("guest room", "The guest room has a single bed and a nightstand. The lights are dim. There is no window.", "Inside the box, there is an old photo album.", False)
home_gym = Location("home gym", "The home gym contains a treadmill and set of weights. The lights are dim. The window is locked.", "Underneath the treadmill, there is a small box.", False)

world_components = World(
[foyer, bathroom, bedroom, nursery, home_office, living_room, kitchen, storage_room, guest_room, home_gym], 
["north", "east", "south", "west"],
[[living_room, None, None, None],
[bedroom, living_room, None, None],
[nursery, None, bathroom, None],
[home_office, None, bedroom, None],
[None, None, nursery, None],
[kitchen, home_gym, foyer, bathroom],
[None, None, living_room, None],
[None, None, guest_room, None],
[storage_room, None, home_gym, None],
[guest_room, None, None, living_room]]
)

name = input("What is your name? ")
player_components = Player(name, "Hannah's Haunted House", foyer, None, 1, 1)

# Functions
def print_intro():
    print("Welcome to Hannah's Haunted House!")
    print(f"Hello {name}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    input("Press enter to begin: ")

def print_first_room():
    global counter
    global score
    # print(rooms[0]["summary"])
    print(foyer.summary)

def get_help():
    print("These are the valid commands: Help, Quit, North, East, South, West, Examine")

# -- Searches through each room in dictionary to find correct details
def examine():
    for locale in world_components.locales:
        if locale == player_components.current_locale:
            print(locale.details)

# -- Finds index of room and direction in order to find associated room in game map
# -- If the room is not the value None, it will update the current room and add to the score and room counter
# -- It also searches through the dictionary to possibly change was_visited to True, and print the correct summary for the new location
# def move(current_room, desired_move):
#     global room_counter
#     global score
#     row_num: int = room_names.index(current_room)
#     column_num: int = direction_options.index(desired_move)
#     new_room: str = game_map[row_num][column_num]
#     if new_room == None:
#         print("You cannot go that way. Try again.")
#         return current_room
#     else:
#         for room in rooms:
#             if room["name"] == new_room:
#                 if room["was_visited"] == False:
#                     room["was_visited"] = True
#                     score += 1
#                 current_room: str = new_room
#                 print(room["summary"])
#                 room_counter += 1
#                 return current_room

def move(current_locale, desired_move, locales, directions, map):
    current_locale = player_components.get_current_locale()
    locales = world_components.get_locales()
    directions = world_components.get_directions()
    map = world_components.get_map()
    row_num: int = locales.index(current_locale)
    column_num: int = directions.index(desired_move)
    new_locale = map[row_num][column_num]
    if new_locale == None:
        print("You cannot go that way. Try again.")
        return current_locale
    else:
        for locale in world_components.locales:
            if locale == new_locale:
                if locale.was_visited == False:
                    locale.update_was_visited(locale)
                    player_components.update_score(player_components.score)
                player_components.update_current_locale(locale)
                print(locale.summary)
                player_components.update_counter(player_components.counter)
                return current_locale

# -- This lets the player choose what they would like to do in the game
# -- It is all contained in an infinite While loop so they can keep playing until they quit
def choose_action():
    while True:
        desired_move = str.lower(input("What would you like to do? "))
        if desired_move == "help":
            get_help()
            continue
        elif desired_move == "quit":
            break
        elif desired_move == "examine":
            examine()
            continue
        elif desired_move == "north" or desired_move == "east" or desired_move == "south" or desired_move == "west":
            current_locale = player_components.get_current_locale()
            locales = world_components.get_locales()
            directions = world_components.get_directions()
            map = world_components.get_map()
            move(current_locale, desired_move, locales, directions, map)
            # current_locale = player_components.update_current_locale()
            continue
        else:
            print("That is not a valid command. Try again.")
            continue

def print_outro():
    print("You visited", player_components.counter, "rooms. You have scored", player_components.score, "points.")
    print(f"Thank you for playing, {name}. Goodbye!")
    print("© Hannah Muermann 2022. All rights reserved.")

# Main Game
def main():
    # global counter
    # global score
    # current_room = rooms[0]["name"] # Intializes the first room
    print_intro()
    print_first_room()
    choose_action()
    print_outro()

# Running the Game          
main()