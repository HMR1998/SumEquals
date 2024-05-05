from typing import List

class user():
    def userInput(self) -> List[int]:
        nums = list(map(int, (input('Enter your list: ').split())))
        target = int(input('Enter your target value: '))
        return nums, target