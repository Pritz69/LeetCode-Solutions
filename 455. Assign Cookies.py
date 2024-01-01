class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i,j=0,0
        c=0
        while i < len(g) and j <len(s) :
            if s[j]>=g[i] :
                i +=1
                j +=1
                c +=1
            else :
                i +=1
        return c
