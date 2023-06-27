class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        d={}
        for x in words :
            if x[::-1] in d :
                d[x[::-1]] += 1
            else :
                d[x] =1
        c=0 
        for x in d :
            c += d[x]//2
        return c
