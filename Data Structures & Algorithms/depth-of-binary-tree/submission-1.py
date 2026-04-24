# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFS_helper(node):
    if node is None:
        return 0 # shouldn't give depth credit for a non-node
    left = 1 + DFS_helper(node.left)
    right = 1 + DFS_helper(node.right)
    return max(left, right)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxSeen = 0
        return DFS_helper(root)
        

        
        