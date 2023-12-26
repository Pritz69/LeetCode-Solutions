class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp={}
        mod=10**9 + 7
        def rec(i,s):
            if i==n:
                if s==target :
                    return 1
                return 0
            if (i,s) in dp :
                return dp[(i,s)]
            c=0
            for j in range(1,k+1) :
                c = (c + rec(i+1,s+j))%mod
            dp[(i,s)]=c
            return c
        return rec(0,0)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: there is one way to achieve a sum of 0
        dp[0][0] = 1

        for i in range(1, n + 1):
            for s in range(1, target + 1):
                for j in range(1, k + 1):
                    if s - j >= 0:
                        dp[i][s] = (dp[i][s] + dp[i - 1][s - j]) % mod

        return dp[n][target]
