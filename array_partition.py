class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
      
      class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        for i in range(0,len(nums)-1,2):
            s += nums[i]
        return s
