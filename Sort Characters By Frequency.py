class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for x in s :
            d[x]=d.get(x,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        ns=""
        for x in d :
            ns =ns+ x*(d[x])
        return ns
