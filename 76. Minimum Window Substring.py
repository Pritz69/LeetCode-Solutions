class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) :
            return ""
        li=[-1,-1]
        m=float('inf')
        l,r=0,0
        se={}
        for x in t :
            se[x]=se.get(x,0)+1
        d={}
        while r < len(s) :
            if s[r] in se :
                d[s[r]]=d.get(s[r],0)+1
            while len(d)==len(se) :
                f=0
                for x in d :
                    if d[x] < se[x] :
                        f=1
                        break
                if f==1 :
                    break
                else : 
                    if r-l +1 < m :
                        m=r-l +1
                        li[0]=l
                        li[1]=r
                    if s[l] in d :
                        d[s[l]] -=1
                        if d[s[l]]==0 :
                            d.pop(s[l])
                    l +=1
            r +=1
        return s[li[0]:li[1]+1]
