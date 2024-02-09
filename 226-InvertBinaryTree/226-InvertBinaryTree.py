# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #recurisvely call on both left and right
        self.invertTree(root.left) 
        self.invertTree(root.right)
[4,2,7,1,3,6,9]
