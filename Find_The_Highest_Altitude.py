class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]*(len(gain)+1)
        m=0
        for i in range(1,len(l)) :
            l[i]=l[i-1]+gain[i-1]
            m=max(m,l[i])
        return m
