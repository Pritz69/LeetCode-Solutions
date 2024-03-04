class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens :
            return 0
        tokens.sort()
        if power < tokens[0] :
            return 0
        i=0
        j=len(tokens)-1
        m=0
        c=0
        while i <= j :
            power -= tokens[i]
            c +=1
            m=max(m,c)
            i +=1
            while i<len(tokens) and power < tokens[i] :
                power += tokens[j]
                j -=1
                c -=1
        return m
