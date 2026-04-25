# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFS(root, target):
    # do an in-order traversal, and increment a furthest from bottom counter.
    # check if this counter matches k
    if root is None:
        return 0, False
    depth = 1
    leftDepth, found = DFS(root.left, k)
    if found:
        return leftDepth, True
    depth += leftDepth
    if depth == k:
        return root.val, True
    rightDepth, found = DFS(root.right, k)
    if found:
        return rightDepth, True
    depth += rightDepth
    return depth, False
def levelOrder(root):
    if root is None:
        return [None]
    else:
        if root.left and root.right:
            left = levelOrder(root.left)
            right = levelOrder(root.right)
            return left + [root.val] + right
        if root.left: # no right
            left = levelOrder(root.left)
            return left + [root.val]
        if root.right: # no left
            right = levelOrder(root.right)
            return [root.val] + right
        else:
            return [root.val]
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if we're finding min we go left until we cant anymore 
        traversal = levelOrder(root)
        print(f"depth: {traversal}")
        return traversal[k -1]