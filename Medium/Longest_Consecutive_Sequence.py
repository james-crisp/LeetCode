# James Crisp
# Jan 9, 2023

# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Hash table
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        hash_table = {}
        highest = -inf
        lowest = inf

        for i in range(len(nums)):
            hash_table[nums[i]] = nums[i]
            if nums[i] > highest:
                highest = nums[i]
            elif nums[i] < lowest:
                lowest = nums[i]

        best = 0
        temp = 0
        for i in range(lowest,highest+1):
            if i in hash_table.values():
                temp += 1
                if temp>best:
                    best = temp
            else:
                temp = 0

        return best
