class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        c=0
        i=0
        while i < n :
            if s[i]!=s[i+1] :
                c=c+1
            i=i+2
        return c