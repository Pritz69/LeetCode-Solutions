class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        for num in range(2,n+1):
            dp[num]=0 if num==n else num
            for i in range(1,num):
                val=dp[i]*dp[num-i]
                dp[num]=max(dp[num],val)
        return dp[n]
