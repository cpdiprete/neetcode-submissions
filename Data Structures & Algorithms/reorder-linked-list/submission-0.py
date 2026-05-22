# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_tail(self, head):
        while head.next:
            if head.next.next is None:
                tail = head.next
                head.next = None
                return tail
            head = head.next
        return head # fallthrough
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if we treat it like 2 linked lists then it's simply
        # just merging 2 of them 1 at a time from each
        cur = head
        while cur.next:
            second = cur.next
            tail = self.find_tail(cur)# find the tail here, set it's next to none, also set prev tail's next to None
            if tail == second:
                tail.next = None
            else:
                tail.next = second
            cur.next = tail
            cur = second
        return

            



        return head