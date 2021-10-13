from typing import List


def solve(nums: List[int]):
    max_sum = nums[0]

    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i] + nums[i + 1]:
            nums[i + 1] += nums[i]
        
        if max_sum < nums[i + 1]:
            max_sum = nums[i + 1]
    
    return max_sum


n = int(input())
nms = map(int, input().split())
nms = list(nms)
print(solve(nms))
