class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def f(x) :
            ans=0
            c=0
            for i in range(len(bloomDay)) :
                if bloomDay[i] <= x :
                    c +=1
                    if c==k :
                        ans +=1
                        c=0
                else :
                    c=0
            return ans
        if m*k > len(bloomDay) :
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        fans=0
        while l<=r :
            mid=(l+r)//2
            if f(mid) >= m :
                fans=mid
                r=mid-1
            else :
                l=mid+1
        return fans