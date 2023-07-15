class Solution {
    public int maxEvents(int[][] a) {
        int ma= Integer.MIN_VALUE;
        for (int i=0;i<a.length;i++)
        {
            ma=Math.max(ma,a[i][1]);
        }
        TreeSet<Integer> set=new TreeSet<>();
        for(int i=1;i<=ma;i++)
        {
            set.add(i);
        }
        int ans=0;
        Arrays.sort(a, (event1, event2) -> {
        if (event1[1] != event2[1]) 
        {
            return Integer.compare(event1[1], event2[1]); 
        } 
        else 
        {
            return Integer.compare(event1[0], event2[0]); 
        }
        });
        //Arrays.sort(a, (event1, event2) -> {
        //if (event1[1] != event2[1]) {
        //    return event1[1] - event2[1]; // Sort by end dates in ascending order
        //} else {
        //   return event1[0] - event2[0]; // If end dates are equal, sort by start dates    in ascending order
        //}
        //});
        for(int i=0;i<a.length;i++)
        {
            Integer available=set.ceiling(a[i][0]);
            if(available==null || available>a[i][1])
            {
                continue;
            }
            else
            {
                ans++;
                set.remove(available);
            }
        }
        return ans; 
    }
}
