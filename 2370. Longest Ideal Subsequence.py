class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0 for i in range(26)]
        n=len(s)
        ma=0
        for i in range(n) :
            idx=ord(s[i])-ord('a')
            dp[idx]=dp[idx]+1 
            for j in range(max(0,idx-k),min(25,idx+k)+1) :
                if j!=idx:
                    dp[idx]=max(dp[idx],dp[j]+1)
            ma=max(ma,dp[idx])
        return ma
