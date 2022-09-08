class Solution {
    public List<Integer> inHelper(TreeNode root,List<Integer>list)
    {
        if(root==null)
        {
            return list ;
        }
        inHelper(root.left,list);
        list.add(root.val);
        inHelper(root.right,list);
        return list;
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer>list=new ArrayList<>();
        return inHelper(root,list);
        }
}
