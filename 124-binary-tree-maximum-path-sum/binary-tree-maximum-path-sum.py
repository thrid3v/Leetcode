# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0 
            
            rootLeft = dfs(root.left)
            rootRight = dfs(root.right)
            rootLeft = max(rootLeft, 0)
            rootRight = max(rootRight, 0)

            res[0] = max(res[0], root.val + rootLeft + rootRight)

            return root.val + max(rootLeft, rootRight)
        
        dfs(root)
        return res[0]
        