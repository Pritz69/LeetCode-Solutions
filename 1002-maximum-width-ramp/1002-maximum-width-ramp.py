class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        mri=[0]*n
        mri[n-1]=nums[n-1]
        for i in range(n-2,-1,-1) :
            mri[i]=max(nums[i],mri[i+1])
        l=0
        ans=0
        for r in range(n) :
            while nums[l] > mri[r] :
                l +=1
            ans=max(ans,r-l)
        return ans