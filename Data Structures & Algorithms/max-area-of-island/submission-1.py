class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        visit=set()
        maxarea=0
        

        def dfs(r,c):

            if r<0 or r>=ROW or c<0 or c>=COL or (r,c) in visit or grid[r][c]==0:
                return 0
            
            visit.add((r,c))
            area=1

            area+=dfs(r-1,c)
            area+=dfs(r+1,c)
            area+=dfs(r,c-1)
            area+=dfs(r,c+1)

            return area
        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    maxarea=max(maxarea,dfs(r,c))
        
        return maxarea



        

                        
