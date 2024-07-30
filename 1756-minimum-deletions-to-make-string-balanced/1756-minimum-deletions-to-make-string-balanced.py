class Solution:
    def minimumDeletions(self, s: str) -> int:
        acountrt=0
        for i in range(len(s)) :
            acountrt +=1 if s[i]=='a' else 0
        bcountleft=0
        res=len(s)
        for i in range(len(s)) :
            if s[i]=='a' :
                acountrt -=1
            res=min(res, acountrt + bcountleft)
            if s[i]=='b' :
                bcountleft +=1
        return res