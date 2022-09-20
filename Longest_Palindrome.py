class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        output = 0

        for count in c.values():
            output += int(count/2) * 2
        if output < len(s):
            output+=1
        return output
