class Solution {
    public boolean isGood(int[] nums) {
        int m=0;
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            if (nums[i]>m)
            {
                m=nums[i];
            }
            h.put(nums[i],h.getOrDefault(nums[i],0)+1);
        }
        if (nums.length != (m+1))
        {
            return false;
        }
        for(int x:h.keySet())
        {
            if (h.get(x)>1 && x !=m)
            {
                return false;
            }
        }
        return true;
    }
}
