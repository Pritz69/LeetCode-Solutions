class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1) :
            dp[i]=dp[i-2]+dp[i-1]
        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        for i in range(n) :
            c=a+b
            a=b
            b=c
        return c
