class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c,a=0,0
        while c <len(s) and a <len(g) :
            if s[c] >= g[a] :
                a +=1
            c +=1 
        return a
