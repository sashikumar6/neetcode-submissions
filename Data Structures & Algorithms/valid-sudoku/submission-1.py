class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet=[set() for i in range(9)]
        colSet=[set() for i in range(9)]
        boxSet=[set() for i in range(9)]

        for i in range(9):
            for j in range(9):

                val= board[i][j]

                if val=='.':
                    continue
                
                if val in rowSet[i]:
                    return False
                else:
                    rowSet[i].add(val)
                
                if val in colSet[j]:
                    return False
                else:
                    colSet[j].add(val)
                

                box_row=i//3
                box_col=j//3

                box_ij=box_row*3+box_col

                if val in boxSet[box_ij]:
                    return False
                else:
                    boxSet[box_ij].add(val)
        return True
