class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(goal) :
            if goal < 0 :
                return 0
            c=0
            l,r=0,0
            n=len(nums)
            s=0
            while r < n :
                s += nums[r]
                while s > goal :
                    s -=nums[l]
                    l +=1
                c += (r-l+1)
                r +=1
            return c

        return func(goal)-func(goal-1)
