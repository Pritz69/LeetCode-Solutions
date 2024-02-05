class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=defaultdict(list)
        for i,v in enumerate(s) :
            d[v].append(i)
        f=0
        for x in d :
            if len(d[x])==1 :
                f=1
        if f==0 :
            return -1
        d=dict(sorted(d.items(),key=lambda x:x[1]))
        for x in d :
            if len(d[x])==1 :
                return d[x][0]
