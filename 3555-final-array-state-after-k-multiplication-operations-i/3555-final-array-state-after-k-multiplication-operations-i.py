class Solution:
    def getFinalState(self, v: List[int], k: int, m: int) -> List[int]:
        n = len(v)
        q = [(v[i], i) for i in range(n)]
        heapq.heapify(q)
        
        while k > 0:
            val, idx = heapq.heappop(q)
            v[idx] = val * m
            heapq.heappush(q, (val * m, idx))
            k -= 1
        
        return v
