class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq=new LinkedList<Integer>();
        int n=nums.length;
        int ans[]=new int[n-k+1];
        int l=0;
        int r=0;
        int i=0;
        while (r<n)
        {
            while (!dq.isEmpty() && nums[r]>nums[dq.peekLast()])
            {
                dq.pollLast();
            } 
            if(!dq.isEmpty() && l>dq.peekFirst())
            {
                dq.pollFirst();
            }
            dq.offer(r);
            if(r+1-k >=0)
            {
                ans[i++]=nums[dq.peekFirst()];
                l +=1;
            }
            r +=1;
        }
        return ans;
    }
}
