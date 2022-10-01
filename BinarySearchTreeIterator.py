class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root :
            self.stack.append(root)
            root=root.left

    def next(self) -> int:
        res=self.stack.pop()
        cur=res.right
        while cur :
            self.stack.append(cur)
            cur=cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack !=[]
