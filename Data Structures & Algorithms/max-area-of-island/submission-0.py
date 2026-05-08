class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        visit=set()
        q=collections.deque()
        island=0
        max_area=0

        def bfs(r,c):
            area=1
            q.append((r,c))
            visit.add((r,c))

            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c=row+dr,col+dc

                    if ( 0 <=r <ROW and  0<=c<COL 
                    and  grid[r][c]==1) and ((r,c) not in visit ):
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
                   

                        
