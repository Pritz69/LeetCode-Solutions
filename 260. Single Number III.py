class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xo=0
        for x in nums :
            xo=xo^x
        rightbitturnedon = (xo&(xo-1))^xo
        b1,b0=0,0
        for x in nums :
            if x & rightbitturnedon == 0 :
                b0=b0^x
            else :
                b1=b1^x
        return [b0,b1] 
