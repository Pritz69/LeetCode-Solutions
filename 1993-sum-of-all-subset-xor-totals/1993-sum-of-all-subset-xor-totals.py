class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        def rec(i,x) :
            nonlocal ans
            if i==n :
                ans += x
                return
            rec(i+1,x^nums[i])
            rec(i+1,x)
        rec(0,0)
        return ans