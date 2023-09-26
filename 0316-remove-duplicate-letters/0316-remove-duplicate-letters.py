class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        st = []
        se = set()
        for x in s:
            if x not in se:
                while st and x < st[-1] and d[st[-1]] > 0:
                    se.remove(st.pop())
                st.append(x)
                se.add(x)
            d[x] -= 1
        return ''.join(st)