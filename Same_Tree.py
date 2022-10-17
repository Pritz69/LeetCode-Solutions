class Solution:
	def preOrder(self, node):
		r = []
		if node is not None:
			r.append(node.val)
			r.append(self.preOrder(node.left))
			r.append(self.preOrder(node.right))
		return r

	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		return self.preOrder(p) == self.preOrder(q)
