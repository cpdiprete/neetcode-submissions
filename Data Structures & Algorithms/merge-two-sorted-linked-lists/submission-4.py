# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return 
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        l1 = list1
        l2 = list2
        # find original head that we'll be adding to
        if l1.val <= l2.val:
            newHead = l1
            newLL = l1
            l1=l1.next
        else:
            newHead = l2
            newLL = l2
            l2=l2.next
        # modify them in place 
        while l1 and l2:
            if l1.val < l2.val:
                updated = l1
                l1=l1.next
            else:
                updated = l2
                l2=l2.next
            newLL.next = updated
            newLL = newLL.next
        while l1:
            newLL.next = l1
            l1=l1.next
            newLL = newLL.next
        while l2:
            newLL.next = l2
            l2=l2.next
            newLL = newLL.next
        return newHead













        # if (list2 is None) and list1 is None:
        #     return None
        # if list2 is None:
        #     return list1
        # if list1 is None:
        #     return list2
        # staged_head = None
        # if list1.val <= list2.val:
        #     merged = list1
        #     list1 = list1.next
        # else:
        #     merged = list2
        #     list2 = list2.next
        # staged_head = merged
        # # merged = merged.next
        # while (list1 and list2):
        #     if (list1.val <= list2.val):
        #         merged.next = list1
        #         list1 = list1.next
        #     else:
        #         merged.next = list2
        #         list2 = list2.next
        #     # print(f"merged: {merged}")
        #     merged = merged.next # move forward

        # if (list1):
        #     merged.next = list1
        # if (list2):
        #     merged.next = list2
        # return staged_head
        

        