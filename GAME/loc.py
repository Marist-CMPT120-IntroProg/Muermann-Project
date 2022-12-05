class Location:
    def __init__(self, name, summary, details, was_visited):
        self.name = name
        self.summary = summary
        self.details = details
        self.was_visited = was_visited

    def update_was_visited(self, was_visited):
        self.was_visited = was_visited
        return self.was_visited

    def __repr__(self):
        return f"You are in the {self.name}."
            
