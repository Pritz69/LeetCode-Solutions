class Solution {
    public int sumOfSquares(int[] nums) {
        int s=0;
        int n=nums.length;
        int i=1;
        for(int x:nums)
        {
            if(n%i==0)
            {
                s+=x*x;
            }
            i +=1;
        }
        return s;
    }
}
