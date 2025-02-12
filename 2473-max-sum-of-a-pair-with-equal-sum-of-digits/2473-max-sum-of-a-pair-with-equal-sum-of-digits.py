class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for x in nums :
            s=0
            n=x
            while n :
                di=n%10
                s=s+di
                n=n//10
            d[s].append(x)
        m=-1
        for x in d :
            l=sorted(d[x])
            if len(l) >= 2 :
                m=max(m,l[-2]+l[-1])
        return m
