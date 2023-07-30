class Solution {
    public int countCompleteSubarrays(int[] nums) {
        HashMap<Integer,Integer> m=new HashMap<>();
        for(int x:nums)
        {
            m.put(x,m.getOrDefault(x,0)+1);
        }
        int ans=0;
        HashMap<Integer,Integer> s=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            s.clear();
            for (int j=i;j<nums.length;j++)
            {
                s.put(nums[j],s.getOrDefault(nums[j],0)+1);
                if(s.size()>=m.size())
                {
                    ans +=1;
                }
            }
        }
        return ans;
    }
}
