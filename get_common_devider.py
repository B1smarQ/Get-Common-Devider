'''
input: 10,20,30,40,0
common deviders: [2,5,10]
array of all deviders: [[1,2,5,10], [1,2,4,5,10,20], [1,2,3,5,10,15,30], [1,2,4,5,10,20,40]]

'''
from dataclasses import dataclass

def getInput() ->int:
    user_input = input('Enter a number: ')
    try:
        user_input = int(user_input)
    except ValueError:
        raise ValueError('This type is not supported')
    return user_input
    

class Number:
    def __init__(self,value:int) -> None:
        self.value = value
        self.deviders = []
    
    def __repr__(self):
        return f'Number(value = {self.value})'
    
    
    def get_deviders(self) -> None:
        for i in range(self.value,0,-1):
            if not self.value%i:
                #print(i)
                self.deviders.append(i)
        return self.deviders
    def get_common_deviders(self,other:list[list[int]]) -> tuple[int]:
        '''
        self.deviders = [1,2,5,10]
        input: [[1,2,4,5,10,20]]
        output: [1,2,5,10]
        
        iterate through two dimensional array getting all common values and getting them into a list     
        
        
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

def compare_deviders(deviders:list[list[int]],numbers:list[Number]) ->list[int]:
    temp_list = deviders.copy()
    temp_list.pop(0)
    devs = numbers[0].get_common_deviders(temp_list)
    return devs
def main() -> None:
    nums = []
    deviders = []
    while True:
        x = getInput()
        if not x:
            break
        y = Number(x)
        nums.append(y)
        deviders.append(y.get_deviders())
        print(f'{nums}, {deviders}')
        
    print(compare_deviders(deviders=deviders,numbers=nums))
    
if __name__=='__main__':
    main()