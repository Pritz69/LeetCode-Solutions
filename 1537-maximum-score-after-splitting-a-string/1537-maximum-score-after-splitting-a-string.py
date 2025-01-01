class Solution:
    def maxScore(self, s: str) -> int:
        m,n=0,len(s)
        l=r=''
        for i in range(1,n):
            l,r=s[:i],s[i:]
            c1=l.count('0')
            c2=r.count('1')
            m=max(m,c1+c2)
        return m