class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mini, maxi, bound, cnt = -1, -1, -1, 0
        for i, val in enumerate(nums):
            if val < minK or val > maxK: bound = i
            if val == minK: mini = i
            if val == maxK: maxi = i
            cnt += max(0, min(mini, maxi) - bound)
        return cnt