class Solution:
    def longestcommonsubsequence(self, s1:str , s2:str) ->int :
        m=len(s1)
        n=len(s2)
        dp=[[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(n-1,-1,-1) :
            for j in range(m-1,-1,-1) :
                if s1[i]==s2[j] :
                    dp[i][j] = 1 + dp[i+1][j+1]
                else :
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]

    def longestpalindromicsubsequence(self, st:str) ->int :
        return self.longestcommonsubsequence(st,st[::-1])

    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestpalindromicsubsequence(s)
