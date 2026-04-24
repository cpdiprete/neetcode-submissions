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
    elif t1 == t2 == node.val:
        return node
    elif t1 == node.val:
        # t2's ancestor must be t1
        return node 
    elif t2 == node.val:
        return node 
    else:
        return node # they diverged
        # found
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return search(root, p.val, q.val)