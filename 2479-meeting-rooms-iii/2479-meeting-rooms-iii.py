class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count=[0]*n
        available=[i for i in range(n)]
        used=[]
        for st,end in meetings :
            while used and st >= used[0][0] :
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)
            if not available :
                endtm,room=heapq.heappop(used)
                end=endtm+(end-st)
                heapq.heappush(available,room)
            room=heapq.heappop(available)
            heapq.heappush(used,(end,room))
            count[room] +=1
        return count.index(max(count))    