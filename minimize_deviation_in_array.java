//not solved
class Solution {
    public int minimumDeviation(int[] nums) {
        int minDev = Integer.MAX_VALUE;
        int minVal = Integer.MAX_VALUE;
        PriorityQueue<Integer> maxQue = new PriorityQueue<>((a,b)->b - a);

        for(int n : nums) {
            if(n % 2 == 1) n = n * 2;           
            maxQue.add(n);
            minVal = Math.min(minVal, n);
        }

        while(!maxQue.isEmpty()) {
            int maxVal = maxQue.poll();
            minDev = Math.min(minDev, maxVal - minVal);
            if(maxVal % 2 == 1) break;
            maxVal /= 2;
            maxQue.add(maxVal);
            minVal = Math.min(minVal, maxVal);
        }

        return minDev;
    }
}
