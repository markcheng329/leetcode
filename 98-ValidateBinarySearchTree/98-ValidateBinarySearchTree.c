// Last updated: 11/12/2025, 4:59:07 AM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool checkhelper(struct TreeNode* root, long minimum, long maximum)
{
    if(root==NULL) return true;
    if(root->val<=minimum || root->val>=maximum) return false;
    return checkhelper(root->left, minimum,root->val) && checkhelper(root->right,root->val,maximum);
}
bool isValidBST(struct TreeNode* root)
{
    if(root==NULL) return true;
    return checkhelper(root,LONG_MIN,LONG_MAX);
}