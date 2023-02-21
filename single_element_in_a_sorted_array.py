class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while (l<=r) :
            m=(l+r)//2
            if (((m-1)<0 or nums[m-1]!=nums[m]) and ((m+1)==len(nums) or nums[m+1]!=nums[m])) :
                return nums[m]
            lft=m-1 if nums[m-1]==nums[m] else m 
            if lft%2 ==0 :
                l=m+1
            else :
                r=m-1
        
