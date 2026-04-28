class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # it can be 
        # 1) the individual rectangle standing up
        # OR
        # 2) the min height of some subset of rectangles
        # areas = [None] * len(heights)
        maxSeen = 0
        # combinedLen = 0
        # minHeight = 0
        start = 0
        # loop through each one where the current height is the min height we'll consider
        while start < len(heights):
            h = heights[start]
            pre = start
            post = start
            while (pre >= 0) and (heights[pre] >= h):
                    pre -= 1# continue
            while (post < len(heights)and heights[post] >= h):
                post += 1
            curArea = (post - pre - 1) * h
            maxSeen = max(curArea, maxSeen)
            start += 1
        return maxSeen

            


