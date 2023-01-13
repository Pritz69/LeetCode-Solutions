class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g=defaultdict(list)
        for ch,par in enumerate(parent) :
            g[par].append(ch)
        ans=1
        def dfs(node) :
            nonlocal ans
            lon,slon=0,0
            for ch in g[node] :
                pl=dfs(ch)
                if s[ch]!=s[node] :
                    if pl > lon :
                        slon=lon
                        lon=pl
                    elif pl > slon :
                        slon=pl 
            ans=max(ans,lon+slon+1)
            return lon+1
        dfs(0)
        return ans
