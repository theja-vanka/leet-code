# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        pre_ind = 0
        index_map = {v:i for i,v in enumerate(inorder)}
        
        def helper(left, right):
            nonlocal pre_ind
            if left > right:
                return None

            rootval = preorder[pre_ind]
            pre_ind += 1

            root = TreeNode(rootval)
            mid = index_map[rootval]

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
        
            return root

        return helper(0, len(inorder)-1)