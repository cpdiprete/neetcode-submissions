class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The barriers between the container would hypothetically dissapear
        # its just finding the 2 points that maximize the area
        maxArea = 0
        # if we start from the front and back, and creep inwards based on the shorter of the 2, we will find the max area
        head = 0
        tail = len(heights) - 1
        while (head != tail):
            curArea = (tail - head) * min(heights[head], heights[tail])
            if curArea > maxArea:
                maxArea = curArea
            if (heights[head] <= heights[tail]):
                head += 1
            else:
                tail -= 1
        return maxArea
            

        