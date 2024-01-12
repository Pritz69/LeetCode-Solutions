class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1,c2=0,0
        i=0
        while i < len(s)//2 :
            if s[i] in "aeiouAEIOU" :
                c1 +=1
            i +=1
        i=len(s)//2
        while i < len(s) :
            if s[i] in "aeiouAEIOU" :
                c2 +=1
            i +=1
        return c1==c2
