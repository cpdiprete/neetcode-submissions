# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        if size == 1 or size == 0:
            return
        # I now know the size of total list
        removeIndex = size - n
        if removeIndex == 0:
            head = head.next
            return head
        curI = 0
        cur = head
        while curI <= removeIndex:
            if ((curI + 1) == removeIndex): # skip its next
                if not(cur.next is None):
                    cur.next = cur.next.next   
                    break
            cur = cur.next
            curI += 1
        return head