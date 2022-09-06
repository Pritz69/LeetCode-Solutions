class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum=0
        maxs=nums[0]
        for i in nums :
            if csum<0 :
                csum=0
            csum+=i
            maxs=max(maxs,csum)
        return maxs
