#�Definition�for�a�binary�tree�node.
#�class�TreeNode:
#�����def�__init__(self,�val=0,�left=None,�right=None):
#���������self.val�=�val
#���������self.left�=�left
#���������self.right�=�right
class�Solution:
����def�invertTree(self,�root:�Optional[TreeNode])�->�Optional[TreeNode]:
��������if�not�root:�return�None
��������self.invertTree(root.left)

��������root.left,�root.right�=�root.right,�root.left

��������self.invertTree(root.right)

��������return�root
[4,2,7,1,3,6,9]
