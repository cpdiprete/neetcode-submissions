import heapq

# heapq.heappush(heap, val)   # push a value
# heapq.heappop(heap)         # pop the minimum
# heap[0]                     # peek at the minimum (no pop)
# heapq.heapify(list)         # turn a list into a heap in-place, O(n)
# the idea is to make an initial min heap, and then start adding larger elements
# this basically lets us make a min-heap of the k-largest elements
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[0:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            top = heapq.heappop(heap)
            heapq.heappush(heap, max(top, nums[i]))
        return heap[0]