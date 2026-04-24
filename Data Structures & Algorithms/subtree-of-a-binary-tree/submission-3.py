# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkEquals(root1, root2):
    if root1 is None or root2 is None:
        if root1 is None and root2 is None:
            return True
        else:
            return False
    if root1.val != root2.val:
        return False
    else:
        return (checkEquals(root1.left, root2.left) and checkEquals(root1.right, root2.right))
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if a node is the same as the root
        if root is None:
            return False
        if root.val == subRoot.val:
            if (checkEquals(root, subRoot)):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        