class Solution:
    def compressedString(self, word: str) -> str:
        ans=""
        n=len(word)
        p=word[0]
        c=1
        for i in range(1,n) :
            if word[i]==p :
                c +=1
            else :
                while c > 9 :
                    ans +='9'
                    ans +=p
                    c -= 9
                ans +=str(c)
                ans +=p
                p=word[i]
                c=1
        while c > 9 :
            ans +='9'
            ans +=p
            c -= 9
        ans +=str(c)
        ans +=p
        return ans