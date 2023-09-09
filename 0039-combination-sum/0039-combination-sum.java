class Solution {
    public void rec(int arr[],int t,int i,List<List<Integer>>ans ,List<Integer>r)
    {
        if (i == arr.length)
        {
            if (t==0)
            {
                ans.add(new ArrayList<>(r));
            }
            return ;
        }
        if (arr[i] <= t)
        {
            r.add(arr[i]);
            rec(arr,t-arr[i],i,ans,r);
            r.remove(r.size()-1);
        }
        rec(arr,t,i+1,ans,r);
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans=new ArrayList<>();
        rec(candidates,target,0,ans,new ArrayList<>());
        return ans;
    }
}