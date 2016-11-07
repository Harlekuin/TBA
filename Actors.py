


class Actor:
    def __init__(self):
        self.Name = ""
        self.Description = ""
        pass

class Person(Actor):
    def __init__(self):
        self.Age = 0
        pass

class Item(Actor):
    def __init__(self):
        self.Requirements = {"expertise": "high"}
        