class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            numStr = str(n)
            newNum = 0
            for char in numStr:
                newNum += int(char) ** 2
            if newNum in seen:
                return False
            if newNum == 1:
                return True
            seen.add(newNum)
            n = newNum
        

        