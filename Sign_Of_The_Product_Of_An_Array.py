class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for x in nums :
            p=p*x
        if p < 0 :
            return -1
        elif p==0 :
            return 0
        else :
            return 1
