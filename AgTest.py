
class Room():
    def __init__(self, roomname):
        self.Residents = []
        self.roomname = roomname
   

class Person():
    def __init__(self, name):
        self.name = name


def AddPersonToRoom(room, person, ResidentDict):
    room.Residents += [person]
    if room in ResidentDict:
        ResidentDict[room] += [person]
    else:
        ResidentDict[room] = [person]
    
def GetResidents(room, ResidentDict):
    if room in ResidentDict:
        return ResidentDict[room]
    
    #for person in room.Residents:
    #   return person.name

def GetRoom(person, ResidentDict):
    for room, personlist in ResidentDict.items():
        if person in personlist:
            return room.roomname
            
    
        
study = Room('study')
kitchen = Room('kitchen')
laundry = Room('laundry')

John = Person('John')
Jane = Person('Jane')
Tim = Person('Tim')

ResidentDict = {}

AddPersonToRoom(study, John, ResidentDict)
AddPersonToRoom(study, Jane, ResidentDict)
AddPersonToRoom(laundry, Tim, ResidentDict)

print(GetResidents(study, ResidentDict))
print(GetResidents(kitchen, ResidentDict))

print(GetRoom(Tim, ResidentDict))


'''
class testclass():
    def __init__(self):
        pass


x = testclass()        
y = testclass()

dict = {}
dict[x] = 1
dict[y] = 2

print(dict[y])
'''