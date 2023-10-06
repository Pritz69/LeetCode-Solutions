# Linear
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3 :
            return n-1
        if n==4 :
            return 4
        res=1
        while n > 4 :
            n -=3
            res *= 3
        return n*res
# Top Down
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

# Bottom Up
class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        for num in range(2,n+1):
            dp[num]=0 if num==n else num
            for i in range(1,num):
                val=dp[i]*dp[num-i]
                dp[num]=max(dp[num],val)
        return dp[n]
