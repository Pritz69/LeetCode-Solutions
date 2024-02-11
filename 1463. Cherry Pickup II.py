class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def rec(i,j1,j2) :
            if j1<0 or j1>=m or j2<0 or j2>=m :
                return float('-inf')
            if i==n-1 :
                if j1==j2 :
                    return grid[i][j1]
                else :
                    return grid[i][j1]+grid[i][j2]
            if (i,j1,j2) in dp :
                return dp[(i,j1,j2)]
            maxi=0
            for x in range(-1,2) :
                for y in range(-1,2) : 
                    if j1==j2 :
                        maxi=max(maxi,grid[i][j1] + rec(i+1,j1+x,j2+y))
                    else :
                        maxi=max(maxi,grid[i][j1] + grid[i][j2] + rec(i+1,j1+x,j2+y))
            dp[(i,j1,j2)]=maxi
            return maxi
        dp={}
        return rec(0,0,m-1)
