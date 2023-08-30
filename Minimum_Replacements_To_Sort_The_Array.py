class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        mv=nums[-1]
        for i in range(len(nums)-2,-1,-1) :
            parts= math.ceil(nums[i]/mv)
            ans += parts-1
            mv = nums[i]//parts
        return ans
