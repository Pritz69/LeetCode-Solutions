class Solution:
    def numberOfSubarrays(self, A, k):
        i = count = res = 0
        for j in range(len(A)):
            if A[j] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += A[i] & 1
                i += 1
                count += 1
            res += count
        return res