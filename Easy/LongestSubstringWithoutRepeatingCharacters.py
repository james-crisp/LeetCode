class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        stack = []
        
        #create a push/pull stack
        
        for i in range(0,len(s)):
            for j in stack:
                if j == s[i]:
                    print(stack)
                    if len(stack) > total:
                        total = len(stack)
                    stack = []
            stack.append(s[i])
            if len(stack) > total:
                total = len(stack)
                
        
        return total
            
        