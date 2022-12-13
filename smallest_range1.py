class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums) - k
        mini = min(nums) + k
        return max(0, maxi - mini)
