class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_ind = []
        b_ind = []
        x = len(a)
        y = len(b)
        for i in range(len(s)):
            if s[i] == a[0] and s[i:i+x] == a:
                a_ind.append(i)
            if s[i] == b[0] and s[i:i+y] == b:    
                b_ind.append(i)
        res = []
        i=j=0
        print(a_ind,b_ind)
        while i < len(a_ind) and j < len(b_ind):
            diff = abs(a_ind[i] - b_ind[j])
            if diff <= k:
                res.append(a_ind[i])
                i += 1
            elif a_ind[i] < b_ind[j]:
                i += 1
            else:
                j += 1
        return res
