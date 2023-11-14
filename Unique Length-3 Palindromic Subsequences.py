class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        l=set()
        r={}
        for x in s:
            r[x]=r.get(x,0)+1
        for i in range(len(s)) :
            r[s[i]] -=1
            if r[s[i]]==0 :
                r.pop(s[i])
            for x in l :
                if x in r :
                    res.add((s[i],x))
            l.add(s[i])
        return len(res)
