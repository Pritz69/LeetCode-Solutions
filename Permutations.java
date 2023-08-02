class Solution {
    public void backtrack(List<List<Integer>> ans,int []nums,int []freq,ArrayList<Integer>temp)
    {
        if(temp.size()==nums.length)
        {
            ans.add(new ArrayList<>(temp));
            return ;
        }
        for(int i=0;i<nums.length;i++)
        {
            if (freq[i]==0)
            {
                freq[i]=1;
                temp.add(nums[i]);
                backtrack(ans,nums,freq,temp);
                temp.remove(temp.size()-1);
                freq[i]=0;
            }
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        int n=nums.length;
        int []freq=new int[n];
        backtrack(ans,nums,freq,new ArrayList<Integer>());
        return ans;
    }
}
