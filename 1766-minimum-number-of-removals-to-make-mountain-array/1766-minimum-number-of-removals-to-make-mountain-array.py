class Solution:
    def minimumMountainRemovals(self, A: List[int]) -> int:
        dpf = [1] * len(A)
        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    dpf[i] = max(dpf[i], 1 + dpf[j])       
        dpb = [1] * len(A)
        for i in range(len(A)):
            for j in range(i - 1, -1, -1):
                if A[i] > A[j]:
                    dpb[i] = max(dpb[i], 1 + dpb[j])
        maxlen = 0
        for i in range(1, len(A) - 1):
            if dpf[i] > 1 and dpb[i] > 1: 
                maxlen = max(dpf[i] + dpb[i] - 1, maxlen)
        return len(A) - maxlen  