from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # treat minute passing as an edge on a graph
        inf = len(grid) * len(grid[0]) + 1
        # start from rotting fruits, tracking the path to get here
        rotten = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                elif grid[i][j] == 1:
                    grid[i][j] = inf
                elif grid[i][j] == 2:
                    grid[i][j] = 0 # source of our search
                    rotten.append((i, j))
        # start BFS from all rotten sources, updating rotten values values
        while rotten:
            cur = rotten.popleft()
            i = cur[0]
            j = cur[1]
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if i < (len(grid) - 1):
                neighbors.append((i + 1, j))
            if j < (len(grid[0]) - 1):
                neighbors.append((i, j + 1))
            for n in neighbors:
                if grid[n[0]][n[1]] != inf:
                    continue
                else:
                    grid[n[0]][n[1]] = min(grid[n[0]][n[1]], grid[i][j] + 1)
                    rotten.append((n[0], n[1]))
        maxPath = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == inf:
                    return -1 # this was never touched by some rotten path

                maxPath = max(grid[i][j], maxPath)
        return maxPath
            
            # check all of its neighbors to see if we should 

        