import heapq
class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeads = []
        prefix = ListNode() # this's next will be the actual head of our returned list
        mergedNode = prefix
        # Step 1) Initialize a min-heap ordered by the value of the heads
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(minHeads, [lists[i].val, i])
        while len(minHeads) > 0:
            # Step 2) pop the min element, make it our next in line, if it's next isn't None, push it back in
            top_val, index = heapq.heappop(minHeads)
            mergedNode.next = lists[index]
            mergedNode = mergedNode.next
            lists[index] = lists[index].next
            if lists[index]:
                # add it to the heap and move it along
                heapq.heappush(minHeads, [lists[index].val, index])
        return prefix.next
            
            

            


