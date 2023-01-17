class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res=0
        c=0
        for i in s :
            if i=='1' :
                c +=1 
            else :
                res = min(res+1,c)
        return res
