class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 :
            return 1
        ws =0 
        for i in range(k,k+maxPts) :
            ws += 1 if i<=n else 0
        dp={}
        for i in range(k-1,-1,-1) :
            rem=0
            dp[i] = ws/maxPts
            if i + maxPts <= n :
                rem = dp.get(i+maxPts,1)
            ws += dp[i] - rem
        return dp[0]
