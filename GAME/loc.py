class Location:
    def __init__(self, name, summary, details, was_visited):
        self.name = name
        self.summary = summary
        self.details = details
        self.was_visited = was_visited

    def __repr__(self):
        if self.was_visited == True:
            return self.summary
        else:
            return f"You are in the {self.name}."
            
