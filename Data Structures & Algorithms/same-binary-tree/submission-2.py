# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFS(node):
    # we can do dfs and track the traversal to compare at the end
    if node is None:
        return [None]
    left = DFS(node.left)
    right = DFS(node.right)
    return [node.val] + left + right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pTraverse = DFS(p)
        qTraverse = DFS(q)
        print(pTraverse)
        print(qTraverse)
        return pTraverse == qTraverse
        