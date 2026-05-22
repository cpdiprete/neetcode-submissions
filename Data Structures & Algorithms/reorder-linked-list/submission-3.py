# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head):
        hare = head
        tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise
    def invertSecondHalf(self, tortoise):
        prev = None
        dummy = tortoise.next
        tortoise.next = None
        tortoise = dummy
        while tortoise:
            dummy = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = dummy
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        # improved solution, split the list and merge them
        # split down the middle using tortoise and hare
        tortoise = self.findMiddle(head)
        invertedHead = self.invertSecondHalf(tortoise)
        # now I have the tail and the middle element of the list, I can just invert starting from tortoise        
        # now I can sew these lists together 
        while head and invertedHead:
            nextHead = head.next
            head.next = invertedHead
            nextInvertedHead = invertedHead.next
            invertedHead.next = nextHead
            head = nextHead
            invertedHead = nextInvertedHead
        return





    # calvin's oringal less intuitive solution:
        # 1) track the head, the one in front, and the tail and reconnect them appropriatley
    # def find_tail(self, head):
    #     while head.next:
    #         if head.next.next is None:
    #             tail = head.next
    #             head.next = None
    #             return tail
    #         head = head.next
    #     return head # fallthrough
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     cur = head
    #     while cur.next:
    #         second = cur.next
    #         tail = self.find_tail(cur)# find the tail here, set it's next to none, also set prev tail's next to None             
    #         if tail == second:
    #             tail.next = None
    #         else:
    #             tail.next = second
    #         cur.next = tail
    #         cur = second
    #     return