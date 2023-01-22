# James Crisp

# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        listNums = []
        temp = str(nums[0])+"->"
        print(temp)
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] + 1:
                temp+=str(nums[i])
                print(temp)
                listNums.append(temp)
                temp = str(nums[i+1])+"-->"
    
        return listNums