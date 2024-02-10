        
        if not subRoot: return True
        if not root: return False

        if self.treeMatch(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def treeMatch(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.treeMatch(root.left, subRoot.left) and self.treeMatch(root.right, subRoot.right)
        else:
            return False
[3,4,5,1,2]
