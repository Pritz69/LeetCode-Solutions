class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans=[]
        word=set(wordDict)
        def rec(ind,res) :
            if ind==len(s) :
                ans.append(' '.join(res))
            for i in range(ind,len(s)) :
                wd=s[ind:i+1]
                if wd in word :
                    res.append(wd)
                    rec(i+1,res)
                    res.pop()
        rec(0,[])
        return ans
