class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,r=0,0
        d={}
        m=0
        ans=0
        n=len(nums) 
        while r < n :
            x=nums[r]
            d[x]=d.get(x,0)+1
            while l<r and d[x] > k :
                d[nums[l]]=d.get(nums[l],0)-1
                l +=1
            ans=max(ans,(r-l)+1)
            r +=1
        return ans
