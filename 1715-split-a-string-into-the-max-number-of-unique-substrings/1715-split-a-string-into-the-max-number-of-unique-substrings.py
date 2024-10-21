class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i,se) :
            if i==len(s):
                return 0
            res=0
            for j in range(i,len(s)) :
                substr=s[i:j+1]
                if substr in se :
                    continue
                se.add(substr)
                res=max(res,1+dfs(j+1,se))
                se.remove(substr)
            return res
        return dfs(0,set())