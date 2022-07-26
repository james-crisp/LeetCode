class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        from itertools import combinations
        
        res = list(combinations(nums, 2))
        #2,7 - 2,11 - 2,15 ... etc
        #res[0][0] = 2
        sol = [0,0]
        for i in res:
            if (i[0] + i[1]) == target:
                if i[0] == i[1]:
                    sol = [nums.index(i[0],0), nums.index(i[0],nums.index(i[0],0)+1)]
                    return sol
                else:
                    sol = [nums.index(i[0]),nums.index(i[1])]
                    return sol
        
        return "No solution"
                    
            
            
        