class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=[]
        for i in range(len(number)) :
            if number[i]==digit :
                l.append(i)
        ans=0
        for x in l :
            w=number[:x] + number[x+1:]
            ans=max(ans,int(w))
        return str(ans)
            
            
