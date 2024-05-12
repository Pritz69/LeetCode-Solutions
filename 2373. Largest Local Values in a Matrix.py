class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(grid)
        li=[]
        for i in range(n-2) :
            for j in range(n-2) :
                m=0
                for k in range(i,i+3) :
                    for l in range(j,j+3) :
                        if k < n and l < n :
                            m=max(m,grid[k][l])
                li.append(m)
                if len(li)==n-2 :
                    ans.append(li)
                    li=[]
                if len(ans)==n-2 :
                    return ans
