class Solution {
    public boolean memoize(int[] nums, int[] dp, int ind, int n) {
        if (ind == n) {
            return true;
        }
        if (dp[ind] != -1) {
            return dp[ind]==1 ;
        }
        boolean res=false;
        if ((ind + 1 < n) && (nums[ind] == nums[ind + 1])) {
            res = memoize(nums, dp, ind + 2, n);
        }
        if (ind + 2 < n) {
            if (((nums[ind] == nums[ind + 1]) && (nums[ind + 1] == nums[ind + 2])) ||
                ((nums[ind] + 1 == nums[ind + 1]) && (nums[ind + 1]  == nums[ind + 2] - 1))) {
                res = res || memoize(nums, dp, ind + 3, n);
            }
        }
        if (res)
        {
            dp[ind] = 1;
        }
        else 
        {
            dp[ind] = 0;
        }
        return res;
    }

    public boolean validPartition(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        boolean ans = memoize(nums, dp, 0, n);
        return ans ;
    }
}


---PYTHON CODE---
  class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp={}
        n=len(nums)
        def dfs(ind) :
            if ind==n:
                return True
            if ind in dp :
                return dp[ind]
            res=False
            if ind+1 < n and nums[ind]==nums[ind+1]:
                res = dfs(ind+2)
            if ind+2 < n :
                if (nums[ind]==nums[ind+1]==nums[ind+2]) or (nums[ind]+1==nums[ind+1]==nums[ind+2]-1) :
                    res = res or dfs(ind+3)
            dp[ind]=res
            return res
        return dfs(0) 
