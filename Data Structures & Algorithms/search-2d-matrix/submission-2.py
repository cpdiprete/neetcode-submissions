class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        head = 0
        tail = m - 1
        candidateRow = -1
        while (head <= tail):
            mid = (head + tail) // 2
            row = matrix[mid]
            row_head = row[0]
            row_back = row[n - 1]
            if target < row_head:
                tail = mid - 1
                continue
            elif target > row_back:
                head = mid + 1
                continue
            else:
                candidateRow = mid
                break
        if (candidateRow == -1):
            print("Row not found")
            return False
        
        # now we know it would be within this list   
        # binary search on the row
        head = 0
        tail = n - 1
        while (head <= tail):
            mid = (head + tail) // 2
            if matrix[candidateRow][mid] == target:
                return True
            elif matrix[candidateRow][mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return False


        