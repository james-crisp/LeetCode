# James Crisp
# Jan 4, 2023

# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        final = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            final.append(total)
        
        return final