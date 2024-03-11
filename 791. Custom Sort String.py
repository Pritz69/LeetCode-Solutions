class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for x in s :
            d[x]=d.get(x,0)+1
        ans=""
        for x in order :
            if x in d :
                ans += x*d[x]
                d.pop(x)
        for x in d :
            ans += x*d[x]
        return ans        
