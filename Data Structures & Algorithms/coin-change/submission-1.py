class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # notes on the pattern I used:
        # Basic Dynamic programming, the trick is the variable size of the given coins.
        # This impacts our base cases and looping behavior
        # Steps:
        # 1) initialize a DP array of size amount, where DP[i] = min coins used to make up i dollars
        # 2) Base cases for each coin
        #   2a) Select 0 coins for i = 0
        #   2b) For each coin, it takes 1 coin to reach that i value, do Dp[coin] = 1 for all coins in the proper range
        # 3) For all values up until total, if we can't reach this value with i - some coin, then we leave it at -1
        # 4) If we can reach it from another coin checkpoint, just use 1 more coin
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


        