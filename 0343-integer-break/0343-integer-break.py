class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        for num in range(2,n+1) :
            dp[num] = 0 if num==n else num
            for j in range(1,num) :
                res = dp[j] * dp[num-j]
                dp[num] = max(dp[num],res)
        return dp[n]