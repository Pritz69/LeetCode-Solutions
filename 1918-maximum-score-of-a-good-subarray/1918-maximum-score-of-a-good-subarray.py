class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l=r=k
        res=nums[k]
        mi=nums[k]
        while l > 0 or r < len(nums)-1 :
            left = nums[l-1] if l > 0 else 0
            right = nums[r+1] if r < len(nums)-1 else 0
            if left > right :
                mi=min(mi,left)
                l -=1
            else :
                mi=min(mi,right)
                r +=1
            res = max(res,mi*(r-l+1))
        return res