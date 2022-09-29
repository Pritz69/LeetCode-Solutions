class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r) :
            if l > r :
                return None
            m=(l+r)//2
            root= TreeNode(nums[m])
            root.left=helper(l,m-1)
            root.right=helper(m+1,r)
            return root
        return helper(0,len(nums)-1)
