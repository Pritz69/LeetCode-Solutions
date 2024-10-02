class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l=set(arr)
        l=list(l)
        l.sort()
        d={}
        for i in range(len(l)) :
            x=l[i]
            if x not in d :
                d[x]=d.get(x,0)+(i+1)
        ans=[]
        for x in arr :
            ans.append(d[x])
        return ans


        
