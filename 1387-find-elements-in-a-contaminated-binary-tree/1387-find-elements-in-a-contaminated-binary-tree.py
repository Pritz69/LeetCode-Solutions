# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val=0
        node=root
        def func(node) :
            if not node :
                return
            if node.left :
                node.left.val=2*node.val +1
                func(node.left)
            if node.right :
                node.right.val=2*node.val+2
                func(node.right)
        func(node)
        self.s=set()
        def inorder(node) :
            if not node :
                return 
            inorder(node.left)
            self.s.add(node.val)
            inorder(node.right)
        inorder(node)
    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)