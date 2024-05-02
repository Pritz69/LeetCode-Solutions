class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s=set(nums)
        f=0
        m=float('-inf')
        for x in nums :
            if -x in s :
                f=1
                m=max(m,x)
        if f==0 :
            return -1
        return m
