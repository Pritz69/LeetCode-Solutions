class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        v=[0]*len(rocks)
        for i in range(len(rocks)):
            v[i]=capacity[i]-rocks[i]
        v.sort()
        c=0
        for i in v :
            if i=='0' :
                c +=1 
            else :
                if additionalRocks >= i :
                    additionalRocks -= i
                    c +=1 
                else :
                    break
        return c
            
