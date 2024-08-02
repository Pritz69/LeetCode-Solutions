class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c=0
        for x in nums :
            if x==1 :
                c +=1
        nums += nums
        co=0
        l=0
        ma=0
        for r in range(len(nums)) :
            if nums[r]==1 :
                co +=1
            if (r-l)+1 == c :
                ma=max(ma,co)
                if nums[l]==1 :
                    co -=1
                l +=1
        return c-ma

