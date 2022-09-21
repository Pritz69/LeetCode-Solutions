class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int evenS =0;
        int n = nums.length ;
        for (int x:nums)
        {
            if (x%2==0)
            {
                evenS +=x;
            }
        }
        int ans[]=new int[n] ;
        for (int i=0;i<n;i++)
        {
            int newv=queries[i][0];
            int indx=queries[i][1];
            int oldv=nums[indx];
            if(oldv %2 ==0)
            {
                evenS -=oldv;
            }
            nums[indx] +=newv;
            if(nums[indx]%2==0)
            {
                evenS +=nums[indx];
            }
            ans[i]=evenS;
        }
        return ans;
    }
}
