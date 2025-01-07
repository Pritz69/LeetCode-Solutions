class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        n=len(words)
        for i in range(n) :
            for j in range(n) :
                if i!=j :
                    if words[i] in words[j] :
                        ans.append(words[i])
                        break
        return ans