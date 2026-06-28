class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        q=deque()
        visit=set()
        time=0
        fresh=0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()

                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr,nc=r+dr,c+dc

                    if nr<0 or nr>=ROW or nc<0 or nc>=COL or (nr,nc) in visit:
                        continue

                    if grid[nr][nc]==0:
                        continue
                    
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1

                        q.append((nr,nc))
                        visit.add((nr,nc))
            time+=1
        
        if fresh==0:
            return time
        else:
            return -1
        


        