class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=0
        r=max(position)-min(position)
        def func(x) :
            place=1
            curr=0
            for i in range(1,len(position)) :
                if position[i]-position[curr] >=x :
                    place +=1
                    curr=i
            return place
        ans=0
        while l <= r :
            mid=(l+r)//2
            value=func(mid)
            if value >= m  :
                ans=mid
                l=mid+1
            else :
                r=mid-1
        return ans