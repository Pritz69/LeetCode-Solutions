class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(s[i])
            
        for i in range(len(t)):
            if t[i] == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(t[i])
        
        return s_stack == t_stack
