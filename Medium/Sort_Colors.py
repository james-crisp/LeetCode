# James Crisp
# Jan 11, 2023

# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        while count!=0:
            for i in range(len(nums)-1):
                if nums[-i-1] < nums[-i-2]:
                    #Swap numbers
                    nums[-i-1],nums[-i-2]=nums[-i-2],nums[-i-1]
            count -= 1
        
        return