/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (!root) return {};

        vector<vector<int>> ans;
        levelOrder(root, 0, ans);
        return ans;
    }
    
    void levelOrder(Node* node, int level, vector<vector<int>>& ans) {
        if (level == size(ans)) {
            ans.push_back({node->val});
        } else {
            ans[level].push_back(node->val);
        }
        for (Node* child : node->children) {
            levelOrder(child, level + 1, ans);
        }
    }
};
