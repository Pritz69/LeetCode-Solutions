class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dfs(r,k) :
            if k==len(key) :
                return 0
            if (r,k) in dp :
                return dp[(r,k)]
            res=float('inf')
            for i in range(len(ring)) :
                if ring[i]==key[k] :
                    mind=min(abs(i-r) , len(ring)-abs(i-r))
                    res=min(res,mind+1+dfs(i,k+1))
            dp[(r,k)]=res
            return res
        dp={}
        return dfs(0,0)
