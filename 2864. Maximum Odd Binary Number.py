class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o,z=0,0
        for x in s :
            if x=='1' :
                o +=1
            else :
                z +=1  
        if o==1 :
            return (len(s)-1)*'0' + '1'
        return (o-1)*'1' + z*'0' + '1'
