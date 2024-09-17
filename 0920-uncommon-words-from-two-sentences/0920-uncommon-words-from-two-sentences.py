class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c={}
        d={}
        for x in s1.split(" ") :
            c[x]=c.get(x,0)+1
        for x in s2.split(" ") :
            d[x]=d.get(x,0)+1
        ans=[]
        for x in c :
            if c[x]==1 and x not in d :
                ans.append(x)
        for x in d :
            if d[x]==1 and x not in c :
                ans.append(x)
        return ans
