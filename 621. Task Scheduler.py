class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for x in tasks :
            d[x]=d.get(x,0)+1
        ma=0
        for x in d :
            ma=max(ma,d[x])
        c=0
        for x in d :
            if d[x]==ma :
                c +=1
        ans=max(len(tasks),(ma-1)*(n+1) + c)
        return ans
