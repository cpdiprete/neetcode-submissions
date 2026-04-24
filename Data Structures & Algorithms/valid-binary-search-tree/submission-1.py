# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# if I'm going 
# def checkRight(node, parent, mini, maxi):
#     # this node should be greater than both mini and maxi
#     if node is None:
#         return True
#     if node.val <= maxi or node.val <= mini:
#         return False
#     if node.val <= parent:
#         return False 
#     maxi = max(maxi, node.val)
#     mini = min(mini, node.val)

#     left = checkLeft(node.left, node.val, mini, maxi)
#     right = checkRight(node.right, node.val, mini, maxi)
#     return left and right
# def checkLeft(node, parent, mini, maxi):
#     # this will confirm that the node is less than mini
#     # this will confirm that the node is more than maxi
#     if node is None:
#         return True
#     if node.val >= mini or node.val >= maxi:
#         return False
#     mini = min(mini, node.val)
#     maxi = max(maxi, node.val)
#     left = checkLeft(node.left, node.val, maxi)
#     right = checkRight(node.right, node.val, maxi)
#     return left and right
def DFS(root, mini, maxi):
    if root is None:
        return True
    # if mini is None:
    #     mini = root.val
    # elif maxi is None:
    #     mini = root.val
    if not(root.val > mini and root.val < maxi):
        print(root.val)
        print(mini)
        print(maxi)
        return False
    
    left = DFS(root.left, mini, root.val)
    right = DFS(root.right, root.val, maxi)
    return left and right
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at any given node, i'll need to make sure its' not 
            #1) Larger than the max we've seen
            #2) Not smaller than the min we've seen in this traversal
            if root is None:
                return True
            return DFS(root, -1001, 1001)
        