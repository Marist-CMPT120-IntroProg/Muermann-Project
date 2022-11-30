from loc import *
from world import *

class Player:
    def __init__(self, name, world, current_locale, desired_move, counter, score):
        self.name = name
        self.world = world
        self.current_locale = current_locale
        self.desired_move = desired_move
        self.counter = counter
        self.score = score
    
    def get_name(self):
        return self.name

    def get_counter(self):
        return self.counter

    def update_counter(self, counter):
        self.counter = counter
        return self.counter

    def get_score(self):
        return self.score

    def update_score(self, score):
        self.score = score
        return self.score

    def move(self):
        row_num: int = World.get_locales().index(self.current_locale)
        column_num: int = World.get_directions().index(self.desired_move)
        new_locale: str = World.map[row_num][column_num]
        if new_locale == None:
            print("You cannot go that way. Try again.")
            return self.current_locale
        else:
            for locale in World.locales:
                if locale == new_locale:
                    if Location.get_was_visited() == False:
                        Location.set_was_visited(True)
                        self.score += 1
                    current_room: str = new_locale
                    print(Location.get_summary())
                    self.counter += 1
                    return current_room
    
