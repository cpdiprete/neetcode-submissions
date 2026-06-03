# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # return true if cycle, false if not
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        if not head:
            return False
        rabbit = head.next
        while turtle and rabbit:
            if rabbit.next is None or rabbit.next.next is None:
                return False
            if rabbit.val == turtle.val or rabbit.next.val == turtle.val:
                return True
            turtle = turtle.next
            rabbit = rabbit.next.next
        return False
                
        