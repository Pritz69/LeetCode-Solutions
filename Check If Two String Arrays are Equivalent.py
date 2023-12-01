class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        for x in word1 :
            s +=x
        a=""
        for x in word2 :
            a +=x
        return a==s
