class Solution:
    def __init__(self):
        self.seen = set()
        
    def recurse(self, i, j):
        if (i < 0) or (i >= self.xmax):
            return
        if (j < 0) or (j >= self.ymax):
            return
        if self.grid[i][j] == "0":
            return
        if (i, j) in self.seen:
            return
        self.seen.add((i, j))
        self.recurse(i - 1, j)
        self.recurse(i + 1, j)
        self.recurse(i, j + 1)
        self.recurse(i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        seen = {}
        islands = 0
        self.xmax = len(grid)
        self.ymax = len(grid[0])
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in self.seen:
                    continue
                else:
                    if grid[i][j] == '1': # island we haven't seen yet
                        self.recurse(i, j)
                        islands += 1
        return islands
                #(i, j) is our node, check if its already assigned an island

        