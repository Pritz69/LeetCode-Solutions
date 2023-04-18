class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        k=0
        for i in range(min(len(word1),len(word2))) :
            ans.append(word1[i])
            ans.append(word2[i])
            k +=1
        for i in range(k,len(word1)):
            ans.append(word1[i])
        for i in range(k,len(word2)) :
            ans.append(word2[i])
        return ''.join(ans)
