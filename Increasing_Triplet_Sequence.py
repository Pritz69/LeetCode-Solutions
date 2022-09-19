class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) <= 2:
            return False
        
        i = j = k = float('inf')
        for idx,val in enumerate(nums):
            if val <= i:
                i = val
            elif val <= j:
                j = val
            else:
                return True
            
        return False
