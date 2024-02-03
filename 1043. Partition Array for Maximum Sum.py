class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def rec(ind) :
            if ind >= len(arr) :
                return 0
            if ind in dp :
                return dp[ind]
            m=0
            res=0
            for j in range(ind,min(len(arr),ind+k)) :
                m=max(m,arr[j])
                size=j-ind + 1
                res=max(res,rec(j+1) + m*size)
            dp[ind]=res
            return res
        dp={}
        return rec(0)
