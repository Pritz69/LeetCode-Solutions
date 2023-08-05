/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> build(int left,int right,HashMap<Pair<Integer,Integer>,List<TreeNode>> dp)
    {
        List<TreeNode> ans=new ArrayList<>();
        if (left > right)
        {
            ans.add(null);
            return ans;
        }
        if (dp.containsKey(new Pair<>(left,right)))
        {
            return dp.get(new Pair<>(left,right));
        }
        for(int root=left;root<=right;root++)
        {
            List<TreeNode> leftsubtree=build(left,root-1,dp);
            List<TreeNode> rightsubtree=build(root+1,right,dp);
            for(TreeNode lefttree : leftsubtree )
            {
                for(TreeNode righttree : rightsubtree)
                {
                    TreeNode roottree= new TreeNode(root,lefttree,righttree);
                    ans.add(roottree);
                }
            }
        }
        dp.put(new Pair<>(left,right),ans);
        return ans ;                        // return dp.get(new Pair<>(left,right)) ;
    }
    public List<TreeNode> generateTrees(int n) {
        HashMap<Pair<Integer,Integer>,List<TreeNode>> dp=new HashMap<>();
        return build(1,n,dp);
    }
}
