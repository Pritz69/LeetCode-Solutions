class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # First, we find the largest circle.
        n, maxc = len(favorite), 0
        seen = [-1] * n
        for idx in range(n):
            if seen[idx] == -1:
                cur_people = idx
                curset = set()
                count = 0
                while seen[cur_people] == -1:
                    seen[cur_people] = count
                    count += 1
                    curset.add(cur_people)
                    cur_people = favorite[cur_people]
					
                if cur_people in curset:
                    circleCount = len(curset) - seen[cur_people] # length - index of previous seen element
                    maxc = max(maxc, circleCount)
		
        # BFS for max leaf depth
        def getArmLength(a,b):
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
            return maxa
        
        # Then we try to find the sum of largest arms. Firstly, find all mutal-favorite peoples.
        res, pair = 0, []
        visited = [0] * n
        child = collections.defaultdict(list)
        for i in range(n):
            # create graph
            child[favorite[i]].append(i)
            
            # find pair
            if favorite[favorite[i]] == i and visited[i] == 0:
                pair.append([i, favorite[i]])
                visited[i] = visited[favorite[i]] = 1
        
        for a, b in pair:
            maxa = getArmLength(a,b)
            maxb = getArmLength(b,a)
            res += 2 + maxa + maxb
			
        return max(maxc, res)