class Solution 
{
    public TreeNode insertIntoBST(TreeNode root, int val) 
    {
        if(root==null)
        {
            return new TreeNode(val);
        }
        
        // Movement in the BST 
        if(root.val<val)
        {
            root.right = insertIntoBST(root.right,val);
        }
        else 
        {
            root.left = insertIntoBST(root.left,val);
        }
        
        return root;
    }
}
