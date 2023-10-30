class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cbits(n) :
            s=""
            while n>0 :
                s += str(n%2)
                n //= 2
            return s.count('1')
        l=[]
        for x in arr :
            l.append((cbits(x),x))
        l.sort()
        nl=[]
        for x in l :
            nl.append(x[1])
        return nl