class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s or s.count(i)<t.count(i):
                return i
