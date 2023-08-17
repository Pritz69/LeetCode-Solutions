class Trip
{
    int x;
    int y;
    int d;
    Trip(int x,int y,int d)
    {
        this.x=x;
        this.y=y;
        this.d=d;
    }
}
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int n=mat.length;
        int m=mat[0].length;
        int ans[][]=new int[n][m];
        int vis[][]=new int[n][m];
        Queue<Trip> q=new LinkedList<Trip>();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(mat[i][j]==0)
                {
                    q.add(new Trip(i,j,0));
                    vis[i][j]=1;
                }
                else
                {
                    vis[i][j]=0;
                }
            }
        }
        int rows[]={-1,0,1,0};
        int cols[]={0,1,0,-1};
        while (!q.isEmpty())
        {
            int r=q.peek().x;
            int c=q.peek().y;
            int dis=q.peek().d;
            ans[r][c]=dis;
            q.remove();
            for(int i=0;i<4;i++)
            {
                int nr=r+rows[i];
                int nc=c+cols[i];
                while(nr<n && nr >=0 && nc<m && nc>=0 && vis[nr][nc]==0)
                {
                    vis[nr][nc]=1;
                    q.add(new Trip(nr,nc,dis+1));
                }
            }
        }
        return ans;
    }
}
