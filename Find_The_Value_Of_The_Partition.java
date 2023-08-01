class Solution {
    public int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);
        int min=Integer.MAX_VALUE;
        for(int i=nums.length-1;i>=1;i--)
        {
            min=Math.min(min,nums[i]-nums[i-1]);
        }
        return min;
    }
}
