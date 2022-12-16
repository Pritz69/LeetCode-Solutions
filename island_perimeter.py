class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            p=dfs(i,j+1)
            p+=dfs(i+1,j)
            p+=dfs(i,j-1)
            p+=dfs(i-1,j)
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
        
