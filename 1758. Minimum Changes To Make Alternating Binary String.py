class Solution:
    def minOperations(self, s: str) -> int:
        s0,s1=0,0
        for i in range(len(s)) :
            if i%2==0 :
                if s[i]=='0' :
                    s1 +=1
                else :
                    s0 +=1
            else :
                if s[i]=='1' :
                    s1 +=1
                else :
                    s0 +=1
        return min(s0,s1)

class Solution:
    def minOperations(self, s: str) -> int:
        l,l2=[],[]
        i=0
        while i < len(s) :
            if i%2==1 :
                l.append('0')
                l2.append('1')
            else :
                l.append('1')
                l2.append('0')
            i +=1
        c,c1=0,0
        for i in range(len(s)) :
            if s[i]!=l[i] :
                c +=1
            if s[i]!=l2[i] :
                c1 +=1
        return min(c,c1)

            
