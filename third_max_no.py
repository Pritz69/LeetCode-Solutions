class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            return sorted(set(nums), reverse = True)[2] if len(set(nums)) >= 3 else max(nums)
    

    
