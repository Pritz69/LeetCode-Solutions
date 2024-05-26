class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        def rec(i, a_count, l_count):
            if i == n:
                return 1
            if dp[i][a_count][l_count] != -1:
                return dp[i][a_count][l_count]
            count = 0
            count += rec(i + 1, a_count, 0)
            if a_count < 1:
                count += rec(i + 1, a_count + 1, 0)
            if l_count < 2:
                count += rec(i + 1, a_count, l_count + 1)
            dp[i][a_count][l_count] = count % MOD
            return dp[i][a_count][l_count]
        return rec(0, 0, 0)
