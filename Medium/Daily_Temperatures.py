# James Crisp
# Jan 8, 2023

# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        final_list = []
        highest_number = 0

        for i in range(len(temperatures)):
            if temperatures[i] > highest_number:
                highest_number = temperatures[i]

        for i in range(len(temperatures)):
            if temperatures[i] == highest_number:
                final_list.append(0)
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    final_list.append(j-i)
                    break
            if len(final_list) == i:
                final_list.append(0)

        return final_list