class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int c=0;
        for(int x:hours)
        {
            if (x>=target)
            {
                c+=1;
            }
        }
        return c;
    }
}
