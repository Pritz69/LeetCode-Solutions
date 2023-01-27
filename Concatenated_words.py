class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset=set(words)
        def dfs (word) :
            for i in range(1,len(word)) :
                prefix=word[:i]
                suffix=word[i:]
                if ((prefix in wordset and suffix in wordset) or (prefix in wordset and dfs(suffix))) :
                    return True
        res=[]
        for w in words :
            if dfs(w) :
                res.append(w)
        return res
