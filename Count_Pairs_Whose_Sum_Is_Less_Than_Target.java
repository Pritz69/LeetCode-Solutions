class Solution {
    public int countPairs(List<Integer> nums, int target) {
        Collections.sort(nums);
        int c=0;
        int l=0;
        int r=nums.size()-1;
        while(l<r)
        {
            if(nums.get(l)+nums.get(r) <target)
            {
                c += r-l;
                l +=1;
            }
            else
            {
                r-=1;
            }
        }
        return c;
    }
}
/*
class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int c=0;
        for(int i=0;i<nums.size();i++)         
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums.get(i)+nums.get(j) < target)
                {
                    c +=1;
                }
            }
        }
        return c;
    }
}
*/
