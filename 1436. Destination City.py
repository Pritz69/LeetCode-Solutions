class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths)==1 :
            return paths[0][1]
        d={}
        for x in paths :
            d[x[0]]=d.get(x[0],0)+1
            d[x[1]]=d.get(x[1],0)+1
        for x in paths :
            if d[x[1]]==1 :
                return x[1]
