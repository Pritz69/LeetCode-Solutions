class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for x in s :
            if x==")" :
                s=[]
                while st[-1] != "(" :
                   s.append(st.pop())
                st.pop()
                st += s
            else :
                st.append(x)
        return "".join(st)