class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)
        for i in range(n) :
            adj[manager[i]].append(i)
        q = deque()
        q.append((headID,0))
        res = 0
        while q :
            i,t = q.popleft()
            res = max(res,t)
            for emp in adj[i] :
                q.append((emp,t + informTime[i]))
        return res
