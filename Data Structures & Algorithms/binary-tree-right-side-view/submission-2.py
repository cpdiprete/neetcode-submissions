# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(root, level):
    if root is None:
        return [None]
    # if root.left and root.right:
    #     left = levelOrder(root.left, level + 1)
    #     right = levelOrder(root.right, level + 1)
    #     return left + (root.val, level) + right
    returnList = []
    if root.left: # no right
        left = levelOrder(root.left, level + 1)
        returnList = left
    returnList += [(root.val, level)]
    if root.right:
        right = levelOrder(root.right, level + 1)
        returnList += right
    return returnList

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # this is basically just the rightmost node at every depth level
        # if I do a level order traversal I can index the -1 element
        levelsDict = dict()
        rList = levelOrder(root, 0)
        print(rList)
        maxLvl = 0
        if None in rList:
            return []
        for val, level in rList:
            maxLvl = max(level, maxLvl)
        visible = [None] * (maxLvl + 1)
        print(visible)
        for val, level in rList:
            visible[level] = val
        return visible
        for val, level in rList:
            if level in levelsDict:
                levelsDict[level].append(val)
            else:
                levelsDict[level] = [val]
        visibleList = []
        for level, nodeList in levelsDict.items():
            visibleList.append(nodeList[-1])
        # sort nodeList based on which level comes first
        print(visibleList)
        return visibleList

        