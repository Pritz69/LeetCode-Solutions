class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N=len(nums)
        l,r=0,sum(nums)
        min=10**20
        mini=0
        for i in range(N):
            l +=nums[i]
            r -=nums[i]
            if i+1 == N:
                res=abs(l//(i+1))
            else :
                res=abs(l//(i+1) - r//(N-i-1))
            if res < min :
                min=res
                mini=i 
        return mini
