class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = profit.length;
        int[][] jobs = new int[n][3];

        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }

        Arrays.sort(jobs, (a, b) -> Integer.compare(a[0], b[0]));

        Map<Integer, Integer> memo = new HashMap<>();
        return rec(0, jobs, memo);
    }

    private int rec(int i, int[][] jobs, Map<Integer, Integer> memo) {
        if (i == jobs.length) {
            return 0;
        }

        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        int takeCurrent = jobs[i][2];
        int nextIndex = findNextJobIndex(i, jobs);

        if (nextIndex != -1) {
            takeCurrent += rec(nextIndex, jobs, memo);
        }

        int notTakeCurrent = rec(i + 1, jobs, memo);

        int result = Math.max(takeCurrent, notTakeCurrent);
        memo.put(i, result);

        return result;
    }

    private int findNextJobIndex(int current, int[][] jobs) {
        for (int j = current + 1; j < jobs.length; j++) {
            if (jobs[j][0] >= jobs[current][1]) {
                return j;
            }
        }
        return -1;
    }
}
