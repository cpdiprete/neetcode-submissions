class Solution:
    def findMin(self, nums: List[int]) -> int:
        # our condition checking should be based on when the tail < head values
        # just hone in on whatever end of the binary search is smaller
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            if (nums[head] <= nums[tail]):
                return nums[head] # already sorted
            mid = (head + tail) // 2
            if nums[tail] > nums[mid]: # appropriately sorted, the min must be on the left side then
                tail = mid 
            else: # head must be on this side
                head = mid + 1
        return nums[head]
        