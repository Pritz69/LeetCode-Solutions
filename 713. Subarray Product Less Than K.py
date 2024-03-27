class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r=0,0
        n=len(nums)
        p=1
        ans=0
        while r < n :
            p = p * nums[r]
            while l<r and p >= k :
                p=p//nums[l]
                l +=1
            if p < k :
                ans += (r-l)+1
            r +=1
        return ans
