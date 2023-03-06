class Solution {
    public int findKthPositive(int[] arr, int k) {
        int i=1,j=0,ans=0;
        while(k>0)
        {
            if(j>=arr.length)
            {
                ans=i;
                i++;
                k--;
            }
            else
            if(arr[j]==i)
            {
                j++;
                i++;
            }
            else
            {
                ans=i;
                k--;
                i++;
            }
        }
        return ans;
    }
}
