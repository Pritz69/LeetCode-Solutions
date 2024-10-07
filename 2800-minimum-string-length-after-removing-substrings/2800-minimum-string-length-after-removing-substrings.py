class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for ch in s:
            # Check the last two characters in the stack to remove "AB" or "CD"
            if st and ((st[-1] == 'A' and ch == 'B') or (st[-1] == 'C' and ch == 'D')):
                st.pop()  # Remove the last character from the stack
            else:
                st.append(ch)  # Append the current character to the stack
        return len(st)