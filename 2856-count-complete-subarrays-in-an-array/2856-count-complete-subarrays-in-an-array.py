class Solution:
    def countCompleteSubarrays(self, A: List[int]) -> int:
        n= len(A)
        k =len(set(A))
        res = i = 0
        count = Counter()
        for j in range(n):
            count[A[j]] += 1
            while len(count) == k:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    del count[A[i]]
                i += 1
            res += i
        return res