class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=[]
        for i in range(len(s)) :
            l.append(abs(ord(s[i])-ord(t[i])))
        m=0
        p,i=0,0
        sm=0
        #print(l)
        while i < len(l) :
            sm += l[i]
            while p < len(l) and sm > maxCost :
                sm -=l[p]
                p +=1
            m=max(m,(i-p)+1)
            i +=1
        return m
