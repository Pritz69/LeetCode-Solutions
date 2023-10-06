class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        def rec(num) :
            if num in dp :
                return dp[num]
            dp[num]= 0 if num==n  else num
            for i in range(1,num) :
                val = rec(i)  * rec(num-i)
                dp[num] = max(dp[num],val)
            return dp[n]

        return rec(n)