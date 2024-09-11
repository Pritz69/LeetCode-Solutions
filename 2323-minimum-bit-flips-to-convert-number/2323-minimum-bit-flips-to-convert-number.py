class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)[2:]
        n=len(s)
        g=bin(goal)[2:]
        m=len(g)
        if m < n :
            g = '0'*(n-m) + g
        else :
            s = '0'*(m-n) + s
        c=0
        for i in range(len(s)) :
            if s[i] != g[i] :
                c +=1
        return c