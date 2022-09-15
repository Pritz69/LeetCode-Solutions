class Solution:
    def singleNumber(self, nums: List[int]) -> int:

      counts=collections.Counter(nums)
      for x in sorted(counts):
        if counts[x] is 1:
            return x 
