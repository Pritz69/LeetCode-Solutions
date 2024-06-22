class Solution:
    def numberOfSubarrays(self, A, k):
        def atMost(k):
            res = i = 0
            c=0
            for j in range(len(A)):
                c += A[j] % 2
                while c > k:
                    c -= A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
