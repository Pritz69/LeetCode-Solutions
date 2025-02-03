class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        li=1
        p=nums[0]
        n=len(nums)
        ans=1
        ld=1
        pd=nums[0]
        for i in range(1,n) :
            if nums[i] > p :
                li +=1
                ans=max(ans,li)
                ld=1
            elif nums[i] < pd :
                ld +=1
                ans=max(ans,ld)
                li=1
            else :
                ld=1
                li=1
            p=nums[i]
            pd=nums[i]
        return ans