class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            odd=0
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -=1 
                r +=1
                odd +=1
            even=0
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -=1 
                r +=1
                even +=1
            c += even + odd
        return c
