class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mf=defaultdict(int)
        for x in words2 :
            for c in x :
                mf[c]=max(mf[c],x.count(c))
        ans=[]
        print(mf)
        for x in words1 :
            c=True
            for c in mf :
                if x.count(c) < mf[c] :
                    c=False
                    break
            if c :
                ans.append(x)
        return ans
