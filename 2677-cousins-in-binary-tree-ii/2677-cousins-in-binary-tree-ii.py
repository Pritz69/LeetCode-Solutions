# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lsm=[]
        q=deque([root])
        while q :
            sm=0
            for i in range(len(q)) :
                node=q.popleft()
                sm +=node.val
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            lsm.append(sm)
        q=deque([(root,root.val)])
        level=0
        while q :
            for i in range(len(q)):
                node,val=q.popleft()
                node.val=lsm[level]-val
                csum=0
                if node.left :
                    csum += node.left.val
                if node.right :
                    csum += node.right.val
                if node.left :
                    q.append((node.left,csum))
                if node.right :
                    q.append((node.right,csum))
            level +=1
        return root