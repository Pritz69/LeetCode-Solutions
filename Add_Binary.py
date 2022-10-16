class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=int(a,2)+int(b,2)
        s=bin(s)
        return s[2:]
