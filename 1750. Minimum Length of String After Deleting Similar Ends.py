class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j and s[i] == s[j]:
            while i < j and s[i] == s[i + 1]:
                i += 1
            while i < j and s[j] == s[j - 1]:
                j -= 1
            i += 1
            j -= 1
        if j<i :
            return 0
        return j - i + 1
