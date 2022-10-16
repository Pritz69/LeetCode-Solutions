class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=list(s.split())
        return len(l[-1])
