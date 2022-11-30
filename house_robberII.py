class Solution:
    def robInLine(self, nums):
        mem = [0] * (len(nums) + 2)
        for idx in range(len(nums)-1,-1,-1):
            mem[idx] = max(nums[idx] + mem[idx+2], mem[idx+1])
        return mem[0]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robInLine(nums[1:]), self.robInLine(nums[:-1]))
