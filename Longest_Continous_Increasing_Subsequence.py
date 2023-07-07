class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l,r=0,1
        prev=nums[l]
        ans=1
        while r < len(nums) :
            if nums[r]>prev :
                ans = max(ans,r-l+1)
            else :
                l = r
            prev = nums[r]    
            r +=1
        return ans
