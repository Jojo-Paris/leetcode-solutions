#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if p.val == q.val keep checking each child node
        # if p and q both equal None (means reached the leaf while they always equal) Base
        # if not p or not q is not equal, so return false

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
            
[1,2,3]
