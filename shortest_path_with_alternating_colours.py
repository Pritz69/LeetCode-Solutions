class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=collections.defaultdict(list)
        blue=collections.defaultdict(list)
        for src,dst in redEdges :
            red[src].append(dst)
        for src,dst in blueEdges :
            blue[src].append(dst)
        ans=[-1 for i in range(n)]
        q=deque()
        q.append([0,0,None])
        visit=set()
        visit.add((0,None))
        while q :
            node,length,colour = q.popleft()
            if ans[node]== -1 :
                ans[node]=length
            if colour != 'Red' :
                for nei in red[node] :
                    if (nei,"Red") not in visit :
                        visit.add((nei,"Red"))
                        q.append([nei,length+1,"Red"])
            if colour != 'Blue' :
                for nei in blue[node] :
                    if (nei,"Blue") not in visit :
                        visit.add((nei,"Blue"))
                        q.append([nei,length+1,"Blue"])           
        return ans
            
