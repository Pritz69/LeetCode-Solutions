class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        m=0
        for x in c :
            m=max(m,c[x])
        s=0
        for x in c :
            if c[x]==m :
                s += c[x]
        return s