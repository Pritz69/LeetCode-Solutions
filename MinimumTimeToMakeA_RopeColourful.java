class Solution {
    public int minCost(String colors, int[] neededTime) {
        int p=0;
        int a=0;
        char arr[]=colors.toCharArray();
        for(int i=1;i<arr.length;i++)
        {
            if(arr[p]!=arr[i])
            {
                p=i;
            }
            else
            {
                if(neededTime[p]<neededTime[i])
                {
                    a +=neededTime[p];
                    p=i;
                }
                else
                {
                    a +=neededTime[i];
                }
            }
        }
        return a;
    }
}
