class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer>d=new HashMap<>();
        for(int x:nums1)
        {
            d.put(x,d.getOrDefault(x,0)+1);
        }
        ArrayList<Integer>a=new ArrayList<Integer>();
        for(int x:nums2)
        {
            if(d.containsKey(x) && d.get(x) >0)
            {
                a.add(x);
                d.put(x,d.get(x)-1);
            }
        }
        int ans[]=new int[a.size()];
        int i=0;
        for(int x:a)
        {
            ans[i++]=x;
        }
        return ans;
    }
}