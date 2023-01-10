# James Crisp
# Jan 10, 2023

# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:

        def recurs(the_num,count):
            if count == 0:
                return the_num

            if the_num == 1:
                return recurs(11,count-1)

            list_num = [int(x) for x in str(the_num)]
            modified_num = []

            ot_count = 1
            for i in range(len(list_num)-1):
                if list_num[i] == list_num[i+1]:
                    ot_count += 1
                else:
                    modified_num.append(ot_count)
                    modified_num.append(list_num[i])
                    ot_count = 1
            print(modified_num)
            modified_num = int("".join(modified_num))

            return recurs(modified_num,count-1)
    
        return recurs(1,count)

