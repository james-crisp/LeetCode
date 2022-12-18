#Dec 13, 2022
#James Crisp

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        spiral_order = []
        row_right = 0
        row_left = len(matrix[0]) - 1
        col_down = 0
        col_up = len(matrix) - 1

        while row_right <= row_left and col_down <= col_up:
            #Traverse right
            for i in range(row_right,row_left+1):
                spiral_order.append(matrix[row_right][i])
            row_right += 1
                
            #Traverse down
            for i in range(col_down+1,col_up):
                spiral_order.append(matrix[i][row_left])
            col_down += 1
            
            #Traverse left
            for i in range(row_right-1,row_left):
                spiral_order.append(matrix[col_up][-i-1])
            row_left -= 1
            
            #Traverse up
            for i in range(col_down-1,col_up):
                spiral_order.append(matrix[-i-1][row_right-1])
            col_up -= 1
            

        return spiral_order




                





                





                





                





                





                





                





                
