class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        n=len(s)
        r=0
        w=0
        while r < n :
            if 65 <= ord(s[r]) <= 90 or 97 <= ord(s[r]) <= 122 :
                w +=1
            else :
                if w > 0 :
                    l=w
                w=0
            r +=1
        if w > 0 :
            l=w
        return l
