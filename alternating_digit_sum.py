class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        n=list(str(n))
        for i in range(len(n)):
            if i%2 == 0 :
                s += int(n[i])
            else :
                s -= int(n[i])
        return s
