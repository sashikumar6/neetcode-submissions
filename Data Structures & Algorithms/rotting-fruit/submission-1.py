class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS=len(grid)
        COLS=len(grid[0])

        fresh=0
        minute=0
        q=collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                R,C = q.popleft()
            
                for dr,dc in directions:
                    row=R+dr
                    col=C+dc

                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col]=2
                    fresh-=1
                    q.append([row,col])
            minute+=1
            
        if fresh==0:
            return minute
        else:
            return -1