class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            w=words[i]
            if w[0] in 'aeiou' and w[-1] in 'aeiou' :
                c +=1
        return c
