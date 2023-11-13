class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        c=[]
        for x in s :
            if x in "AEIOUaeiou" :
                v.append(x)
            else :
                c.append(x)
        v.sort()
        ans=[]
        i,j=0,0
        for k,x in enumerate(s) :
            if x in "AEIOUaeiou" :
                ans.append(v[i])
                i +=1
            else :
                ans.append(c[j])
                j +=1
        return ''.join(ans)