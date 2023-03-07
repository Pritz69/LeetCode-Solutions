class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=1
        tmin=min(time)
        right=tmin*totalTrips
        def func(mid) :
            ttrips=0
            for x in time :
                ttrips += mid//x
            return ttrips
        while left < right :
            m= (left+right)//2
            totalc = func(m)
            if totalc < totalTrips :
                left=m +1
            else :
                right=m
        return left
