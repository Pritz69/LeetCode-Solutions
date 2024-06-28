class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={}
        for x in roads :
            d[x[0]]=d.get(x[0],0) +1
            d[x[1]]=d.get(x[1],0) +1
        d=sorted(d.items(),key=lambda x:(x[1]),reverse=True)
        ans=0
        for x in d :
            ans += x[1] * n
            n -=1
        return ans 