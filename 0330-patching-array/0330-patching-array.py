class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        c=0
        reach=0
        i=0
        while reach < n :
            if i >= len(nums) :
                reach += reach + 1
                c +=1
            elif i<len(nums) and nums[i] <= reach + 1 :
                reach += nums[i]
                i +=1
            else :
                reach += reach + 1
                c +=1
        return c
