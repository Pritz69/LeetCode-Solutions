class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end=len(graph)-1
        def dfs(node,path,output):
            if node==end:
                output.append(path)
            for nx in graph[node]:
                dfs(nx,path+[nx],output)
        output=[]
        dfs(0,[0],output)
        return output
