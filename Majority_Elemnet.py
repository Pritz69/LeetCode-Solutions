class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      counts=collections.Counter(nums)
      n=len(nums)
      max_key = max(counts, key=counts.get)
      if counts[max_key] > n/2 :
            return max_key
