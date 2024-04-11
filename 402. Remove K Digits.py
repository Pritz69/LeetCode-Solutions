class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for c in num :
            while k > 0 and st and st[-1] > c :
                st.pop()
                k -=1
            st.append(c)
        st=st[:len(st)-k]
        res = "".join(st).lstrip("0")
        return res if res else "0"
