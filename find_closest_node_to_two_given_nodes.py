class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj=collections.defaultdict(list)
        for i,dest in enumerate(edges) :
            adj[i].append(dest)
        def bfs(src,dmap) :
            q=deque()
            q.append([src,0])
            dmap[src]=0
            while q :
                node,dist = q.popleft()
                for nei in adj[node] :
                    if nei not in dmap :
                        q.append([nei,dist+1])
                        dmap[nei] =dist+1
        n1dist={}
        bfs(node1,n1dist)
        n2dist={}
        bfs(node2,n2dist)
        res=-1
        resd=float('inf')
        for i in range(len(edges)) :
            if  i in n1dist and i in n2dist :
                dist=max(n1dist[i],n2dist[i])
                if dist < resd :
                    resd=dist
                    res=i
        return res
            
