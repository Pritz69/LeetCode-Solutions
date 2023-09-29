class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        fi=0
        fd=0
        for i in range(1,len(nums)) :
            if nums[i] > nums[i-1] :
                fi=1
            if nums[i] < nums[i-1] :
                fd=1
        if fi==1 and fd==1 :
            return False
        else :
            return True
