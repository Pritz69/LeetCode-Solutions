class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta=[(n^k)-n for n in nums] 
        delta.sort(reverse=True)
        res=sum(nums)
        for i in range(0,len(delta),2) :
            if i==len(delta)-1 :
                break
            currpath=delta[i]+delta[i+1]
            if currpath <=0 :
                break
            res +=currpath
        return res


/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function(nums, k, edges) {
    let delta=nums.map(n=> (n^k)-n);
    delta.sort((a,b)=> b-a);
    let sum=nums.reduce((acc,n)=>acc+n,0);
    for(let i=0;i<delta.length;i+=2)
    {
        if (i==delta.length-1)
        {
            break;
        }
        currpath=delta[i]+delta[i+1];
        if (currpath <=0)
        {
            break;
        }
        sum += currpath;
    }
    return sum;
};
