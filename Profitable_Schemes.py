class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod=10 **9 +7
        dp={}
        def dfs (i,n,p) :
            if i==len(group) :
                if p >= minProfit :
                    return 1
                else :
                    return 0
            if (i,n,p) in dp :
                return dp[(i,n,p)]
            dp[(i,n,p)]= dfs(i+1,n,p)
            if n-group[i] >= 0 :
                dp[(i,n,p)] += dfs(i+1,n-group[i],min(minProfit,p+profit[i])) % mod
            return dp[(i,n,p)]
        return dfs(0,n,0) % mod
