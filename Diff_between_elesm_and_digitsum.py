class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        ds=0
        for i in nums :
            for x in str(i) :
                ds += int(x)
        return s-ds
