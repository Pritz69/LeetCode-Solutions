class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={}
        for x in roads :
            d[x[0]]=d.get(x[0],0) +1
            d[x[1]]=d.get(x[1],0) +1
        d=sorted(d.items(),key=lambda x:(x[1]),reverse=True)
        l=[]
        i=n
        for x in d :
            l.append((x[1],i))
            i -=1
        #print(l)
        ans=0
        for x in l :
            ans += x[0]*x[1]
        return ans 