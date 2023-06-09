class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        v=ord(target)
        m=-1
        ans=''
        for x in letters :
            if ord(x) > v :
                m = ord(x)
                ans += x
                break
        if m==-1 :
            return letters[0]
        else :
            return ans
