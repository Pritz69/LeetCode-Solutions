class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1 :
            return True
        m=0
        i=0
        l=len(nums)
        while i < l and i <= m:
            x=nums[i]
            m=max(m,i+x)
            if m >= (l-1) :
                return True
            i=i+1
        return False
