class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=''
        for x in num :
            s += str(x)
        s =int(int(s)+k)
        l=[int(x) for x in str(s)]
        return l
