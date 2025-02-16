from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(numbers)):
            if target - numbers[i] in numMap:
                return [numMap[target - numbers[i]]+1, i+1]
            numMap[numbers[i]] = i
        return [-1, -1]
