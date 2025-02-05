class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2 :
            return True
        c=0
        s=set()
        d=set()
        n=min(len(s1),len(s2))
        for i in range(n) :
            if s1[i] != s2[i] :
                c +=1
                s.add(s1[i])
                d.add(s2[i])
            if c > 2 :
                return False
        return s==d