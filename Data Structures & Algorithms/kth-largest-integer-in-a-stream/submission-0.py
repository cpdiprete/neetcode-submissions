import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # maintain some min heap of the k largest elements
        self.heap = [-1001] * k
        heapq.heapify(self.heap)
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        top = heapq.heappop(self.heap)
        heapq.heappush(self.heap, max(top, val))
        return self.heap[0]


        