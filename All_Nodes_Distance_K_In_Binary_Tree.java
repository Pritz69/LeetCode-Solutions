/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private void make_parents(TreeNode root,TreeNode target,Map<TreeNode,TreeNode> parent_track)
    {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while (!queue.isEmpty())
        {
            TreeNode curr = queue.poll();
            if (curr.left != null)
            {
                parent_track.put(curr.left,curr);
                queue.offer(curr.left);
            }
            if (curr.right != null)
            {
                parent_track.put(curr.right,curr);
                queue.offer(curr.right);
            }
        }
    }
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode,TreeNode> parent_track = new HashMap<>();
        Map<TreeNode,Boolean> visited = new HashMap<>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        make_parents(root,root,parent_track);
        queue.offer(target);
        visited.put(target,true);
        int clevel=0;
        while (!queue.isEmpty())
        {
            int size=queue.size();
            if (clevel==k)
            {
                break;
            }
            clevel++ ;
            for (int i=0;i<size;i++)
            {
                TreeNode cur=queue.poll();
                if (cur.left != null && visited.get(cur.left)== null )
                {
                    queue.offer(cur.left);
                    visited.put(cur.left,true);
                }
                if (cur.right != null && visited.get(cur.right)== null )
                {
                    queue.offer(cur.right);
                    visited.put(cur.right,true);
                }
                if (parent_track.get(cur)!=null && visited.get(parent_track.get(cur))==null)
                {
                    queue.offer(parent_track.get(cur));
                    visited.put(parent_track.get(cur),true);
                }
            }
        }
        List<Integer> ans = new ArrayList<>();
        while (!queue.isEmpty())
        {
            TreeNode cur=queue.poll();
            ans.add(cur.val);
        }
        return ans;
    }
}
