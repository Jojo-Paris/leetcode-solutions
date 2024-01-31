# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def sumOfLeft(root, isLeft):
            if root is None: return 0

            if root.left is None and root.right is None and isLeft:
                return root.val

            return sumOfLeft(root.left, True) + sumOfLeft(root.right, False)
        
        return sumOfLeft(root, False)
        
[3,9,20,null,null,15,7]
