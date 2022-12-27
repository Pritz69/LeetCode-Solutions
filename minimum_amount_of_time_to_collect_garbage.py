class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p=0
        m=0
        g=0
        a=0
        for i,v in enumerate(garbage) :
            for c in v :
                if c=='P':
                    p=i
                elif c=='M' :
                    m=i
                elif c=='G' :
                    g=i
            a += len(v)
        for i in range(1,len(travel)):
            travel[i] +=travel[i-1]
        if p!=0:
            a +=travel[p-1]
        if m!=0:
            a +=travel[m-1]
        if g!=0:
            a +=travel[g-1]
        return a
