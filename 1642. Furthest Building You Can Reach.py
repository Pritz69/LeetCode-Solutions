class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h=[]
        for i in range(len(heights)-1) :
            d=heights[i+1]-heights[i]
            if d<=0:
                continue
            bricks -= d
            heapq.heappush(h,-d)
            if bricks<0 :
                if ladders==0 :
                    return i
                ladders -=1
                x=heapq.heappop(h)
                bricks += -x
        return len(heights)-1
