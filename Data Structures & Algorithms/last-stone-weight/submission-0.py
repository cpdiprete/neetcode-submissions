import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need to maintain a max-Heap of heaviest stones, pop, smash and push
        heap = [(stone * -1) for stone in stones]
        heapq.heapify(heap)
        # some loop to check if the heap is emptry
        while (len(heap) > 1):
            print("hi")
            top = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second == 0 or top == 0:
                print("triggered")
                return top * -1
            kept = min(top, second) - max(top, second)
            if kept == 0:
                print(f"kept = 0 triggered")
                continue
            print(f"pushing kept: {kept}")
            heapq.heappush(heap, kept)
        if len(heap) == 1:
            return heapq.heappop(heap) * -1
        return 0
            