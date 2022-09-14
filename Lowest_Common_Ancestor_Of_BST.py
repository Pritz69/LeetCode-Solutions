class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur =root 
        while cur :
            if cur.val<p.val and cur.val < q.val :
                cur=cur.right
            elif cur.val > p.val and cur.val > q.val :
                cur=cur.left
            else :
                return cur
