class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=int("".join(map(str, digits)))
        d+=1
        return list(str(d))
