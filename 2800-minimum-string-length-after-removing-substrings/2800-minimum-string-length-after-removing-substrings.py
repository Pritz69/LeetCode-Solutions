class Solution:
    def minLength(self, s: str) -> int:
        st = s[:2]  
        for i in range(2, len(s)):
            while len(st) >= 2 and (st[-2] + st[-1] == "AB" or st[-2] + st[-1] == "CD"):
                st = st[:-2]  
            
            st += s[i]
        
        while len(st) >= 2 and (st[-2] + st[-1] == "AB" or st[-2] + st[-1] == "CD"):
            st = st[:-2]
        
        return len(st)