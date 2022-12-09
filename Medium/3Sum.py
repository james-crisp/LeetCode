class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 3:
            if sum(nums[:]) == 0:
                return [nums]
            else: return []

        return []