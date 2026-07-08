class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet=defaultdict(set)
        colSet=defaultdict(set)
        boxSet=defaultdict(set)

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
                
                box=(i//3,j//3)


                if val in boxSet[box]:
                    return False
                else:
                    boxSet[box].add(val)
        return True
