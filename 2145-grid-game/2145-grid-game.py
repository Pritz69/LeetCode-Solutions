class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        pr1=grid[0].copy()
        pr2=grid[1].copy()
        for i in range(1,n) :
            pr1[i] += pr1[i-1]
            pr2[i] += pr2[i-1]
        res=float('inf')
        for i in range(n) :
            t=pr1[-1]-pr1[i]
            b=pr2[i-1]if i>0 else 0
            sd=max(t,b)
            res=min(res,sd)
        return res