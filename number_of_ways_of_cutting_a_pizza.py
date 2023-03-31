class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows=len(pizza)
        cols=len(pizza[0])
        prefixsum =[[0 for j in range(cols+1)]for i in range(rows+1)]
        for i in range(rows-1,-1,-1) :
            for j in range(cols-1,-1,-1) :
                cell=1 if pizza[i][j]=='A' else 0
                rightgrid=prefixsum[i][j+1]
                bottomgrid=prefixsum[i+1][j]
                botrightgrid=prefixsum[i+1][j+1]
                prefixsum[i][j]= cell + rightgrid + bottomgrid - botrightgrid
        
        dp={}
        def recurse(crow,ccol,k) :
            if (crow,ccol,k) in dp :
                return dp[(crow,ccol,k)]
            if prefixsum[crow][ccol]==0 :
                return 0
            if k==0 :
                return 1
            ans=0
            for i in range(crow+1,rows) :
                if prefixsum[crow][ccol] - prefixsum[i][ccol] > 0 :
                    ans += recurse(i,ccol,k-1)
            for j in range(ccol+1,cols) :
                if prefixsum[crow][ccol] - prefixsum[crow][j] > 0 :
                    ans += recurse(crow,j,k-1)
            dp[(crow,ccol,k)]=ans
            return ans
        return recurse(0,0,k-1) % (10**9 +7)
