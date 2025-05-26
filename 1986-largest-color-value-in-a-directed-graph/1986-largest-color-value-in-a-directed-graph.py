class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        out = [[] for _ in range(n)]        # outgoing edges init
        for u, v in edges: out[u].append(v) # outgoing edges building of
        visit = [0] * n                     # 0-unvisited, -1 in current stack, 1 visited
        state = [defaultdict(int) for _ in range(n)]   # [node][letter] -> longest count of letters starting from this node
        def dfs(node):
            visit[node] = -1   # tmp on current path
            for u in out[node]:
                if visit[u] == -1: return -1   # cycle detedted
                if not visit[u]:               # call dfs on unvisited nodes
                    if dfs(u) == -1:    # if there was a cycle
                        return -1       # then return -1
                for k, val in state[u].items():                 # update the state for each letter in the child
                    state[node][k] = max(state[node][k], val)
            state[node][colors[node]] += 1                      # add the color of the node to the state
            visit[node] = 1                                     # mark visited
            return max(state[node].values())                    # longest color value for this node
        
        ret = 0
        for u in range(n):   # the main loop over all nodes
            if not visit[u]:
                r = dfs(u)
                if r == -1: return -1   # cycle detected
                ret = max(ret, r)
        return ret