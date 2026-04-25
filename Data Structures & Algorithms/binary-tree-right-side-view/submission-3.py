# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# def levelOrder(root, level):
#     if root is None:
#         return [None]
#     # if root.left and root.right:
#     #     left = levelOrder(root.left, level + 1)
#     #     right = levelOrder(root.right, level + 1)
#     #     return left + (root.val, level) + right
#     returnList = []
#     if root.left: # no right
#         left = levelOrder(root.left, level + 1)
#         returnList = left
#     returnList += [(root.val, level)]
#     if root.right:
#         right = levelOrder(root.right, level + 1)
#         returnList += right
#     return returnList

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         # this is basically just the rightmost node at every depth level
#         # if I do a level order traversal I can index the -1 element
#         levelsDict = dict()
#         rList = levelOrder(root, 0)
#         print(rList)
#         maxLvl = 0
#         if None in rList:
#             return []
#         for val, level in rList:
#             maxLvl = max(level, maxLvl)
#         visible = [None] * (maxLvl + 1)
#         print(visible)
#         for val, level in rList:
#             visible[level] = val
#         return visible


class Solution:
    def __init__(self):
        self.levelList = []
    def levelOrder(self, root, level):
        if root is None:
            return [None]
        if len(self.levelList) == level: # this is the first time this was seen
            self.levelList.append(root.val)
        right = self.levelOrder(root.right, level + 1)
        left = self.levelOrder(root.left, level + 1)
        return [None]

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelOrder(root, 0)
        # print(self.levelList)
        return self.levelList

    
        