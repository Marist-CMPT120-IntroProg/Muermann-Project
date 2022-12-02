class World:
    def __init__(self, locales, directions, map):
        self.locales = locales
        self.directions = directions
        self.map = map

    def get_locales(self):
        return self.locales

    def get_directions(self):
        return self.directions

    def get_map(self):
        return self.map