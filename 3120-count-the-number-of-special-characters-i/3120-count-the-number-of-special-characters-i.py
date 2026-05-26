class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in s and ch.upper() in s:
                ans += 1

        return ans