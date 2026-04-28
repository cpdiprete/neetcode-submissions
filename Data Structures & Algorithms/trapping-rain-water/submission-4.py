class Solution:
    def trap(self, height: List[int]) -> int:
        # key idea is considering how much water is on top of each column
        # precompute left and right max of each column
        leftMaxs = []
        rightMaxs = [None] * len(height)
        tLeft = 0
        tRight = 0
        for i in range(len(height)):
            leftMaxs.append(max(tLeft, height[i]))
            tLeft = max(tLeft, height[i])
        for i in range(len(height) - 1, -1, -1):
            rightMaxs[i] = max(tRight, height[i])
            tRight = max(tRight, height[i])
        
        print(rightMaxs)
        print(leftMaxs)
        # now I have precomputed the heights.. we can get how much water is on my head
        waterTotal = 0
        for i in range(len(height)):
            waterTotal += max(0, min(leftMaxs[i], rightMaxs[i]) - height[i])
        return waterTotal

        # # how can I make an array where arr[i] = (max left neighbor, max right neighbor)

        # trapped = 0
        # while i < len(height):
        #     # each column can only have the (min(left, right) - my_height) on top of my head
        #     left = i - 1
        #     right = i + 1

        # # # water can't be trapped until its enclosed on both sides
        # # # if I'm considering the left pointer (head), then any single column to its right, that
        # # # is as tall (or taller) will be the end of needing to track this one 
        # # trapped = 0
        # # left = 0
        # # right = 1
        # # while (right < len(height)):
        # #     lH = height[left]
        # #     rH = height[right]
        # #     if rH >= lH:
        # #         print(f"left: {left}, right: {right}")
        # #         # update trapped to the water between left and right, it should just be the area minus the blocking pillars
        # #         unblockedArea = min(lH, rH) * (right - left - 1)
        # #         print(f"unblocked Area: {unblockedArea}")
        # #         blockages = 0
        # #         for j in range(left + 1, right):
        # #             blockages += height[j]
        # #         blockedArea = max(unblockedArea - blockages, 0)
        # #         print(f"blocked area: {blockedArea}")
        # #         trapped += blockedArea
        # #         left = right
        # #     right += 1
        # # # do one sweep back to find if we missed a trap
        # # right = len(height) - 1
        # # maxStraggler = None
        # # maxRightHeight = 0
        # # while (right > left):
        # #     if (height[right] > maxRightHeight):
        # #         maxStraggler = right
        # #         maxRightHeight = height[right]
        # #     right -= 1
        # # # now find the leftover area
        # # if maxStraggler: # found one, more water to be trapped
        # #     print(f"STRAGGLER: left: {left}, right: {maxStraggler}")
        # #     unblockedArea = min(height[left], maxRightHeight) * (maxStraggler - left - 1)
            
        # #     print(f"unblocked Area: {unblockedArea}")
        # #     blockages = 0
        # #     for j in range(left + 1, maxStraggler):
        # #         blockages += height[j]
        # #     blockedArea = max(unblockedArea - blockages, 0)
        # #     print(f"blocked area: {blockedArea}")
        # #     trapped += blockedArea

        # # return trapped

        