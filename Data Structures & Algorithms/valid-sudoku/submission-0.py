class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)

        rowSet=[set() for _ in range(n)]
        colSet=[set() for _ in range(n)]
        boxSet=[set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val=board[i][j]
                if val==".":
                    continue
                if val in rowSet[i]:
                    return False
                else:
                    rowSet[i].add(val)
                
                if val in colSet[j]:
                    return False
                else:
                    colSet[j].add(val)
            
                box_ij=(i//3*3 + j//3)
                if val in boxSet[box_ij]:
                    return False
                else:
                    boxSet[box_ij].add(val)
        return True