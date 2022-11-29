class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(opn,clse):
            if opn==clse==n:
                res.append("".join(stack))
                return 
            if opn<n:
                stack.append('(')
                backtrack(opn+1,clse)
                stack.pop()
            if clse<opn:
                stack.append(')')
                backtrack(opn,clse+1)
                stack.pop()
        backtrack(0,0)
        return res
