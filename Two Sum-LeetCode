class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = nums.length;
        int a[] = new int[2];
        Map<Integer,Integer> map=new HashMap<Integer,Integer>();
        for(int i=0; i<l ; i++)
        {
            if(map.containsKey(target-nums[i]))
            {
                a[1]=i;
                a[0]=map.get(target-nums[i]);
                return a;
            }
            map.put(nums[i],i);
        }
        return a;
    }
}
