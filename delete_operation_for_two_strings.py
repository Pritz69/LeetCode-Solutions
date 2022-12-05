class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N,M=len(word1),len(word2)
        dp=[[0 for _ in range(N+1)]for _ in range(M+1)]
        for r in range(M+1):
            dp[r][0]=r
        for c in range(N+1):
            dp[0][c]=c
        for r in range(1,M+1):
            for c in range(1,N+1):
                if word1[c-1]==word2[r-1]:
                    dp[r][c]=dp[r-1][c-1]
                else :
                    dp[r][c]=1+min(dp[r-1][c],dp[r][c-1])
        return dp[-1][-1]
