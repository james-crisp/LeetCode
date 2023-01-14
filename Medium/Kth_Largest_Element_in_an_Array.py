# James Crisp
# Jan 13, 2023

# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        largest = -inf

        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        
        return largest
