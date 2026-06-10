class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flipped = dict()
        marked = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                # flip all to zeros
                    for r in range(len(matrix)):
                        marked.add((r, col))
                    for c in range(len(matrix[0])):
                        marked.add((row, c))
        for row, col in marked:
            matrix[row][col] = 0
                    
        
                    
        
        