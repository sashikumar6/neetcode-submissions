class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posDiagonal=set()
        negDiagonal=set()

        board=[["."]* n for r in range(n)]
        res=[]

        def backtracking(r):
            if r==n:
                copy=["".join(row) for row in board ]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or r+c in posDiagonal or r-c in negDiagonal :
                    continue
                
                col.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c]="Q"

                backtracking(r+1)

                col.remove(c)
                posDiagonal.remove(r + c)
                negDiagonal.remove(r - c)
                board[r][c] = "."

        backtracking(0)

        return res


