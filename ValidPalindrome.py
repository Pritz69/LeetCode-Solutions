class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(e for e in s if e.isalnum())
        l,r=0,len(s)-1
        f=0
        while l<=r:
            if s[l]!=s[r]:
                f=1
                return False
            l +=1
            r -=1
        if f==0:
            return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(e for e in s if e.isalnum())
        reverseStr = s[::-1]  

        if s != reverseStr:
            return False
        return True
