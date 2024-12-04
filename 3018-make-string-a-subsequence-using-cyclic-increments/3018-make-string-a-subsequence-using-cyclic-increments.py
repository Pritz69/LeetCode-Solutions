class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        j, n, m = 0, len(s1), len(s2)
        for i in range(n):
            if j < m and (ord(s2[j]) - ord(s1[i])) % 26 <= 1:
                j += 1
        return j == m