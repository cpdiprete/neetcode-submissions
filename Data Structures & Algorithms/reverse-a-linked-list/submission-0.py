# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None
        prev = None
        cur = head
        while (cur.next):
            dummy = cur.next
            print(f"dummy: {dummy.val}")
            cur.next = prev
            prev = cur
            cur = dummy
            print(f"new cur: {cur.val}")
        cur.next = prev
        return cur

        