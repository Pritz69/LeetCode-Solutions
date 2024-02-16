class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for x in arr :
            d[x]=d.get(x,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1]))
        c=len(d)
        #print(d)
        for x in d :
            if k >= d[x] :
                k -= d[x]
                c -=1
                if k==0 :
                    break
            else :
                break
        return c
