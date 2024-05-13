class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n) :
            if grid[i][0]==0 :
                for j in range(m) :
                    if grid[i][j]==0 :
                        grid[i][j]=1
                    else :
                        grid[i][j]=0
        for j in range(m) :
            c0,c1=0,0
            for i in range(n) :
                if grid[i][j]==0 :
                    c0 +=1
                else :
                    c1 +=1
            if c0 > c1 :
                for i in range(n) :
                    if grid[i][j]==0 :
                        grid[i][j]=1
                    else :
                        grid[i][j]=0
        ans=0
        for i in range(n) :
            n=grid[i]
            s=0
            v=1
            for i in range(len(n)-1,-1,-1) :
                s += v*n[i]
                v *=2
            ans += s
        return ans
