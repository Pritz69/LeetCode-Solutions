class Solution:
    def minimumLength(self, s: str) -> int:
        d=defaultdict(int)
        for i,x in enumerate(s) :
            d[x] +=1
        s=0
        for x in d :
            if d[x]%2==0 :
                s +=2
            else :
                s +=1
        return s
        