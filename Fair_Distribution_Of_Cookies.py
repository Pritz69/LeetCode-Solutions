class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        d=[0]*k
        m=float('inf')
        def backtrack(i) :
            nonlocal m,d
            if i==len(cookies) :
                m=min(m,max(d))
                return m
            if m <= max(d) :
                return 
            for j in range(k) :
                d[j] += cookies[i]
                backtrack(i+1)
                d[j] -= cookies[i]
        backtrack(0)
        return m
