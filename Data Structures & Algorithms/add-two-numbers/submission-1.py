# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def makeListNode(self, val, index):
        if index == 0:
            return ListNode(val[index])
        nextNode = self.makeListNode(val, index - 1)
        return ListNode(val[index], nextNode)

    def makeLinkedList(self, value):
        value = str(value) # eg. 975 
        return self.makeListNode(value, len(value) - 1)


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # get the 
        # total = 0
        # carry = False
        # brute force is just reverse the lists and add them
        place = 0
        total = 0
        while l1:
            total += (10 ** place) * l1.val
            l1 = l1.next
            place += 1
        place = 0
        while l2:
            total += (10 ** place) * l2.val
            l2 = l2.next
            place += 1
        print(f"making a list node for: {total}")
        return self.makeLinkedList(total)
        # now I can reverse the string and make new nodes

        
        