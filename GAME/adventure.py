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
guest_room = Location("guest room", "The guest room has a single bed and a nightstand. The lights are dim. There is no window.", "Inside a small box, there is an old photo album.", False)
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

# Functions
# - Prints each time a new game starts
def print_intro(): 
    print("Welcome to Hannah's Haunted House!")
    print(f"Hello {name}! You will soon travel through several rooms and chat to many ghosts in order to escape this spooky home.")
    print("But be warned! The ghosts are not exactly fond of humans.")
    input("Press enter to begin: ")

# - Game always starts in foyer
def print_first_room():
    print(foyer.summary)

def get_help():
    print("These are the valid commands: Help, Quit, North, East, South, West, Examine, Talk")

# - When this function finds where the current locale is in the list in the world class, it then uses that variable to access the details in the location class.
def examine():
    for locale in world.locales:
        if locale == player.current_locale:
            print(locale.details)

# - Prints options for who a player can talk to in any given room.
def talk():
    if player.current_locale == storage_room:
        print("A ghost flies out of the box! \"Get out of here human! You're just a guest here.\"")
    elif player.current_locale == nursery:
        print("A ghost flies out of the space underneath the floorboard. \"Hey! This house belongs to the spooky spirits. Get out of here, guest.")
    elif player.current_locale == bedroom:
        print("A ghost flies out from underneath the mattress. \"This is not your home, human. Be gone!\"")
    elif player.current_locale == guest_room:
        offer_riddle()
    elif player.current_locale == kitchen:
        print("A ghost flies out of the oven! \"Ugh a human... Well we might have a room for you in this house, but nothing permanent.\"")
    else:
        print("There is no one to talk to here.")

# - To win or lose the game, you must solve a riddle.
# - You can choose to not play the riddle and continue venturing on.
# - If you do play, you have to get it right or else you lose the game.
def offer_riddle():
    play_riddle = input("A ghost flies out of the nightstand. \"...Hello. Do you wanna get out of here? I can help you, but only if you can answer a quick question. Wanna play? ")
    if play_riddle.lower() == "yes":
        riddle_answer = input("Okay, human. In a house full of ghosts, what is your role here? ")
        # I tried to be offer many different options that a person can guess
        if riddle_answer.lower() == "a guest" or riddle_answer.lower() == "guest" or riddle_answer.lower() == "the guest" or riddle_answer.lower() == "i am a guest" or riddle_answer.lower() == "i am the guest" or riddle_answer.lower() == "i'm a guest" or riddle_answer.lower() == "im a guest" or riddle_answer.lower() == "i'm the guest" or riddle_answer.lower() == "im the guest":
            print("You're correct! I guess I'll let you go, since you know your place here")
            player.success = True
        else:
            print("Wrong! Have you learned nothing? This is the house of the ghosts, you're just a guest here.")
            player.success = False
    elif play_riddle.lower() == "no":
        print("Fine. Come back later then.")
    else:
        print("I don't understand what you're saying.")

# - This lets the player choose what they would like to do in the game.
# - It is all contained in an infinite While loop so they can keep playing until they quit OR win/lose.
def choose_action():
    while player.success == None:
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
            talk()
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

# - Resets all the data essential to restart a game.
# - This includes if the player has won or not, the current locale, room counter, score, and if each room was visited.
def game_reset():
    player.success = None
    player.current_locale = foyer
    player.counter = 1
    player.score = 1
    bathroom.was_visited = False
    bedroom.was_visited = False
    nursery.was_visited = False
    home_office.was_visited = False
    living_room.was_visited = False
    kitchen.was_visited = False
    storage_room.was_visited = False
    guest_room.was_visited = False
    home_gym.was_visited = False

# Main Game
# - This is contained within a while loop to make it possible for a player to restart the game.
def main():
    while True:
        print_intro()
        print_first_room()
        choose_action()
        print_outro()
        play_again = input("Would you like to play again? ")
        if play_again.lower() == "yes":
            game_reset()
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("If you would like to play again, please restart the game.")
            break

# Running the Game          
main()