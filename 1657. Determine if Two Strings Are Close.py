class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2) :
            return False
        c1=Counter(word1)
        c2=Counter(word2)
        if c1==c2 :
            return True
        l1=[]
        l2=[]
        for x in c1 :
            l1.append(c1[x])
        for x in c2 :
            l2.append(c2[x])
        if sorted(l1)!=sorted(l2) or set(word1) != set(word2) :
            return False
        return True
