class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        lo, hi = 1, n + 1
        while lo < hi:
            mid = (lo + hi) // 2 
            left_sum = (mid - 1) * mid // 2
            right_sum = total_sum - left_sum - mid
            if left_sum < right_sum:
                lo = mid + 1
            else:
                hi = mid
        return lo if lo * (lo - 1) // 2 == total_sum - (lo + 1) * lo // 2 else -1
