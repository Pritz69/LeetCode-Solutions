class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        li=1
        p=nums[0]
        n=len(nums)
        ans=1
        ld=1
        for i in range(1,n) :
            if nums[i] > p :
                li +=1
                ld=1
            elif nums[i] < p :
                ld +=1
                li=1
            else :
                ld=1
                li=1
            p=nums[i]
            ans=max(ans,max(li,ld))
        return ans