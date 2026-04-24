# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def search(node, t1, t2):
    if node is None:
        return None
    if t1 > node.val and t2 > node.val: # not done looking
        return search(node.right, t1, t2)
    elif t1 < node.val and t2 < node.val: # not done looking
        return search(node.left, t1, t2)
    else:
        return node
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return search(root, p.val, q.val)