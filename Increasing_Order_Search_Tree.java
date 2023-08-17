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
    public void inorder(TreeNode curr,ArrayList<Integer>ans)
    {
        if(curr==null)
        {
            return;
        }
        inorder(curr.left,ans);
        ans.add(curr.val);
        inorder(curr.right,ans);
    }
    public TreeNode increasingBST(TreeNode root) {
        ArrayList<Integer> ans=new ArrayList<>();
        inorder(root,ans);
        TreeNode a=new TreeNode(0);
        TreeNode s=a;
        for(int x:ans)
        {
            TreeNode ne=new TreeNode(x);
            a.right=ne;
            a=ne;
        }
        return s.right;
    }
}
