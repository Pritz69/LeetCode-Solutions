class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        m=0
        for x in s :
            if x=="(" :
                c +=1
                m=max(m,c)
            elif x==")" :
                c -=1
            else :
                continue
        return m
