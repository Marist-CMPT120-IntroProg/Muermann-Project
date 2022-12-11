from loc import *
from world import *

class Player:
    def __init__(self, name, world, current_locale, success, counter = 1, score = 1):
        self.name = name
        self.world = world
        self.current_locale = current_locale
        self.success = success
        self.counter = counter
        self.score = score

    def get_name(self):
        return self.name

    def update_current_locale(self, locale):
        self.current_locale = locale
        return self.current_locale

    def get_success(self):
        return self.success

    def update_counter(self, counter):
        self.counter = counter + 1
        return self.counter

    def update_score(self, score):
        self.score = score + 1
        return self.score
    
    def move(self, world, desired_move):
        row_num: int = world.locales.index(self.current_locale)
        column_num: int = world.directions.index(desired_move)
        new_locale = world.map[row_num][column_num]
        if new_locale == None:
            print("You cannot go that way. Try again.")
            return self.current_locale
        else:
            for locale in world.locales:
                if locale == new_locale:
                    if locale.was_visited == False:
                        locale.update_was_visited(locale)
                        self.update_score(self.score)
                        print(locale.summary)
                    else:
                        print(locale.__repr__())
                    self.update_current_locale(locale)
                    self.update_counter(self.counter)
                    return self.current_locale
