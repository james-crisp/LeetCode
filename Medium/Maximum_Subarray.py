#James Crisp
#Dec 12, 2022

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = -inf
        
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i,len(nums)):
                cur_sum += nums[j]
                total = max(total,cur_sum)

        return total