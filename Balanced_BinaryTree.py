class Solution(object):
    def isBalanced(self, root):
        r = [1]
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            if abs(left - right) > 1:
                r[0] = 0
            return 1 + max(left,right)
        
        maxDepth(root)
        return True if r[0] == 1 else False
