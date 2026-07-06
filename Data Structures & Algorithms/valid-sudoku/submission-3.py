class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareCheck = [[0 for _ in range(9)] for _ in range(9)]
        for rows in range(len(board)):
            rowsCheck = [0] * 9
            columnCheck = [0] * 9
            for columns in range(len(board)):
                #row
                x = board[rows][columns]
                if x != '.':
                    x = int(x)
                    rowsCheck[x - 1] += 1
                    if rowsCheck[x - 1] > 1:
                        return False    
                #column
                y = board[columns][rows]
                if y != '.':
                    y = int(y)
                    columnCheck[y - 1] += 1
                    if columnCheck[y - 1] > 1:
                        return False  
                #3x3
                z = board[rows][columns]
                if z != '.':
                    z = int(z)
                    squareCheck[((rows // 3) * 3) + columns // 3][z - 1] += 1
                    if squareCheck[((rows // 3) * 3) + columns // 3][z - 1] > 1:
                        return False
        return True 

        
            