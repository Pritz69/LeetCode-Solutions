class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        for x in words :
            for c in x :
                d[c]=d.get(c,0)+1
        f=0
        #print(d)
        for x in d :
            if d[x]%len(words)!=0 :
                f=1
        return f==0
