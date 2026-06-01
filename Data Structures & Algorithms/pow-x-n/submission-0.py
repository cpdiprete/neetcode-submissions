class Solution:
    def myPow(self, x: float, n: int) -> float:
        iters = n
        runningNum = 1
        if n >= 0:
            while iters > 0:
                runningNum *= x
                iters -= 1
            return runningNum
        else:
            while iters < 0:
                runningNum /= x
                iters += 1
            return runningNum


        