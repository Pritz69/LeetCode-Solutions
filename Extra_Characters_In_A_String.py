class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp={}
        words=set(dictionary)
        def dfs(i) :
            if i==len(s) :
                return 0
            if i in dp :
                return dp[i]
            res = 1 + dfs(i+1)
            for j in range(i,len(s)) :
                if s[i:j+1] in words :
                    res = min(res,dfs(j+1))
            dp[i]=res
            return res
        return dfs(0)
