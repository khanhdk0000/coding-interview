from typing import List
def jump(nums: List[int]) -> int:
    # initVal, jump, pos, n, subMaxPos = nums[0], 0, 0, len(nums) - 1, 0
    # if n == 0:
    #     return 0
    # if initVal >= n:
    #     return 1
    # while pos < n:
    #     jump += 1
    #     print(jump, pos, initVal)
    #     if nums[pos] + pos >= n :
    #         return jump
    #     initVal = nums[pos+1]
    #     for i in range(1, nums[pos]+1):
    #         idx = pos + i
    #         if nums[idx] >= initVal:
    #             initVal = nums[idx]
    #             subMaxPos = idx
    #         if nums[idx] + idx >= n :
    #             return jump + 1
    #         if idx >= n:
    #             break
    #     if subMaxPos > pos:
    #         pos = subMaxPos
    # return jump
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times


input = [1,1,1,1,1]
# input = [1,2]
# input = [0]
# input = [2,1,1,1,1]
# input = [2,3,1,1,4]
# input = [2,1]
# input = [1,2,3]
input = [3,4,3,2,5,4,3]
# input = [5,9,3,2,1,0,2,3,3,1,0,0]
input = [10,9,8,7,6,5,4,3,2,1,1,0]
input = [9,8,7,6,5,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]
#vlvov
print(jump(input))

    