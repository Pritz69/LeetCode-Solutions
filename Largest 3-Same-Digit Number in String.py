class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m=0
        f=0
        for i in range(len(num)-2) :
            if num[i]==num[i+1]==num[i+2] :
                m=max(m,int(num[i]))
                f=1
        if f==0 :
            return ""
        else :
            return str(m)*3
