class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        c=0
        for x in s :
            if o>0 and x==")" :
                o -=1
            elif x=="(" :
                o +=1
            else :
                c +=1
        return o+c