from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            res[i] = stack[-1] if stack else -1
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
        return res 