class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for x in matches :
            d[x[0]]=d.get(x[0],0)+0
            d[x[1]]=d.get(x[1],0)+1
        l=[]
        nw=[]
        nl=[]
        for x in d :
            if d[x]==0 :
                nw.append(x)
            elif d[x]==1 :
                nl.append(x)
        l.append(sorted(nw))
        l.append(sorted(nl))
        return l
