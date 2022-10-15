'''
EXAMPLE:
input: 10,20,30,40,0
common_deviders: [2,5,10]
array of all deviders: [[1,2,5,10], [1,2,4,5,10,20], [1,2,3,5,10,15,30], [1,2,4,5,10,20,40]]

output:common_deviders
'''
from dataclasses import dataclass

def getInput() ->int:
    '''
    EXAMPLE:
    input:1,5.1,hello world
    
    output:1,ValueError(This type is not supported),ValueError(This type is not supported)
    
    gets a user input
    converts into an int
    raises an error if input is not an int
    '''
    user_input = input('Enter a number: ')
    try:
        user_input = int(user_input)
    except ValueError:
        raise ValueError('This type is not supported')
    return user_input
    

class Number:
    '''
    class for any integer
    contains function to get all its deviders
    contains function to get all common deviders from self deviders and 2D array of other deviders 
    '''
    def __init__(self,value:int) -> None:
        self.value = value
        self.deviders = []
    
    def __repr__(self):
        return f'Number(value = {self.value})'
    
    
    def get_deviders(self) -> list[int]:
        '''
        EXAMPLE:
        input:self.value = 10
        
        output: [1,2,5,10]
        
        iterates through all numbers from self value to 0
        puts all deviders in a array and returns it
        '''
        for i in range(self.value,0,-1):
            if not self.value%i:
                self.deviders.append(i)
        return self.deviders
    def get_common_deviders(self,other:list[list[int]]) -> tuple[int]:
        '''
        EXAMPLE:
        self.deviders = [1,2,5,10]
        input: [[1,2,4,5,10,20]]
        
        output: [1,2,5,10]
        
        takes a 2D array of all deviders except for itself
        iterates through the deviders
        compares self deviders with all others   
        returns a reversed sorted tuple of common deviders
        
        '''
        self.deviders.clear()
        self.get_deviders()
        common_deviders = []
        for devider in self.deviders:
            for i in range(len(other)):
                for z in range(len(other[i])):
                    if devider == other[i][z]:
                        common_deviders.append(devider)
                        
        return sorted(tuple(set(common_deviders)),reverse=True)

def compare_deviders(deviders:list[list[int]],numbers:list[Number]) ->tuple[int]:
    '''
    EXAMPLE:
    input: [[1,2,5,10],[1,2,4,5,10,20]]
    
    output:[[1,2,4,5,10,20]]
    
    takes a 2D array of all deviders
    removes the first element of the array
    gets all common deviders and returns them as a sorted tuple   
    '''
    temp_list = deviders.copy()
    temp_list.pop(0)
    devs = numbers[0].get_common_deviders(temp_list)
    return devs
def main() -> None:
    '''
    EXAMPLE:
    input: 10,20,30
    nums: [10,20,30]
    deviders:[[1,2,5,10],[1,2,4,5,10,20],[1,2,3,5,10,15,30]]
    
    output:[1,2,5,10]
    
    
    takes user input until user gives a 0
    puts all inputs in an array of Number class objects
    puts all deviders in a 2D array of integers
    gets and outputs all common deviders
    '''
    nums = []
    deviders = []
    while True:
        x = getInput()
        if not x:
            break
        y = Number(x)
        nums.append(y)
        deviders.append(y.get_deviders())
        
    print(compare_deviders(deviders=deviders,numbers=nums))
    
if __name__=='__main__':
    main()
