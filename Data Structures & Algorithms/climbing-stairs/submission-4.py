class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        # dp = [None] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # dp[2] = 2
        twoDown = 1
        oneDown = 1
        for i in range(2, n + 1):
            cur = oneDown + twoDown
            dummy = oneDown
            oneDown = cur
            twoDown = dummy
            # 1) Jumping 2 spots from [i - 2], OR Jumping 1 spot twice from [i - 1]
            # OR
            # 2) Jumping 1 spot from [i - 1]
            # dp[i] = dp[i-2] + dp[i-1] 
        # print(dp)
        return cur
        # return dp[n]
        