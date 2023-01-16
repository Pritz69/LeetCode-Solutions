class Solution {
   public int[][] rangeAddQueries(int n, int[][] queries) {
   int[][] ans = new int[n][n];
   for (int[] q : queries) {
       int row1 = q[0], col1 = q[1], row2 = q[2], col2 = q[3];
       for (int i = row1; i <= row2; i++) 
       {
           ans[i][col1] +=1; //MARK THE BEGINNING OF QUERY WITH +1
           if ((col2 +1) < n ) //CHECK IF THE POSITION LIES WITHIN THAT COL IN THE ARRAY
           {
               ans[i][col2 +1] -=1; //IF THE POS EXISTS, MARK IT WITH -1 ... DRY RUN IT FOR BETTER UNDERSTANDING.
           }
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<n;j++)
        {
            ans[i][j] += ans[i][j-1]; //FINALLY TRAVERSE THE ARRAY AND ADD THE CONTENT OF EACH ROW IN IT.
        }
    }
   return ans;
   }
}
