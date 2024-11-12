class Solution:
    def maximumBeauty(self, A, queries):
        A = sorted(A + [[0, 0]])
        for i in range(len(A) - 1):
            A[i + 1][1] = max(A[i][1], A[i + 1][1])
        return [A[bisect.bisect(A, [q + 1]) - 1][1] for q in queries]