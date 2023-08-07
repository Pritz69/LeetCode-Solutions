class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        int t=0;
        int b=rows-1;
        int targetrow=0;
        while (t<=b)
        {
            int r=(t+b)/2;
            if (target < matrix[r][0])
            {
                b=r-1;
            }
            else if(target > matrix[r][cols-1])
            {
                t=r+1;
            }
            else
            {
                targetrow=r;
                break;
            }
        }
        int le=0;
        int ri=cols-1;
        while(le<=ri)
        {
            int m=(le+ri)/2;
            if (target > matrix[targetrow][m])
            {
                le=m+1;
            }
            else if(target < matrix[targetrow][m])
            {
                ri=m-1;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
}
