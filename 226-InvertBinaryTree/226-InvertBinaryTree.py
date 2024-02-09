#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
        if not root:
            
            return None
        
        return root
        #swap

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

[4,2,7,1,3,6,9]
