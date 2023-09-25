class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in t:
            ans =ans+ ord(c)

        for c in s:
            ans =ans- ord(c)           
        return chr(ans)


        