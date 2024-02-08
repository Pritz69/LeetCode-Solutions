class Solution:
    def minFlips(self, target: str) -> int:
        n=len(target)
        s='0'*n
        if s==target:
            return 0
        while target[0]=='0' :
            target=target[1:]
        #print(target)
        p=target[0]
        c=1
        for x in target :
            if x==p :
                continue
            else :
                c +=1
            p=x
        return c
