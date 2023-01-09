class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans=0
        for n in nums :
            ans=ans^n
        return ans
