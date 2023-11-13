class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        for x in s :
            if x=='A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u' :
                v.append(x)
        v.sort()
        i=0
        ans=[]
        for x in s :
            if x=='A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u' :
                ans.append(v[i])
                i +=1
            else :
                ans.append(x)
        return ''.join(ans)