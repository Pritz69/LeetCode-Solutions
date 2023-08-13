class Solution {
    public int maxSum(int[] nums) {
        HashMap<Integer,ArrayList<Integer>> h = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int num=nums[i];
            int mx=0;
            while (num>0)
            {
                int d=num%10;
                mx=Math.max(mx,d);
                num=num/10;
            }
            if(h.containsKey(mx))
            {
                ArrayList<Integer> a=h.get(mx);
                a.add(nums[i]);
                h.put(mx,a);
            }
            else
            {
                ArrayList<Integer> a=new ArrayList<>();
                a.add(nums[i]);
                h.put(mx,a);
            }
        }
        int ans=-1;
        for(int x:h.keySet())
        {
            ArrayList<Integer> al=h.get(x);
            Collections.sort(al);
            if (al.size() >=2)
            {
                ans=Math.max(ans,al.get(al.size()-1)+al.get(al.size()-2));
            }
        }
        System.out.println(h);
        return ans;
    }
}
