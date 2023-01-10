# James Crisp
# Jan 10, 2023

# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:

        def recurs(the_num,count):
            if count = 0:
                return the_num
            
            modified_num = []

            modified_num.append(1)

            return recurs(int(modified_num),count-1)
    
    return recurs(1,count)
