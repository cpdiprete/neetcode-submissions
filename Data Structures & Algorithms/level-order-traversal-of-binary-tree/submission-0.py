# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def BFS(node, level):
    if node is None:
        return [None]
    left = BFS(node.left, level + 1)
    right = BFS(node.right, level + 1)
    return [(node.val, level)] + left + right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # maintain a list of nodes, track the current level  
        traversal = BFS(root, 0)
        levelsDict = dict()
        for i in range(len(traversal)):
            if traversal[i] is None:
                continue
            else: # we have a node with it's current level
                level = traversal[i][1]
                val = traversal[i][0]
                if level not in levelsDict:
                    levelsDict[level] = [val]
                else:
                    levelsDict[level].append(val)
        return(list(levelsDict.values()))


        # print(traversal)
        #this is just a BFS right?