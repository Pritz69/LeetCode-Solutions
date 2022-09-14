class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        int c=0;
        vector<int>n(10,0);
        pseudo_count(root,n,c);
        return c;
    }
    void pseudo_count(TreeNode* root,vector<int>& n ,int& c )
    {
        if(root==NULL)
        {
            return ;
        }
        n[root->val]++ ;
        pseudo_count(root->left,n,c);
        pseudo_count(root->right,n,c);
        if(root->left==NULL && root->right == NULL)
        {
            int f=0;
            for(int i=0;i<=9;i++)
            {
                if(n[i]%2!=0)
                {
                    f++;
                }
            }
            if(f==1 || f==0)
                {
                    c++;
                }
        }
        n[root->val]--;
    }
};
