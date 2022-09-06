class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        o=True
        for i in range(len(s)) :
            if s[i] != s[(len(s))-i-1] :
                o=False
        if o is False :
            return False
        return True
