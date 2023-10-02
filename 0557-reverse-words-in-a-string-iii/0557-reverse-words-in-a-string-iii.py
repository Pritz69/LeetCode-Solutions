class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        for w in s.split() :
            rw=""
            for x in w :
                rw = x + rw
            ans += rw + " "
        
        return ans.strip()