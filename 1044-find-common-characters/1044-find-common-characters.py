class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[]
        d={}
        for i in range(26) :
            c=chr(97+i)
            m=float('inf')
            for w in words :
                cntc=0
                for ch in w :
                    if ch==c :
                        cntc +=1
                m=min(m,cntc)
            d[c]=d.get(c,0) + m
        for x in d :
            if d[x] > 0 :
                for i in range(d[x]) :
                    l.append(x)
        return l
