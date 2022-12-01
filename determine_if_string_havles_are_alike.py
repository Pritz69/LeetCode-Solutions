class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a,b=0,0
        for i in s[:len(s)//2] :
            if i in 'aeiouAEIOU':
                a +=1 
        for i in s[len(s)//2:] :
            if i in 'aeiouAEIOU':
                b +=1
        if a==b:
            return True
        else :
            return False
