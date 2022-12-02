class Location:
    def __init__(self, name, summary, details, was_visited):
        self.name = name
        self.summary = summary
        self.details = details
        self.was_visited = was_visited

    def get_name(self):
        return self.name

    def get_summary(self):
        return self.summary

    def get_details(self):
        return self.details
    
    def get_was_visited(self):
        return self.was_visited

    def update_was_visited(self, was_visited):
        self.was_visited = was_visited
        return self.was_visited

    def __repr__(self):
        if self.was_visited == True:
            return self.summary
        else:
            return f"You are in the {self.name}."
            
