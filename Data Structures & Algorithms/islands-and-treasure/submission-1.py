class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW=len(grid)
        COL=len(grid[0])
        visit=set()
        q=deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        
        while q:
            r,c=q.popleft()

            directions=[[0,-1],[0,1],[-1,0],[1,0]]

            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                if nr<0 or nr>=ROW or nc<0 or nc>=COL or grid[nr][nc]==-1 or (nr,nc) in visit:
                    continue 
                
                
                q.append((nr,nc))
                visit.add((nr,nc))


                if grid[nr][nc] !=2147483647:
                    continue

                grid[nr][nc]=1+grid[r][c]
    
            
