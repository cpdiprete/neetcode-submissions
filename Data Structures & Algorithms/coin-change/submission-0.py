class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        # base cases for each coin
        for coin in coins:
            if (coin > amount):
                continue
            else:
                dp[coin] = 1
    
        for i in range(1, amount + 1):
            if dp[i] == 1:
                continue
            jump = 2 ** 31
            for coin in coins:
                if (coin > i): # coin was too large
                    continue
                if (dp[i - coin] == -1):
                    continue
                else:
                    # we can make lower denomination with this coin
                    # print(f'jump for val: {i}')
                    jump = min(jump, dp[i-coin] + 1)
            if (jump != 2 ** 31):
                dp[i] = jump
        print(dp)
        return dp[amount]

        # dp[i] = min number of coins to make the value i
        # dp[]


        