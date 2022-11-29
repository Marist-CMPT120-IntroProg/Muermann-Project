class World:
    def __init__(self, locales, map):
        self.locales = locales
        self.map = map

    def get_locales(self):
        return self.locales
        
    def get_map(self):
        return self.map