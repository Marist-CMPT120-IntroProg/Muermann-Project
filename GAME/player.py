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

    def get_world(self):
        return self.world
    
    def get_current_locale(self):
        return self.current_locale

    def update_current_locale(self, locale):
        self.current_locale = locale
        return self.current_locale

    def get_desired_move(self):
        return self.desired_move

    def update_desired_move(self, desired_move):
        self.desired_move = desired_move
        return self.desired_move

    def get_counter(self):
        return self.counter

    def update_counter(self, counter):
        self.counter = counter + 1
        return self.counter

    def get_score(self):
        return self.score

    def update_score(self, score):
        self.score = score + 1
        return self.score

    # def move(self, current_locale, desired_move, locales, directions, map):
    #     row_num: int = locales.index(current_locale)
    #     column_num: int = directions.index(desired_move)
    #     new_locale: str = map[row_num][column_num]
    #     if new_locale == None:
    #         print("You cannot go that way. Try again.")
    #         return current_locale
    #     else:
    #         for locale in locales:
    #             if locale == new_locale:
    #                 if locale.get_was_visited() == False:
    #                     locale.update_was_visited() == True
    #                     self.score += 1
    #                 current_locale: str = new_locale
    #                 print(Location.get_summary())
    #                 self.counter += 1
    #                 return current_locale
    
