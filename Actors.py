def check_dest(f):
    def wrapper(*args):
        if args[0].dest:
            #print("you didn't use it")
            return None
        else:
            return f(*args)
    return wrapper


class Actor:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.destroyed = False
        pass
        
    def destroy(self):
        self.destroyed = True
        

class Lifeform(Actor):
    def __init__(self, name="", description="", species=""):
        super().__init__(name, description)
        self.species = species

        
            
class Person(Lifeform):
    def __init__(self, Name, Age, Health=100):
        self.Name = Name
        self.Age = Age
        self.Health = 100
        self.Status = 'Healthy'
        Location = {}

        
    @check_dest
    def _act(self):
        pass
        
    def get_status(self):
        if self.Health > 70:
            return 'Healthy'
        elif self.Health > 30:
            return 'Worse for Wear'
        elif self.Health > 0:
            return 'Critical'
        else:
            return 'Dead'
            
    def Take_Damage(self, damage_i):
        self.Health -= damage_i


class Crew(Person):
    def __init__(self, Position, Name, Age, Health=100):
        self.Position = Position
        self.Name = Name
        self.Age = Age
        self.Health = 100
        self.Inventory = {}

    def Print_Actor_Status(self, level = 'Full'):
        print('\nStatus Report...Activated')
        print('Name... %s' % self.Name)
        print('Position... %s' % self.Position)
        print('Age... %i' % self.Age)
        print('Health Status... %s' % self.get_status())


class Item(Actor):
    def __init__(self):
        self.Requirements = {"expertise": "high"}
        self.Charges = 3
        self.Energy = 5
        
    @check_dest
    def _use(self):
        self._itemfunction()
    
    def _itemfunction(self):
        self.Energy -= cost
        self.Charges -= 1
        
class Location(Actor):
    def __init__(self, Name, Description, Loc):
        self.Name = Name
        self.Description = Description
        self.Loc = Loc

class Planet(Location):
    def __init__(self, Name, Description, Loc):
        self.Name = Name
        self.Description = Description
        self.Loc = Loc
        self.Details = [] #atmosphere, G, etc

class Ship(Location):
    def __init__(self, Name, Description, Loc):
        self.Name = Name
        self.Description = Description
        self.Loc = Loc
        self.Details = [] #Engines, Departments, ammo, fuel etc

    def travel(self, Loc):
        pass