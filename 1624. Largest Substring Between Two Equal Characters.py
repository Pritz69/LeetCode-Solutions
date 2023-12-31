class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c,m=0,0
        f=0
        for i in range(len(s)) :
            c=0
            for j in range(i+1,len(s)) :
                if s[j] == s[i] :
                    f=1
                    m=max(m,c)
                c +=1
        return -1 if f==0 else m


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d=defaultdict(list)
        for i in range(len(s)) :
            d[s[i]].append(i)
        ans=0
        f=0
        for x in d :
            if len(d[x])>1 :
                f=1
                ans=max(ans,d[x][-1]-d[x][0]-1)
        return ans if f==1 else -1
