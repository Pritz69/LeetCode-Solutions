class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int c=0,mx=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==0)
            {
                c=0;
            }
            else 
            {
                c++;
            }
            mx=Math.max(mx,c);
        }
        return mx;
    }
}
