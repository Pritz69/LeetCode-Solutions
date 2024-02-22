class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dp=[0]*(n+1)
        for a,b in trust :
            dp[a] -=1
            dp[b] +=1
        for i in range(1,n+1) :
            if dp[i]==n-1 :
                return i
        return -1
