class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x,y=0,0
        d={}
        l=[]
        for s in secret :
            d[s] = d.get(s,0) + 1
        for i in range(len(secret)) :
            if secret[i]==guess[i] :
                x +=1
                d[secret[i]] -=1
            else :
                l.append(i)
        for i in l :
            if guess[i] in d :
                if d[guess[i]] >=1 :
                    y +=1
                    d[guess[i]] -=1
        ans=""
        ans +=str(x)
        ans +='A'
        ans +=str(y)
        ans +="B"
        return ans
        
