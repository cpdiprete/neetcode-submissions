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
        place = 0
        total = 0
        carry = False
        while (l1 and l2):
            numberToAdd = l1.val + l2.val
            if carry:
                numberToAdd += 1
            if (numberToAdd) > 9:
                carry = True
                numberToAdd -= 10
            else:
                carry = False
            total += numberToAdd * (10 ** place)
            place += 1
            l1 = l1.next
            l2 = l2.next
        while l1:
            numberToAdd = l1.val
            if carry:
                numberToAdd += 1
            if numberToAdd > 9:
                numberToAdd -= 10
                carry = True
            else:
                carry = False
            total += (10 ** place) * numberToAdd
            place += 1
            l1 = l1.next
        while l2:
            numberToAdd = l2.val
            if carry:
                numberToAdd += 1
            if numberToAdd > 9:
                numberToAdd -= 10
                carry = True
            else:
                carry = False
            total += (10 ** place) * numberToAdd
            place += 1
            l2 = l2.next
        if carry:
            total += 1 * (10 ** place) 
        return self.makeLinkedList(total)
        # now I can reverse the string and make new nodes

        
        