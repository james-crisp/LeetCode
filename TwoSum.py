class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        locations = [0,0]
        done = False
        
        def tryit(numbers):
            test = numbers[0]
            for j in range(1,len(numbers)):
                if test + numbers[j] == target:
                    locations[1] = j
                    done = True
                    return
            
        if done == True:
            print(locations)
            return locations
        else:
            for i in range(len(nums)):
                locations[0] = i
                tryit(nums[i:])

            
            