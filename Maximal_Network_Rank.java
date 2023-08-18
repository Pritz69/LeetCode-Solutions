class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        Map<Integer,ArrayList<Integer>> a=new HashMap<>();
        for(int i=0;i<roads.length;i++)
        {
            int u=roads[i][0];
            int v=roads[i][1];
            a.computeIfAbsent(u,key ->new ArrayList<>()).add(v);
            a.computeIfAbsent(v,key ->new ArrayList<>()).add(u);
        }
        /*for(int x:a.keySet())
        {
            System.out.println(x+" "+a.get(x));
        }*/
        int m=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                List<Integer> neighborsI = a.getOrDefault(i, new ArrayList<>());
                List<Integer> neighborsJ = a.getOrDefault(j, new ArrayList<>());
                int ans = neighborsI.size() + neighborsJ.size();
                int f1 = neighborsI.contains(j) ? 1 : 0;
                int f2 = neighborsJ.contains(i) ? 1 : 0;
                if (f1 == 1 && f2 == 1) 
                {
                    ans -= 1;
                }
                m = Math.max(m, ans);
            }
        }
        return m;
    }
}
/*class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int N = roads.length;
        int[][] isDirectEdge = new int[n][n];
        int[] num = new int[n];
        for(int i =0;i<N;i++){
            int src=roads[i][0];
            int dest = roads[i][1];

            num[src]++;
            num[dest]++;

            isDirectEdge[src][dest] = 1;
            isDirectEdge[dest][src] = 1;
        }
        int ans =0;
        for(int i =0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                ans = Math.max(ans,num[i] + num[j] - isDirectEdge[i][j]);
                // System.out.println(num[i] + num[j] - isDirectEdge[i][j]);
            }
        }
        return ans;
    }
}*/
