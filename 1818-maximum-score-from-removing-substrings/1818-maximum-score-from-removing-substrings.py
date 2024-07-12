class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def func(pair,sc) :
            nonlocal s
            ans=0
            st=[]
            for x in s :
                if x==pair[1] and st and st[-1]==pair[0] :
                    ans += sc
                    st.pop()
                else :
                    st.append(x)
            s="".join(st)
            return ans
        res=0
        if x > y :
            res += func("ab",x)
            res += func("ba",y)
        else :
            res += func("ba",y)
            res += func("ab",x)
        return res