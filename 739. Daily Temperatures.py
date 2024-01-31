class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i, x in enumerate(temperatures):
            while st and x > temperatures[st[-1]]:
                index = st.pop()
                ans[index] = i - index
            st.append(i)
        return ans

        
