class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        visit=set()

        def dfs(r,c):
            if (r<0 or r>=ROW or c<0 or c>=COL or grid[r][c]==0):
                return 1
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            perimeter=dfs(r,c+1)
            perimeter+=dfs(r-1,c)
            perimeter+=dfs(r+1,c)
            perimeter+=dfs(r,c-1)

            return perimeter
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    return dfs(r,c)
 


            
