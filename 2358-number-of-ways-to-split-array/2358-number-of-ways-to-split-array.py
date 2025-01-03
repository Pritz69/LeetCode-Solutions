class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ps=[0]*len(nums)
        ps[0]=nums[0]
        for i in range(1,len(nums)):
            ps[i]=ps[i-1]+nums[i]
        ans=0
        #print(ps)
        for i in range(len(nums)-1) :
            l=ps[i]
            r=ps[len(nums)-1]-ps[i]
            if l >= r :
                ans +=1
        return ans
