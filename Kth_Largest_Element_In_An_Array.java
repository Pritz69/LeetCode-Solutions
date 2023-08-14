class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq= new PriorityQueue<Integer>();
        int n=nums.length;
        for (int x : nums)
        {
            pq.add(x);
        }
        int i=1;
        while(i<=n-k)
        {
            pq.poll();
            i +=1;
        }
        return pq.peek();
    }
}
