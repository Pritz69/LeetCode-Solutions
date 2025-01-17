class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n=len(derived)
        if derived==[1] :
            return False
        if derived==[0] :
            return True
        a=[0]
        for i in range(n) :
            x=a[-1]^derived[i]
            a.append(x)
            if len(a)==n :
                break
        if a[0]^a[-1]==derived[n-1] :
            return True
        b=[1]
        for i in range(n) :
            x=b[-1]^derived[i]
            b.append(x)
            if len(b)==n :
                break
        if b[0]^b[-1]==derived[n-1] :
            return True
        return False