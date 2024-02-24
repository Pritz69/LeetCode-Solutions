class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans=set([0,firstPerson])
        time={}
        for s,d,t in meetings :
            if t not in time :
                time[t]=defaultdict(list)
            time[t][s].append(d)
            time[t][d].append(s)
        def dfs(src,adj) :
            if src in visit :
                return
            visit.add(src)
            ans.add(src)
            for neigh in adj[src] :
                dfs(neigh,adj)
            
        for tm in sorted(time.keys()) :
            visit=set()
            for src in time[tm] :
                if src in ans :
                    dfs(src,time[tm])
        return list(ans)
