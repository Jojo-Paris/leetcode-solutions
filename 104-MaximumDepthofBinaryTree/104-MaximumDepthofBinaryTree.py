# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #DFS
        def maximumHeight(root, curMax):
            if not root:
                return curMax
            
            curMax += 1

            return max(maximumHeight(root.left, curMax), maximumHeight(root.right, curMax))

        return maximumHeight(root, 0)

[3,9,20,null,null,15,7]
