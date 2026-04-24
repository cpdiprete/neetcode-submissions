# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node, maxSeen):
    if node is None:
        return 0
    if node.val < maxSeen:
        left = dfs(node.left, maxSeen)
        right = dfs(node.right, maxSeen)
        return left + right
    else:
        # need to add 1 in the return
        # need to update maxSeen
        maxSeen = node.val
        left = dfs(node.left, maxSeen)
        right = dfs(node.right, maxSeen)
        return 1 + left + right

    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node is good if it's the max node up to this point in the rcurrent path
        # I can pass the max seen so far on the DFS, and 
        goodCount = 0
        return dfs(root, root.val - 1)
        