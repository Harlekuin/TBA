import Actors
import Loading

def Print_Actor_Status(_Actor, level = 'Full'):
    print('\nStatus Report...Activated')
    if type(_Actor) == Actors.Person:
        print('Name... %s' % _Actor.Name)
        print('Position... %s' % _Actor.Position)
        print('Age... %i' % _Actor.Age)
        print('Health Status... %s' % _Actor.get_status())

        
        
if __name__ == '__main__':
    CrewMember = Actors.Crew(Name = 'John Smith', 
                                          Position = 'Captain', 
                                          Age = 53)
    
    CrewMember.Print_Actor_Status()
    CrewMember.Take_Damage(80)
    CrewMember.Print_Actor_Status()
    
'''
as per https://stackoverflow.com/questions/40704035/what-would-be-the-most-efficient-way-to-set-up-classes-that-belong-to-a-class
and https://en.wikipedia.org/wiki/Object_composition#Aggregation

set up an external dictionary with the relationships
'''    