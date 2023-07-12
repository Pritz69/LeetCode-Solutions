class Solution {
    private boolean dfscheck(int node,int vis[],int pathvis[],int check[],int graph[][])
    {
        vis[node]=1;
        pathvis[node]=1;
        check[node]=0;
        for(int it:graph[node])
        {
            if (vis[it]==0)
            {
                if (dfscheck(it,vis,pathvis,check,graph)==true)
                {
                    return true;
                }
            }
            if(pathvis[it]==1)
            {
                return true;
            }
        }
        check[node]=1;
        pathvis[node]=0;
        return false;
    }
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int v=graph.length;
        int vis[]=new int[v];
        int pathvis[]=new int[v];
        int check[]=new int[v];
        for(int i=0;i<v;i++)
        {
            if(vis[i]==0)
            {
                dfscheck(i,vis,pathvis,check,graph);
            }
        }
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<v;i++)
        {
            if (check[i]==1)
            {
                ans.add(i);
            }
        }
        return ans;
    }
}
