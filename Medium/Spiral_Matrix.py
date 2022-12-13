#Dec 13, 2022
#James Crisp

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        spiral_order = []
        row_right = 0
        row_left = len(matrix[0])-1
        col_down = 0
        col_up = len(matrix)

        while row_right < inf:
            #Traverse right
            if row_right < len(matrix[0]):
                spiral_order.append(matrix[col_down][row_right])
                row_right += 1
            #Traverse down
            elif col_down < len(matrix):
                spiral_order.append(matrix[col_down][row_right])
                col_down += 1
            #Traverse left
            elif row_left > 0:
                spiral_order.append(matrix[col_up][row_left])
                row_left -= 1
            elif col_up > 0:
                spiral_order.append(matrix[col_up][row_left])
                col_up -= 1
        
        return spiral_order




                





                
