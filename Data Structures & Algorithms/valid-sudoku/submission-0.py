class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #verify row
        for r in range(9):
            seen = []
            row = board[r]
            for i in row:
                if i != '.' and i in seen:
                    return False
                seen.append(i)

        #verify column:
        for c in range(9):
            seen = []
            for i in range(9):
                n = board[i][c]
                if n != '.' and n in seen:
                    return False
                seen.append(n)
        
        #check box
        for boxRow in range(3):
            for boxCol in range(3):
                seen = []
                for r in range(3):
                    for c in range(3):
                        n = board[r + 3*boxRow][c + 3*boxCol]
                        if n != '.' and n in seen:
                            return False
                        seen.append(n)
        
        return True
