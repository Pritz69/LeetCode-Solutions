class Solution:
    def minimumLength(self, s: str) -> int:
        d=defaultdict(list)
        for i,x in enumerate(s) :
            d[x].append(i)
            if len(d[x])==3 :
                d[x].pop(0)
                d[x].pop(1)
        s=0
        for x in d :
            s +=len(d[x])
        return s
        