class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        currentSubstring = ""
        for c in s:
            if c == '(':
                stack.append(currentSubstring)
                currentSubstring = ""
            elif c == ')':
                currentSubstring = stack.pop() + currentSubstring[::-1]
            else:
                currentSubstring += c
        return currentSubstring
