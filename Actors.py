def check_dest(f):
    def wrapper(*args):
        if args[0].dest:
            #print("you didn't use it")
            return None
        else:
            return f(*args)
    return wrapper


class Actor:
    def __init__(self):
        self.Name = ""
        self.Description = ""
        
        pass
        
    def _Destroy(self):
        self.Destroyed = True

class Person(Actor):
    def __init__(self):
        self.Age = 0
        pass
        
    @check_dest
    def _act(self):
        

class Item(Actor):
    def __init__(self):
        self.Requirements = {"expertise": "high"}
        self.Charges = 3
        self.Energy = 5
        
    @check_dest
    def _use(self):
        self._itemfunction():
    
    def _itemfunction(self):
        self.Energy -= cost
        self.Charges -= 1
        
    
        
        

        
        