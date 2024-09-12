class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        c=0
        for w in words :
            f=0
            for x in w :
                if x not in s:
                    f=1
                    break
            if f==0 :
                c +=1
        return c
            