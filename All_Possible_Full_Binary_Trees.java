/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() { }
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    HashMap <Integer,List<TreeNode>> m= new HashMap<Integer,List<TreeNode>>();
    public List<TreeNode> allPossibleFBT(int n) {
        if (n%2==0)
        {
            return new ArrayList<TreeNode>();
        }
        if (n==1)
        {
            return Arrays.asList(new TreeNode(0));
        }
        if(m.containsKey(n))
        {
            return m.get(n);
        }
        List<TreeNode> res=new ArrayList<TreeNode>();
        for(int i=1;i<n;i+=2)
        {
            List<TreeNode> left= allPossibleFBT(i);
            List<TreeNode> right= allPossibleFBT(n-i-1);
            for (TreeNode l :left)
            {
                for(TreeNode r:right)
                {
                    TreeNode root=new TreeNode(0,l,r);
                    res.add(root);
                }
            }
        }
        m.put(n,res);
        return res;
    }
    /* FUNCTION FOR PRINTING THE TREE- LEVEL ORDER TRAVERSAL

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 7;
        List<TreeNode> result = solution.allPossibleFBT(n);

        System.out.println("All possible full binary trees with " + n + " nodes:");

        List<List<Integer>> resultList = new ArrayList<>();
        for (TreeNode root : result) {
            List<Integer> treeList = new ArrayList<>();
            printTree(root, treeList);
            if (treeList.size() == 0) {
                resultList.add(Collections.emptyList());
            } else {
                resultList.add(treeList);
            }
        }

        // Print the 2D list
        System.out.println(resultList);
    }

    // Utility function to perform level-order traversal and add nodes to the list
    private static void printTree(TreeNode root, List<Integer> treeList) {
        if (root == null) {
            treeList.add(null);
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null) {
                treeList.add(node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            } else {
                treeList.add(null);
            }
        }
    }

    */
}
