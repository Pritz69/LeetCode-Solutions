# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans=0
        def dfs(node) :
            nonlocal ans 
            if not node :
                return []
            if not node.left and not node.right :
                return [1]
            left=dfs(node.left)
            right=dfs(node.right)
            for x in left :
                for y in right :
                    if (x+y) <= distance :
                        ans +=1
            total=left+right
            total=[d+1 for d in total]
            return total
        dfs(root)
        return ans