# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfsHelper(node): # will return the number of nodes traversed, need the number of edges
    if node is None:
        return 0, 0
    left, leftDiam = dfsHelper(node.left)
    right, rightDiam = dfsHelper(node.right)

    curDiam = left + right # compare this with the largest one we've seen
    curDiam = max(curDiam, leftDiam, rightDiam) # keep the largest one
    return (max(left, right) + 1, curDiam)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return dfsHelper(root)[1]
        