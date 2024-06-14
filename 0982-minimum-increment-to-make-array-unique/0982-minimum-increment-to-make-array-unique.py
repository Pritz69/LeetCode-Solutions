class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        last=-1
        ans=0
        nums.sort()
        for x in nums :
            if last < x :
                last=x
            else :
                last=last +1
                ans += last-x
        return ans