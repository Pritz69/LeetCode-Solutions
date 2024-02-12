class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def rec(i,j,x,y) :
            if i>=n or j>=m or x>=n or y>=m or grid[i][j]==-1 or grid[x][y]==-1 :
                return float('-inf')
            if i==n-1 and j==n-1 :
                return grid[i][j]
            if x==n-1 and y==n-1 :
                return grid[x][y]
            if (i,j,x,y) in dp :
                return dp[(i,j,x,y)]
            if i==x and j==y :
                ans=grid[i][j]
            else :
                ans=grid[i][j]+grid[x][y]
            ans+=max(max(rec(i,j+1,x,y+1),rec(i+1,j,x+1,y)),max(rec(i,j+1,x+1,y),rec(i+1,j,x,y+1)))
            dp[(i,j,x,y)]=ans
            return ans
        dp={}
        return max(0,rec(0,0,0,0))
