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
            else :
                li=1
            p=nums[i]
            if nums[i] < pd :
                ld +=1
                ans=max(ans,ld)
            else :
                ld=1
            pd=nums[i]
            print(li,ld)
        return ans