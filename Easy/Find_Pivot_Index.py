# James Crisp
# Jan 5, 2023

# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        index_left = 0
        total_left = nums[index_left]
        
        index_right = len(nums) - 1
        total_right = nums[index_right]

        while index_left != index_right:

            if total_left < total_right:
                index_left += 1
                total_left += nums[index_left]
            else:
                index_right -= 1
                total_right += nums[index_right]
        
        if total_left == total_right:
            return index_left
        else:
            return -1