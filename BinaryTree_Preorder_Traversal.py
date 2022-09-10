class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        stack=[root]
        r=[]
        while stack !=[] :
            root=stack.pop()
            r.append(root.val)
            if root.right is not None :
                stack.append(root.right)
            if root.left is not None :
                stack.append(root.left)
        return r
