class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        q=deque()
        fresh=0
        time=0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])

        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        while q and fresh >0:
            for i in range(len(q)):
                row,col=q.popleft()

                for dr,dc in directions:
                    r,c=dr+row,dc+col

                    if (r < 0 or r==ROW or c<0 or c==COL or grid[r][c] !=1):
                        continue
                    
                    grid[r][c]=2
                    q.append([r,c])
                    fresh-=1
            time+=1
        
        if fresh==0:
            return time
        else:
            return -1


