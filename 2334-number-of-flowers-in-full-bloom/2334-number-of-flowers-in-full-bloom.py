class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people=[(p,i) for i,p in enumerate(people)]
        start=[i[0] for i in flowers]
        end=[i[1] for i in flowers]
        res=[0]*len(people)
        heapq.heapify(start)
        heapq.heapify(end)
        count=0
        people.sort()
        for person,pos in people :
            while start and start[0] <= person :
                heapq.heappop(start)
                count +=1
            while end and end[0] < person :
                heapq.heappop(end)
                count -=1
            res[pos]=count
        return res
            