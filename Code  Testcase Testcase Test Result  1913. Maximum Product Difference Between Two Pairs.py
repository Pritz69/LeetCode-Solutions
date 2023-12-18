class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m,sm=0,0
        for x in nums :
            if x > m :
                sm=m
                m=x
            elif x>sm :
                sm=x
        mi,smi=float('inf'),float('inf')
        for x in nums :
            if x < mi :
                smi=mi
                mi=x
            elif x < smi :
                smi=x
        return (m*sm)-(mi*smi)
