class Solution {
    public long maxArrayValue(int[] nums) {
        long last= nums[nums.length-1];
        for(int i=nums.length-2;i>=0;i--)
        {
            if (nums[i]>last)
            {
                last=nums[i];
            }
            else
            {
                last += nums[i];
            }
        }
        return last;
    }
}
/*    STACK SOLUTION----

        Stack<Long> s=new Stack<>();
        s.push((long)nums[nums.length-1]);
        for(int i=nums.length-2;i>=0;i--)
        {
            if (nums[i]>s.peek())
            {
                s.push((long)nums[i]);
            }
            else
            {
                long v=s.pop();
                s.push((long)(v+nums[i]));
            }
        }
        return s.pop();
*/ 
