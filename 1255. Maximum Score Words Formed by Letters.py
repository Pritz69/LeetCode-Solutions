class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans=[]
        for x in words :
            v=0
            for c in x :
                v += score[ord(c)-97]
            ans.append((v,x))
        d={}
        for x in letters :
            d[x]=d.get(x,0)+1
        mans=0
        def rec(i,s) :
            nonlocal mans
            if i==len(ans) :
                mans=max(mans,s)
                return
            v=ans[i][0]
            w=ans[i][1]
            f=0
            for c in w :
                d[c]=d.get(c,0)-1
                if d[c] < 0 :
                    f=1
            if f==0 :
                rec(i+1,s+v)
            for c in w :
                d[c]=d.get(c,0)+1
            rec(i+1,s)
        rec(0,0)
        return mans
