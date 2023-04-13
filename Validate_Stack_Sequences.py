class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        stack=[]
        for x in pushed :
            stack.append(x)
            while (i<len(popped) and stack and popped[i] == stack[-1]) :
                stack.pop()
                i +=1
        return not stack
