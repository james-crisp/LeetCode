#James Crisp
#December 2nd, 2022

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = []
        temp = []
        
        def ispalindrome(letters):
            for i in range(len(letters)):
                if letters[i] != letters[-i-1]:
                    return False
            return True
        
        return ispalindrome("abbaa")
                    
                
            
                