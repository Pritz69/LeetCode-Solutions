class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output=[]
        def dfs(node,path,sm) :
            sm += node.val 
            tmp =path + [node.val]
            if node.left :
                dfs(node.left,tmp,sm)
            if node.right :
                dfs(node.right,tmp,sm)
            if not node.left and not node.right and sm==targetSum :
                self.output.append(tmp)
        if not root :
            return []
        dfs(root,[],0)
        return self.output
