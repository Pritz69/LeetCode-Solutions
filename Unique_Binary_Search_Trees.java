class Solution {
    public int numTrees(int n) {
        int dp[]=new int[n+1];
        Arrays.fill(dp,1);
        for (int nodes=2;nodes<=n;nodes++)
        {
            int total=0;
            for(int root=1;root<=nodes;root++)   // Calculating the unique bsts with the tnode, considering each node upto tnode as root.
            {
                int left=root-1;               
                int right=nodes-root;
                total += dp[left]*dp[right];
            }
            dp[nodes]=total;
        }
        return dp[n];
    }
}
