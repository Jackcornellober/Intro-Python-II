# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description,items):
        self.description = description
        self.name = name
        self.items = items
    