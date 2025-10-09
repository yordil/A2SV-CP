# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, current_sum):
        
            if not node.left and not node.right:
                return current_sum == targetSum

        
            left_has = dfs(node.left, current_sum + node.left.val) if node.left else False
            right_has = dfs(node.right, current_sum + node.right.val) if node.right else False

            return left_has or right_has

        return dfs(root, root.val)

        
