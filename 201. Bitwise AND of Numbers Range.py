class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c=0
        while left != right :
            left = left >>1
            right = right >>1
            c +=1
        return left << c
