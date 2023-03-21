class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        c=0
        for i in range(len(nums)) :
            if nums[i]==0 :
                c +=1 
            else :
                c =0
            res +=c
        return res
