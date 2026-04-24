# import numpy as np

def checkrowDuplicates(row):
    rowSet = set()
    for item in row:
        if item in rowSet and item != ".":
            return False
        rowSet.add(item)
    return True

def concatRows(rowList):
    rList = []
    for r in rowList:
        rList += r
    return rList

def checkBoxDuplicates(board):
    for row in range(0, 7, 3):
        b1 = concatRows([slot[0:3] for slot in board[row:row+3]])
        b2 = concatRows([slot[3:6] for slot in board[row:row+3]])
        b3 = concatRows([slot[6:9] for slot in board[row:row+3]])

        if not(checkrowDuplicates(b1)):
            return False
        if not(checkrowDuplicates(b2)):
            return False
        if not(checkrowDuplicates(b3)):
            return False
    return True
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we don't need to solve the sudoku, just check if its valid in its current state
        # we can make a 2x2 matrix of sets
        for i in range(len(board)):
            # 0-9 form a row
            if not(checkrowDuplicates(board[i])):
                return False
        for i in range(len(board)):
            column = [row[i] for row in board]
            if not(checkrowDuplicates(column)):
                return False
        return checkBoxDuplicates(board)

        return True

        
        
        