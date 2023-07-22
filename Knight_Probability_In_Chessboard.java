class Solution {
    public boolean valid(int ni,int nj,int n)
    {
        if((ni<n && ni >=0) && (nj<n && nj>=0))
        {
            return true;
        }
        return false;
    }
    public double knightProbability(int n, int k, int row, int column) {
        double curr[][]=new double[n][n];
        double next[][]=new double[n][n];
        curr[row][column]=1;
        for(int mo=1;mo<=k;mo++)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if (curr[i][j] !=0)
                    {
                        int ni=0;
                        int nj=0;
                        ni=i-2;
                        nj=j+1;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i-1;
                        nj=j+2;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i+1;
                        nj=j+2;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i+2;
                        nj=j+1;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i+2;
                        nj=j-1;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i+1;
                        nj=j-2;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i-1;
                        nj=j-2;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                        ni=i-2;
                        nj=j-1;
                        if (valid(ni,nj,n))
                        {
                            next[ni][nj] += curr[i][j]/8.0;
                        }
                    }
                }
            }
            curr=next;
            next=new double[n][n];
        }
        double sum=0.0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                sum += curr[i][j];
            }
        }
        return sum;
    }
}
/* SHORT VERSION
class Solution {
    public boolean valid(int ni, int nj, int n) {
        return (ni < n && ni >= 0) && (nj < n && nj >= 0);
    }

    public double knightProbability(int n, int k, int row, int column) {
        double curr[][] = new double[n][n];
        double next[][] = new double[n][n];
        curr[row][column] = 1;

        int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
        int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};

        for (int mo = 1; mo <= k; mo++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (curr[i][j] != 0) {
                        for (int move = 0; move < 8; move++) {
                            int ni = i + dx[move];
                            int nj = j + dy[move];
                            if (valid(ni, nj, n)) {
                                next[ni][nj] += curr[i][j] / 8.0;
                            }
                        }
                    }
                }
            }
            curr = next;
            next = new double[n][n];
        }

        double sum = 0.0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum += curr[i][j];
            }
        }
        return sum;
    }
}
*/
