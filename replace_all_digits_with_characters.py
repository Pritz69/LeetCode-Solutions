class Solution:
    def replaceDigits(self, s: str) -> str:
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)
        
