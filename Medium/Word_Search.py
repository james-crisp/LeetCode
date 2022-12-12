class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        answer = False

        def wordsearch(letter):
            num_rows = len(board)
            num_cols = len(board[0])
            for i in range(num_rows):
                for j in range(num_cols):
                    if board[i][j] == letter:
                        return [i,j]
            return False

        for letter in word:
            location = wordsearch(letter)

        return answer