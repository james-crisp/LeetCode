class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        stack = [s[0]]
        
        #create a push/pull stack
        #recursion?
        
        for i in range(1,len(s)):
            stack.append(s[i])
            if s[i] in stack:
                for j in range(len(stack)):
                    if stack[j] == s[i]:
                        stack = stack[j+1:]
                    print(stack)
            if len(stack) > total:
                total = len(stack)
                
        
        return total
        