class Solution:
    def minimizedMaximum(self, n, A):
        left, right = 1, max(A)
        while left < right:
            x = (left + right) // 2
            if sum((a + x - 1) // x for a in A) > n:
                left = x + 1
            else:
                right = x
        return left