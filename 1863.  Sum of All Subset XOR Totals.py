/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums) {
    let ans=0;
    let n=nums.length;
    let rec=(i,x)=>{
        if (i==n) 
        {
            ans +=x;
            return ;
        }
        rec(i+1,x^nums[i])
        rec(i+1,x)
    }
    rec(0,0);
    return ans;
};
