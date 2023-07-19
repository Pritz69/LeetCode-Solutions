class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a, b) ->Integer.compare(a[0],b[0]));
        int prev_end= intervals[0][1];
        int res=0;
        for(int i=1;i<intervals.length;i++)
        {
            int st=intervals[i][0];
            int ed=intervals[i][1];
            if (st >= prev_end)
            {
                prev_end = ed;
            }
            else
            {
                res +=1;
                prev_end = Math.min(prev_end,ed);
            }
        }
        return res;
    }
}
