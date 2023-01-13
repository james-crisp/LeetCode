# James Crisp
# Jan 12, 2023

# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        final_merge = []
        i = 0
        temp = intervals[0]

        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                temp[1] = intervals[i+1][1]
                print(temp)
            else:
                final_merge.append(temp)
                temp = intervals[i]

            i += 1

        return final_merge