class Solution:
    def __init__(self):
        self.levelList = []
    def levelOrder(self, root, level):
        if root is None:
            return
        if len(self.levelList) == level: # this is the first time this was seen
            self.levelList.append(root.val)
        right = self.levelOrder(root.right, level + 1)
        left = self.levelOrder(root.left, level + 1)
        return

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelOrder(root, 0)
        # print(self.levelList)
        return self.levelList

    
        