#James Crisp
#December 1, 2022

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        list_s = list(s)
        final_list = []
        final_list.append(list_s)
        
        def ispalindrome(letters):
            palin = True
            for i in range(len(letters)):
                if letters[i] != letters[-i-1]:
                    palin = False
                    break
            return palin
        
        
        
        return final_list