from typing import List
from itertools import combinations

class SumEquals():
    def __init__(self, nums:List[int], target:int) -> None:
        self.nums = nums
        self.target = target
        
    def sumEquals(self) -> List[int]:
        results = []
        for i in range(len(self.nums)):
            for num in combinations(self.nums, i):
                if sum(num) == self.target:
                    results.append(num)
        return results