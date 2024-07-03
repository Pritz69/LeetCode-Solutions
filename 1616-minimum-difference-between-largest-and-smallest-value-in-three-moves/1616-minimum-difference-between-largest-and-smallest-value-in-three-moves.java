class Solution {
    public int minDifference(int[] nums) {
        if(nums.length <=3)
        {
            return 0;
        }
        Arrays.sort(nums);
        int n=nums.length;
        int d1=nums[n-4]-nums[0];
        int d2=nums[n-1]-nums[3];
        int d3=nums[n-3]-nums[1]; //2 big 1 small
        int d4=nums[n-2]-nums[2]; //1 big 2 small
        return Math.min(d1,Math.min(d2,Math.min(d3,d4)));
    }
}
