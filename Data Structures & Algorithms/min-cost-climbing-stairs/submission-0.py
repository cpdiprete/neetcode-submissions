class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Each stair may either be reached from:
        # 1) the previous stair
        # 2) 2 stairs down

        # steps[i] = minCost it takes to reach step i
        # steps[0] = minCost to reach step 0
        
        steps = [None] * (len(cost) + 1)
        steps[0] = 0
        steps[1] = 0
        steps[2] = min(cost[0], cost[1])
        for i in range(3, len(cost) + 1):
            steps[i] = min(steps[i -1] + cost[i - 1], steps[i - 2] + cost[i - 2])
        print(steps)
        return steps[len(cost)]