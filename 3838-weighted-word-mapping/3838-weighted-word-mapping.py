class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for x in words :
            s=0
            for c in x :
                i=ord(c)-96
                s=s+weights[i-1]
            s=s%26
            ansb=26-s
            ans += chr(96+ansb)
        return ans
