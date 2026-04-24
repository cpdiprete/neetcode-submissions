# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFShelper(node):
    if node is None:
        return 0, True
    left, ltruth = DFShelper(node.left)
    right, rtruth = DFShelper(node.right)
    if not (ltruth and rtruth):
        return (-1, False)
    if abs(left - right) > 1:
        return -1, False
    else:
        return 1 + max(left, right), True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # idea is to do DFS, and compare right vs left tree depth 
        return DFShelper(root)[1]
        