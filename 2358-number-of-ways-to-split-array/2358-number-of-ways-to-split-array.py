class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        ps=[0]*n
        ps[0]=nums[0]
        for i in range(1,n):
            ps[i]=ps[i-1]+nums[i]
        ans=0
        for i in range(n-1) :
            l=ps[i]
            r=ps[n-1]-ps[i]
            if l >= r :
                ans +=1
        return ans
