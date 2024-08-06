class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for x in word :
            d[x]=d.get(x,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        ans=0
        c=0
        for x in d :
            c +=1
            if c <=8 :
                ans += d[x]
            elif c <=16 :
                ans += d[x]*2
            elif c <=24 :
                ans += d[x]*3
            else :
                ans += d[x]*4
        return ans    
