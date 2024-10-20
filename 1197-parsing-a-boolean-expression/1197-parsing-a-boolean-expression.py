class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        stack = []
        for i in range(len(e)):
            c = e[i]
            if c == ',':
                continue
            elif c == 't':
                stack.append(True)
            elif c == 'f':
                stack.append(False)
            elif c in ['&', '|', '!','(']:
                stack.append(c)
            elif c == ')':
                operands = []
                while stack[-1] != '(':
                    operands.append(stack.pop())
                stack.pop() # pop out '('.
                operator = stack.pop()
                if operator == '&':
                    stack.append(all(operands))
                elif operator == '|':
                    stack.append(any(operands))
                elif operator == '!':
                    stack.append(not operands[0])
        return stack.pop()