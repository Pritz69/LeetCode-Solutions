class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c={}
        for x in tasks :
            c[x] = c.get(x,0) + 1
        t=0
        q=deque()
        h=[]
        for x in c :
            h.append(-c[x])
        heapq.heapify(h)
        while h or q :
            t +=1
            if h :
                cnt = 1 + heapq.heappop(h)
                if cnt :
                    q.append([cnt,t+n])
            if q and q[0][1]==t :
                heapq.heappush(h, q.popleft()[0])
        return t
