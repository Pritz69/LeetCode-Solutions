class Solution:
    def maxScore(self, s: str) -> int:
        o=0
        z=0
        for x in s :
            if x=='1' :
                o +=1
            else :
                z +=1
        if len(s)==o or len(s)==z:
            return len(s)-1
        m=0
        lz,lo=0,0
        for i in range(len(s)-1):
            if s[i]=='0' :
                lz +=1
            else :
                lo +=1
            m=max(m,(lz+(o-lo)))
        return m
