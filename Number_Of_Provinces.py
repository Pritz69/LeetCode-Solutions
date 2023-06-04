class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(isConnected)) :
            for j in range(len(isConnected)) :
                if isConnected[i][j]==1 and i != j :
                    adj[i].append(j)
                    adj[j].append(i)
        def dfs(i,vis) :
            vis[i]=1
            for el in (adj[i]) :
                if vis[el]==0 :
                    dfs(el,vis)
        province = 0
        vis = [0] * len(isConnected) 
        for i in range(len(isConnected)) :
            if vis[i] == 0 :
                province +=1
                dfs(i,vis)
        return province
