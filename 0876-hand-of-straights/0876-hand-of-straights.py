class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        d={}
        for x in hand :
            d[x]=d.get(x,0)+1
        mh=list(d.keys())
        heapq.heapify(mh)
        while mh :
            start=mh[0]
            for i in range(start,start+groupSize) :
                if i not in d :
                    return False
                d[i] -=1
                if d[i]==0 :
                    if i != mh[0] :
                        return False
                    heapq.heappop(mh)
        return True    
