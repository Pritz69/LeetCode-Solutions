class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d={}
        for x in nums :
            d[x]=d.get(x,0)+1
        l=[]
        c=0
        while c!=len(nums) :
            nl=[]
            for x in d :
                if d[x]>0 :
                    nl.append(x)
                    d[x]-=1
                    c +=1
            l.append(nl)
        return l
