# Hannah's Haunted House!
# - By Hannah Muermann

from loc import *
from player import *
from world import *

# All Locales
# - name, summary, details, was visited
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

# World
# - list of locales, list of directions, navigation matrix
world = World(
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

# Player
# - name of player, name of world, current locale, room counter, score
name = input("What is your name? ")
player = Player(name, world, foyer, None, 1, 1)

all_data = world, player

# Functions
def print_intro(): 
    print("Welcome to Hannah's Haunted House!")
    print(f"Hello {name}! You will soon travel through several rooms and collect many objects in order to escape this spooky home.")
    input("Press enter to begin: ")

def print_first_room():
    print(foyer.summary)

def get_help():
    print("These are the valid commands: Help, Quit, North, East, South, West, Examine, Talk")

# -- Searches through each room in dictionary to find correct details
def examine():
    for locale in world.locales:
        if locale == player.current_locale:
            print(locale.details)

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
        elif desired_move == "talk":
            if player.current_locale == storage_room:
                print("A ghost flies out of the box! \"Get out of here human! You're just a guest here.\"")
            elif player.current_locale == nursery:
                print("A ghost flies out of the space underneath the floorboard. \"Hey! This house belongs to the spooky spirits. Get out of here, guest.")
            elif player.current_locale == guest_room:
                riddle_answer = input("A ghost flies out of the nightstand. \"...Hello. Do you wanna get out of here? I can help you, but just answer this quick question. What is your role here? ")
                if riddle_answer.lower() == "a guest" or riddle_answer.lower() == "guest" or riddle_answer.lower() == "the guest":
                    print("You're correct! I guess I'll let you go, since you know your place here")
                    player.success = True
                    break
                else:
                    print("Wrong! Have you learned nothing? This is the house of the ghosts, you're just a guest here.")
                    player.success = False
                    break
        elif desired_move == "north" or desired_move == "east" or desired_move == "south" or desired_move == "west":
            player.move(world, desired_move)
            continue
        else:
            print("That is not a valid command. Try again.")
            continue

def print_outro():
    if player.success == True:
        print("The ghosts let you escape the house! You win!")
    elif player.success == False:
        print("The ghosts never let you escape. You are stuck in the guest room forever!")
    print("You visited", player.counter, "rooms. You have scored", player.score, "points.")
    print(f"Thank you for playing, {name}. Goodbye!")
    print("© Hannah Muermann 2022. All rights reserved.")

# Main Game
def main():
    while True:
        print_intro()
        print_first_room()
        choose_action()
        print_outro()
        play_again = input("Would you like to play again? ")
        if play_again.lower() == "yes":
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("If you would like to play again, please restart the game.")
            break

# Running the Game          
main()