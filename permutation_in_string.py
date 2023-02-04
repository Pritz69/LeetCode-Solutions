class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2) :
            return False
        s1c=[0]*26
        s2c=[0]*26
        for i in range(len(s1)) :
            s1c[ord(s1[i])-ord('a')] +=1
            s2c[ord(s2[i])-ord('a')] +=1
        match=0
        for i in range(26) :
            if s1c[i]==s2c[i] :
                match +=1
        l=0
        for r in range(len(s1),len(s2)) :
            if match==26 :
                return True
            ind=ord(s2[r])-ord('a')
            s2c[ind] +=1
            if s1c[ind] == s2c[ind] :
                match +=1
            elif s1c[ind] + 1 ==s2c[ind] :
                match -=1

            ind=ord(s2[l])-ord('a')
            s2c[ind] -=1
            if s1c[ind] == s2c[ind] :
                match +=1
            elif s1c[ind] - 1 ==s2c[ind] :
                match -=1
            l +=1
        return match == 26 
            
