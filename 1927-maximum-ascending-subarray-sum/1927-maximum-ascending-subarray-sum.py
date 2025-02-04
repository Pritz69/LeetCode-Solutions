class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=max(nums)
        s=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                s +=nums[i]
            else :
                s = nums[i]
            ans=max(ans,s)
        return ans