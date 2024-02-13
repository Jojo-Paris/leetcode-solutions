

    def isSame(self, root, subRoot):

        if not root: return False

        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if root and subroot:
        if not subRoot: return True 
            return True
        if root and subroot and root.val == subRoot.val:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
class Solution:
#         self.right = right
#         self.left = left
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
[3,4,5,1,2]
