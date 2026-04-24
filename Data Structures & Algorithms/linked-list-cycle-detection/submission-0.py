# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if head is None:
            return False
        cur = head
        visited.add(cur)
        while (cur.next):
            if cur.next in visited:
                return True
            else:
                visited.add(cur.next)
                cur = cur.next
        return False
        