class Solution:
    def __init__(self):
        self.maxIsland = 0
        self.seen = set()
    def recurse(self, i, j):
        if (i < 0) or (i >= self.maxX):
            return 0
        if (j < 0) or (j >= self.maxY):
            return 0
        if (i, j) in self.seen:
            return 0
        if self.grid[i][j] == 0:
            return 0
        self.seen.add((i, j))
        # else, we are a 1, and it's time to expand the island
        l = self.recurse(i - 1, j)
        r = self.recurse(i + 1, j)
        u = self.recurse(i, j + 1)
        d = self.recurse(i, j - 1)
        total = 1 + l + r + d + u
        print(f"total: {total}")
        self.maxIsland = max(self.maxIsland, total)
        return total
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxX = len(grid)
        self.maxY = len(grid[0])
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in self.seen or grid[i][j] == 0:
                    continue
                # else this is the start of a new island batch
                self.recurse(i, j)
        return self.maxIsland





    

        