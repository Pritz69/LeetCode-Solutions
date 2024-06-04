class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for x in s :
            d[x]=d.get(x,0)+1
        c=0
        f=0
        for x in d :
            if d[x]%2==0 :
                c +=d[x]
            else :
                f=1
                c +=d[x]-1
        return c+1 if f==1 else c