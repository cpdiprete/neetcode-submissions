
import collections   
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chest_set = collections.deque()
        # Instead of starting at the land and searching for the chests, I can start at chests and look for land
        # this way I can maintain a current distance from chest value
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    chest_set.append((i, j))
        # now I have all of the chests as my start for this bfs source search
        islands = collections.deque()
        # pop all of the chests from the deque, so we can bfs from all of them
        while chest_set:
            (i, j) = chest_set.popleft()
            neighbors = []
            if (i != 0):
                # add bottom
                neighbors.append((i - 1, j))
            if (i != (len(grid) - 1)):
                # add top
                neighbors.append((i + 1, j))
            if (j != 0):
                neighbors.append((i, j -1))
            if (j != len(grid[0]) - 1):
                neighbors.append((i, j + 1))
            for n in neighbors:
                old = grid[n[0]][n[1]]
                if old <= (grid[i][j] + 1):
                    # don't need to add, didn't replace
                    continue
                else:
                    grid[n[0]][n[1]] = grid[i][j] + 1
                    chest_set.append(n) # append this neighbor to search it's neighbors, because we did an update
        return


            # check neighbors, and update to our min(its value, our current value + 1) if its not water
            


        

                
        # self.grid = grid
        # self.maxX = len(grid)
        # self.maxY = len(grid[0])
        # self.seen = set()
        # self.inf = 2147483647
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if (i, j) in self.seen:
        #             continue
        #         else:
        #             self.DFS(i, j)
        # grid = self.grid
        # return
        
        

        