class Solution {
    public int maxScoreSightseeingPair(int[] A) {
        int left = A[0] + 0, res = Integer.MIN_VALUE;
        for (int j = 1; j < A.length; j++) {
            
            res = Math.max(res, left + A[j] - j);
            left = Math.max(left, A[j] + j);
        }
        return res;
    }
}