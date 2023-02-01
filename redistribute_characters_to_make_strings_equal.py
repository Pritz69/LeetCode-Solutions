class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d=dict()
        c=0
        for w in words :
            c +=1
            for x in w :
                if x in d :
                    d[x] +=1
                else :
                    d[x] =1
        for k in d :
            if d[k]%c != 0 :
                return False
        return True
