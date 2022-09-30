class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root :
            return None
        if root.val == key :
            if not root.left and not root.right :
                return None
            if not root.left and root.right :
                return root.right 
            if not root.right and root.left :
                return root.left
            pnt=root.right 
            while pnt.left :
                pnt=pnt.left
            root.val =pnt.val
            root.right= self.deleteNode(root.right,root.val)
        elif root.val > key :
            root.left=self.deleteNode(root.left,key)
        elif root.val < key :
            root.right=self.deleteNode(root.right,key)
        return root
                
