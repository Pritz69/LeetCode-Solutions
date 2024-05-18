/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var distributeCoins = function(root) {
    let ans=0;
    const func=(node)=>{
        if(node==null)
        {
            return 0;
        }
        let l=func(node.left);
        let r=func(node.right);
        ans += Math.abs(l) + Math.abs(r);
        return node.val + l + r -1;
    }
    func(root);
    return ans
};
