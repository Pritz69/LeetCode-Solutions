class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        for i,x in enumerate(mat) :
            c=0
            for v in x :
                if v==1 :
                    c +=1
            l.append([c,i])
        l.sort()
        ans=[]
        for i in range(k) :
            ans.append(l[i][1])
        return ans
        