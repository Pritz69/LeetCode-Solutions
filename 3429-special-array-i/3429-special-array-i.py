class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1 :
            return True
        for i in range(1,len(nums)) :
            if (nums[i]&1)==1 and (nums[i-1]&1)==1 or (nums[i]&1)==0 and (nums[i-1]&1)==0  :
                return False
        return True