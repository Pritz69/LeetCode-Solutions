class Solution:
    def checkRecord(self, s: str) -> bool:
        s=list(s)
        c=0
        l=0
        m=-float('infinity')
        for i in s :
            if i=='L' :
                l +=1
            elif i=='A' :
                c +=1
                l=0
            elif i=='P' :
                l=0
            m=max(m,l)
        if c<2 and m<3 :
            return True
        else :
            return False
