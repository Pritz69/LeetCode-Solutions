class Solution {
    public int uniquePathsIII(int[][] grid) {
        int z=0;
        int sx=0;
        int sy=0;
        for(int i=0;i<grid.length;i++)
        {
            for(int j=0;j<grid[0].length;j++)
            {
                if (grid[i][j]==0)
                {
                    z++;
                }
                else if(grid[i][j]==1)
                {
                    sx=i;
                    sy=j;
                }
            }
        }
        return dfs(grid,sx,sy,z);
    }
    private int dfs(int grid[][],int x,int y,int z)
    {
        if(x<0 || y<0 || x >= grid.length || y >= grid[0].length || grid[x][y]==-1)
        {
            return 0;
        }
        if (grid[x][y]==2)
        {
            return z==-1 ? 1 : 0;
        }
        grid[x][y]=-1;
        z--;
        int total=dfs(grid,x+1,y,z) + dfs(grid,x,y+1,z) + dfs(grid,x,y-1,z) + dfs(grid,x-1,y,z);
        grid[x][y]=0;
        return total;
    }
}
