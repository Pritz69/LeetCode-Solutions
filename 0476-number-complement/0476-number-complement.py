class Solution:
    def findComplement(self, num: int) -> int:
        st=""
        while num :
            st = str(num%2) +st
            num = num//2
        ans=""
        for x in st :
            if x=="0" :
                ans += "1"
            else :
                ans += "0"
        ans.lstrip("0")
        a=0
        p=1
        for i in range(len(ans)-1,-1,-1) :
            a=a + int(ans[i])*p
            p *=2
        return a