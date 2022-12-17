class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        t=Counter()
        b={}
        for c,i,v in zip(creators,ids,views) :
            t[c] +=v 
            if c not in b :
                b[c] =(v,i)
            elif v > b[c][0] :
                b[c] =(v,i)
            elif v==b[c][0] and i < b[c][1] :
                b[c] =(v,i)
        m=max(t.values())
        l=[]
        for c in t.keys():
            if t[c]==m :
                l.append([c,b[c][1]])
        return l
