class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        
        if len(s) == 0: return 0
        elif len(s) == 1: return 1
        
        stack = [s[0]]
        
        #create a stack
        
        
        for i in range(1,len(s)):
            
            if s[i] in stack:
                
                for j in range(len(stack)):
                    if stack[j] == s[i]:
                        stack = stack[j+1:]
                        break
                        
            stack.append(s[i])     
            if len(stack) > total:
                total = len(stack)
                
        
        return total
            
        
        