class Solution {
    public void backtrack(int nums[],int index,Set<List<Integer>> res , List<Integer>seq)
    {
        if (index==nums.length)
        {
            if (seq.size()>=2)
            {
                res.add(new ArrayList<>(seq));
            }
            return ;
        }
        if(seq.isEmpty() || seq.get(seq.size()-1)<=nums[index])
        {
            seq.add(nums[index]);
            backtrack(nums,index+1,res,seq);
            seq.remove(seq.size()-1);
        }
        backtrack(nums,index+1,res,seq);
    }
    public List<List<Integer>> findSubsequences(int[] nums) {
        Set<List<Integer>> res = new HashSet<List<Integer>>();
        List<Integer> seq = new ArrayList<Integer>();
        backtrack(nums,0,res,seq);
        return new ArrayList(res);
    }
}
