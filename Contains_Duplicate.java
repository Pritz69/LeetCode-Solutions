class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int c=0,i=0;
        for(i=0;i<(nums.length)-1;i++)
        {
            if(nums[i]==nums[i+1])
            {
                c++;
            }
        }
        if(c>0)
            return true; 
        else
            return false;
    }
}
