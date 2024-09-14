class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m=max(nums)
        ans=0
        l=0
        for i in range(len(nums)) :
            if nums[i]==m :
                l +=1
                ans=max(ans,l)
            else :
                l=0
        return ans