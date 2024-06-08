class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        d = {}
        currSum = 0
        
        for i in range(len(nums)):
            
            currSum = currSum + nums[i]
            mod = currSum%k
            
            if mod == 0 and i+1 >= 2:
                return True
                        
            if mod in d:
                if i - d[mod] >= 2:
                    return True
            else:
                d[mod] = i
                
        return False