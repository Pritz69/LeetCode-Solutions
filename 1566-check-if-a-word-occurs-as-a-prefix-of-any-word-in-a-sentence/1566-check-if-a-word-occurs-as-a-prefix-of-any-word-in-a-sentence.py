class Solution:
    def isPrefixOfWord(self, sentence: str, searchword: str) -> int:
        l=sentence.split(" ")
        n=len(l)
        for i in range(n) :
            if l[i][:len(searchword)]==searchword :
                return i+1
        return -1