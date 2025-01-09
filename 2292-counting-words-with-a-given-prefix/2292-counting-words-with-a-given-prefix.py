class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(pref)
        c=0
        for x in words :
            if pref==x[:n] :
                c +=1
        return c