class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=float('-inf')
        p,s=1,1
        for i in range(len(nums)) :
            if p==0 :
                p=1
            if s==0 :
                s=1
            p=p*nums[i]
            s=s*nums[len(nums)-i-1]
            m=max(m,p,s)
        return m
