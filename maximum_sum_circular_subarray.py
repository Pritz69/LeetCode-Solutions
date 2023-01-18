class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax,gmin,t,cmax,cmin=nums[0],nums[0],0,0,0
        for n in nums :
            t +=n 
            cmax=max(cmax+n,n)
            gmax=max(gmax,cmax)
            cmin=min(cmin+n,n)
            gmin=min(cmin,gmin)
        if gmax > 0 :
            return max(gmax,t-gmin)
        else :
            return gmax
