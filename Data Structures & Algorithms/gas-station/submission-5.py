class Solution:
    def isPossible(self, gas, cost):
        return (sum(gas) - sum(cost) >= 0)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # observations:
        # 1) no matter where I start from, each step will still have the same overall impact on the gas I have left
        # 2) I can arbitrarily start from the front, and keep track of the max gas - cost at any time. 
        #       a) if the gas is every 0 or negative, return -1
        # Solution:
        # track the total gas, and the starting index
        # to have reached any point i, it must mean that starting from prior to i accumulated a surplus
        # if at any point our gas tank is 0 or negative
        if not self.isPossible(gas, cost):
            return -1
        # since we made it here, it is definitely possible to do
        start = 0
        tank = 0
        cur = 0
        while cur < len(gas):
            stopSurplus = gas[cur] - cost[cur]
            tank += stopSurplus
            if tank < 0: # this and previos stops are not valid at all
                start = cur + 1
                tank = 0
            cur += 1
        return start
