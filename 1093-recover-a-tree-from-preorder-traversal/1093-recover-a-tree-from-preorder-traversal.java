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
    public TreeNode recoverFromPreorder(String traversal) {
        
        int i=0;
        int dashes = 0;
        Stack<TreeNode> st = new Stack<>();
        int n = traversal.length();
        int j=0;
        while(i<n)
        {
            char ch  = traversal.charAt(i);
            if(ch=='-'){
                i++;
                dashes++;
            }
            else
            {
                j=i;
                while(j<n && traversal.charAt(j)!='-'){
                    j++;
                }
                int value = Integer.parseInt(traversal.substring(i,j));
                TreeNode node = new TreeNode(value);
                while(st.size()> dashes){
                    st.pop();
                }
                if(!st.isEmpty() && st.peek().left == null){  
                    st.peek().left = node;  
                }
                else if(!st.isEmpty() && st.peek().right == null) {  
                    st.peek().right = node;  
                }  
                st.push(node);
                i=j;
                dashes=0;
            }
        }
       while (st.size() > 1) {  
            st.pop();  
        }  
        return st.peek();
    }
}