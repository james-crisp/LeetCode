#Dec 13, 2022
#James Crisp

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        spiral_order = []
        row_right = 0
        row_left = len(matrix[0]) - 1
        col_down = 0
        col_up = len(matrix) - 1

        while row_right < inf:
            #Traverse right
            if row_right <= row_left:
                spiral_order.append(matrix[col_down][row_right])
                row_right += 1
                #Last row_right will be out of range
            #Traverse down
            elif col_down < col_up:
                col_down += 1
                spiral_order.append(matrix[col_down][row_right-1])
                #Last col_down will be out of range for next time
            #Traverse left
            elif row_left >= 0:
                spiral_order.append(matrix[col_up][row_left - 1])
                row_left -= 1
            #Traverse up
            elif col_up > 0:
                col_up -= 1
                spiral_order.append(matrix[col_up][row_left-1])
            print(spiral_order)
        
        return spiral_order




                





                





                





                





                
