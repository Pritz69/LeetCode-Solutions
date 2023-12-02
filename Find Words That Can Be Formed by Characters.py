class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        for x in chars :
            d[x]=d.get(x,0)+1
        ans=0
        for x in words :
            if len(x) > len(chars) :
                continue
            di={}
            for c in x :
                di[c]=di.get(c,0)+1
            f=0
            for y in di :
                if y in d and di[y] <= d[y] :
                    continue
                else :
                    f=1
                    break
            if f==0 :
                ans += len(x)
        return ans
