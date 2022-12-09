class Solution {
public:
    int maxAncestorDiff(TreeNode* r, int mn = 100000, int mx = 0) {
  return r == nullptr ? mx - mn :
    max(maxAncestorDiff(r->left, min(mn, r->val), max(mx, r->val)),
      maxAncestorDiff(r->right, min(mn, r->val), max(mx, r->val)));
}
};
