class Solution:
    def findComplement(self, num: int) -> int:
        s=list(bin(num)[2:])
        for i in range(len(s)):
            if s[i]=='0':
                s[i]='1' 
            elif s[i]=='1' :
                s[i]='0'
        return int(''.join(s),2)

